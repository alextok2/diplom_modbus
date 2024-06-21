
from pyModbusTCP.server import ModbusServer, DataBank
from pyModbusTCP.server import logger
import logging
from datetime import datetime
import random
from random import uniform
from pyModbusTCP import utils
import numpy as np 
from time import sleep
import time 
import math 
import json
import sqlite3

from generate_values.water_meter.gen_temperature import get_temperature_value, celsius_to_fahrenheit
from generate_values.water_meter.gen_pressure import get_interpolated_pressure
from generate_values.water_meter.gen_instantaneous_flow_rate import get_interpolated_instantaneous_flow_rate
from generate_values.water_meter.gen_density import get_density_value
from generate_values.water_meter.gen_velocity import get_velocity_value
from generate_values.water_meter.gen_board_temperature import get_board_temperature
from generate_values.water_meter.gen_vortex_frequency import get_vortex_frequency
from generate_values.water_meter.gen_enthalpy import get_enthalpy_value


from generate_values.power_meter.gen_value import get_value


def string_to_modbus_ascii(s):
    return ''.join('{:02X}'.format(ord(c)) for c in s)

def hex_string_to_word_list(hex_string):
    return [int(hex_string[i:i+4], 16) for i in range(0, len(hex_string), 4)]

# print(hex_string_to_word_list('53312E3031'))

def word_list_to_hex_string(word_list):
    return ''.join('{:04X}'.format(w) for w in word_list)

# print(word_list_to_hex_string([21297, 11824, 49]))

def modbus_ascii_to_string(s):
    return ''.join(chr(int(s[i:i+2], 16)) for i in range(0, len(s), 2))




class MyDataBank(DataBank):
    def __init__(self, holding_registers, input_registers):
        DataBank.__init__(self)


        self.holding_registers = holding_registers

        for register in holding_registers:
            address = register["ADDR"]
            default_value = register["DEFAULT"]
            
            type_register = register["TYPE"]

            if type_register == "ascii" or type_register == "string":
                # print(address, type_register, default_value,string_to_modbus_ascii(default_value), hex_string_to_word_list(string_to_modbus_ascii(default_value) )) 
                for word in hex_string_to_word_list(string_to_modbus_ascii(default_value)):
                    
                    self.set_holding_registers(address, [word])
                    address += 1
            else:
                # print(address, type_register, default_value)
                self.set_holding_registers(address, [default_value])

        for input_register in input_registers:
            address = input_register["ADDR"]
            default_value = input_register["DEFAULT"]
            
            type_register = input_register["TYPE"]

            if type_register == "ascii" or type_register == "string":
                # print(address, type_register, default_value,string_to_modbus_ascii(default_value), hex_string_to_word_list(string_to_modbus_ascii(default_value) )) 
                for word in hex_string_to_word_list(string_to_modbus_ascii(default_value)):
                    
                    self.set_input_registers(address, [word])
                    address += 1
            else:
                # print(address, type_register, default_value)
                self.set_input_registers(address, [default_value])
        self.set_coils(0, [True])




    def on_coils_change(self, address, from_value, to_value, srv_info):
        msg = 'change in coil space [{0!r:^5} > {1!r:^5}] at @ 0x{2:04X} from ip: {3:<15}'
        msg = msg.format(from_value, to_value, address, srv_info.client.address)
        logger.debug(msg)
    def on_holding_registers_change(self, address, from_value, to_value, srv_info):
        # print(f"on_holding_registers_change({address}, {from_value}, {to_value})")
        self.set_validated_holding_registers(address=address, values=to_value)
        msg = 'change in holding registers space [{0!r:^5} > {1!r:^5}] at @ 0x{2:04X} from ip: {3:<15}'
        msg = msg.format(from_value, to_value, address, srv_info.client.address)
        # print(set_validated_holding_registers(address, to_value))
        logger.debug(msg)
    
    

    # def set_validated_holding_registers(self, address, values):

    #     for register in self.holding_registers:
    #         if address == register["ADDR"]:
    #             if "RANGE" in register:
    #                 min_value, max_value = register["RANGE"]
    #                 print(register["RANGE"],min_value, max_value, values)
    #                 values = min(max(min_value, values), max_value)  
    #                 self.set_holding_registers(address, [values])

    #             elif "REGISTERS" in register:
    #                 if values not in register["REGISTERS"]:
    #                     print(register["REGISTERS"])
    #                     values = register["DEFAULT"]
    #                     self.set_holding_registers(address, [values])
    #             break
    def set_validated_holding_registers(self, address, value, holding_registers):
        for register in holding_registers:
            if address == register["ADDR"]:
                if "RANGE" in register:
                    if not (register["RANGE"][0] <= value <= register["RANGE"][-1]):
                        
                        value = register["DEFAULT"]
                        self.set_holding_registers(address, [value])


                elif "REGISTERS" in register:
                    if value not in register["REGISTERS"]:
                        
                        value = register["DEFAULT"]
                        self.set_holding_registers(address, [value])


                elif "RANGES" in register:
                    valid = False
                    for rng in register["RANGES"]:
                        if value == rng:
                            valid = True
                            self.set_holding_registers(address, [rng])

                    if not valid:
                        
                        value = register["DEFAULT"]
                        self.set_holding_registers(address, [value])



        

    



class ModbusServerApp:
    def __init__(self, meter_type="water", ip_address="127.0.0.1", port=5002):
        self.configure_logger()
        self.start_time = time.time()
        self.meter_type = meter_type
        if self.meter_type == "water":
            from registers import holding_registers_water_meter, input_registers_water_meter
            self.mydatabank = MyDataBank(holding_registers_water_meter, input_registers_water_meter)
            self.server = ModbusServer(ip_address, port, no_block=True, data_bank=self.mydatabank)
        elif self.meter_type == "power":
            from registers import holding_registers_power_meter, input_registers_power_meter
            self.mydatabank = MyDataBank(holding_registers_power_meter, input_registers_power_meter)
            self.server = ModbusServer(ip_address, port, no_block=True, data_bank=self.mydatabank)


    def configure_logger(self):
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler = logging.FileHandler('myapp.log')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)





    def run(self):
        try:
            self.server.start()

            while True:
                if self.meter_type == "water":


                    
                    # Flow rate 202 30203 
                    new_flow_rate = get_interpolated_instantaneous_flow_rate() * 100
                    # print(new_flow_rate)
                    self.server.data_bank.set_input_registers(203, [new_flow_rate])
                    # Flow rate(%) 200 30201 
                    procent_flow_rate = 80 * (new_flow_rate / 100) 
                    self.server.data_bank.set_input_registers(201, [procent_flow_rate])
                    # Temperature 206 30207 
                    new_temperature = get_temperature_value()
                    self.server.data_bank.set_input_registers(207, [new_temperature])
                    # Temperature(%) 204 30205 
                    procent_tempeature = 80 * new_temperature / 100
                    self.server.data_bank.set_input_registers(205, [procent_tempeature])
                    # Total 212 30213 
                    total = new_flow_rate + new_temperature
                    self.server.data_bank.set_input_registers(213, [total])
                    # Density 214 30215 
                    new_density = get_density_value(new_temperature)
                    self.server.data_bank.set_input_registers(215, [new_density])
                    # Density ratio 216 30217 
                    density_ratio = 100 * (new_density - 0.9) / 0.1
                    self.server.data_bank.set_input_registers(217, [density_ratio])
                    # Selected temperature 220 30221 
                    selected_temperature = 20 + (new_temperature - 20) / 80 * 50
                    self.server.data_bank.set_input_registers(221, [selected_temperature])
                    # Selected pressure 222 30223 
                    new_pressure = get_interpolated_pressure()
                    self.server.data_bank.set_input_registers(223, [new_pressure])
                    # Enthalpy 218 30219 
                    new_enthalpy = get_enthalpy_value(new_temperature, new_pressure)
                    self.server.data_bank.set_input_registers(219, [new_enthalpy])
                    # Velocity 226 30227 
                    new_velocity = get_velocity_value() * 10
                    self.server.data_bank.set_input_registers(227, [new_velocity])
                    # Vortex frequency 224 30225 
                    new_vortex_frequency = get_vortex_frequency(new_velocity)
                    self.server.data_bank.set_input_registers(225, [new_vortex_frequency])
                    # Built-in temperature 228 30229 
                    built_in_temperature = 20 + (get_board_temperature() - 20) / 80 * 50
                    self.server.data_bank.set_input_registers(229, [built_in_temperature])
                    # Board temperature 232 30233
                    new_board_temp = get_board_temperature()
                    self.server.data_bank.set_input_registers(233, [new_board_temp])
                    

                    
                    
                    
                    
                    
                    
                    

                    self.server.data_bank.set_input_registers(0, [new_flow_rate, new_temperature, new_pressure, new_density, new_board_temp, new_velocity, new_vortex_frequency, new_enthalpy])
                elif self.meter_type == "power":
                    

                    # Constants
                    SAMPLING_INTERVAL_VOLTAGE = 600
                    SAMPLING_INTERVAL_CURRENT = 300
                    SAMPLING_INTERVAL_POWER = 600
                    SAMPLING_INTERVAL_ENERGY = 3600
                    SAMPLING_INTERVAL_ANGLE = 600



                    

                    # Voltage RMS (Urms) and Peak (Upeak)
                    Urms_L1 = get_value(0, RANGE=(200, 240), SAMPLING_INTERVAL=SAMPLING_INTERVAL_VOLTAGE)
                    self.server.data_bank.set_input_registers(0x10d9, [Urms_L1])
                    Upeak_L1 = get_value(0, RANGE=(282, 340), SAMPLING_INTERVAL=SAMPLING_INTERVAL_VOLTAGE)
                    self.server.data_bank.set_input_registers(0x1810, [Upeak_L1])
                    Urms_L2 = get_value(0, RANGE=(200, 240), SAMPLING_INTERVAL=SAMPLING_INTERVAL_VOLTAGE)
                    self.server.data_bank.set_input_registers(0x10da, [Urms_L2])
                    Upeak_L2 = get_value(0, RANGE=(282, 340), SAMPLING_INTERVAL=SAMPLING_INTERVAL_VOLTAGE)
                    self.server.data_bank.set_input_registers(0x1812, [Upeak_L2])
                    Urms_L3 = get_value(0, RANGE=(200, 240), SAMPLING_INTERVAL=SAMPLING_INTERVAL_VOLTAGE)
                    self.server.data_bank.set_input_registers(0x10db, [Urms_L3])
                    Upeak_L3 = get_value(0, RANGE=(282, 340), SAMPLING_INTERVAL=SAMPLING_INTERVAL_VOLTAGE)
                    self.server.data_bank.set_input_registers(0x1814, [Upeak_L3])

                    # Frequency
                    Frequency = get_value(0, RANGE=(59, 61), SAMPLING_INTERVAL=SAMPLING_INTERVAL_ANGLE)
                    self.server.data_bank.set_input_registers(0x10f8, [Frequency])

                    # Voltage angles
                    Voltage_angle_L1 = 0
                    self.server.data_bank.set_input_registers(0x10fd, [Voltage_angle_L1])
                    Voltage_angle_L2 = get_value(0, RANGE=(-120, -100), SAMPLING_INTERVAL=SAMPLING_INTERVAL_ANGLE)
                    self.server.data_bank.set_input_registers(0x10fe, [Voltage_angle_L2])
                    Voltage_angle_L3 = get_value(0, RANGE=(100, 120), SAMPLING_INTERVAL=SAMPLING_INTERVAL_ANGLE)
                    self.server.data_bank.set_input_registers(0x10ff, [Voltage_angle_L3])

                    # Current RMS (Irms) and Peak (Ipeak)
                    Irms_L1 = get_value(0, RANGE=(0, 10), SAMPLING_INTERVAL=SAMPLING_INTERVAL_CURRENT)
                    self.server.data_bank.set_input_registers(0x10dd, [Irms_L1])
                    Ipeak_L1 = get_value(0, RANGE=(Irms_L1, Irms_L1 * np.sqrt(2)), SAMPLING_INTERVAL=SAMPLING_INTERVAL_CURRENT)
                    self.server.data_bank.set_input_registers(0x1818, [Ipeak_L1])
                    Irms_L2 = get_value(0, RANGE=(0, 10), SAMPLING_INTERVAL=SAMPLING_INTERVAL_CURRENT)
                    self.server.data_bank.set_input_registers(0x10de, [Irms_L2])
                    Ipeak_L2 = get_value(0, RANGE=(Irms_L2, Irms_L2 * np.sqrt(2)), SAMPLING_INTERVAL=SAMPLING_INTERVAL_CURRENT)
                    self.server.data_bank.set_input_registers(0x181a, [Ipeak_L2])
                    Irms_L3 = get_value(0, RANGE=(0, 10), SAMPLING_INTERVAL=SAMPLING_INTERVAL_CURRENT)
                    self.server.data_bank.set_input_registers(0x10df, [Irms_L3])
                    Ipeak_L3 = get_value(0, RANGE=(Irms_L3, Irms_L3 * np.sqrt(2)), SAMPLING_INTERVAL=SAMPLING_INTERVAL_CURRENT)
                    self.server.data_bank.set_input_registers(0x181c, [Ipeak_L3])

                    # Power (P), Reactive Power (Q), Apparent Power (S), and Power Factor (PF)
                    P_L1 = get_value(0, RANGE=(0, 2400), SAMPLING_INTERVAL=SAMPLING_INTERVAL_POWER)
                    self.server.data_bank.set_input_registers(0x1302, [P_L1])
                    Q_L1 = get_value(0, RANGE=(-1200, 1200), SAMPLING_INTERVAL=SAMPLING_INTERVAL_POWER)
                    self.server.data_bank.set_input_registers(0x130a, [Q_L1])
                    S_L1 = np.sqrt(P_L1**2 + Q_L1**2)
                    self.server.data_bank.set_input_registers(0x1312, [S_L1])
                    PF_L1 = P_L1 / S_L1 if S_L1 != 0 else 0
                    self.server.data_bank.set_input_registers(0x10bd, [PF_L1])

                    P_L2 = get_value(0, RANGE=(0, 2400), SAMPLING_INTERVAL=SAMPLING_INTERVAL_POWER)
                    self.server.data_bank.set_input_registers(0x1304, [P_L2])
                    Q_L2 = get_value(0, RANGE=(-1200, 1200), SAMPLING_INTERVAL=SAMPLING_INTERVAL_POWER)
                    self.server.data_bank.set_input_registers(0x130c, [Q_L2])
                    S_L2 = np.sqrt(P_L2**2 + Q_L2**2)
                    self.server.data_bank.set_input_registers(0x1314, [S_L2])
                    PF_L2 = P_L2 / S_L2 if S_L2 != 0 else 0
                    self.server.data_bank.set_input_registers(0x10be, [PF_L2])

                    P_L3 = get_value(0, RANGE=(0, 2400), SAMPLING_INTERVAL=SAMPLING_INTERVAL_POWER)
                    self.server.data_bank.set_input_registers(0x1306, [P_L3])
                    Q_L3 = get_value(0, RANGE=(-1200, 1200), SAMPLING_INTERVAL=SAMPLING_INTERVAL_POWER)
                    self.server.data_bank.set_input_registers(0x130e, [Q_L3])
                    S_L3 = np.sqrt(P_L3**2 + Q_L3**2)
                    self.server.data_bank.set_input_registers(0x1316, [S_L3])
                    PF_L3 = P_L3 / S_L3 if S_L3 != 0 else 0
                    self.server.data_bank.set_input_registers(0x10bf, [PF_L3])

                    # Energy
                    AP_energy_L1 = get_value(0, RANGE=(0, 1000), SAMPLING_INTERVAL=SAMPLING_INTERVAL_ENERGY)
                    self.server.data_bank.set_input_registers(0x1204, [AP_energy_L1])
                    RP_energy_L1 = get_value(0, RANGE=(0, 500), SAMPLING_INTERVAL=SAMPLING_INTERVAL_ENERGY)
                    self.server.data_bank.set_input_registers(0x1224, [RP_energy_L1])
                    AP_energy_L2 = get_value(0, RANGE=(0, 1000), SAMPLING_INTERVAL=SAMPLING_INTERVAL_ENERGY)
                    self.server.data_bank.set_input_registers(0x1208, [AP_energy_L2])
                    RP_energy_L2 = get_value(0, RANGE=(0, 500), SAMPLING_INTERVAL=SAMPLING_INTERVAL_ENERGY)
                    self.server.data_bank.set_input_registers(0x1228, [RP_energy_L2])
                    AP_energy_L3 = get_value(0, RANGE=(0, 1000), SAMPLING_INTERVAL=SAMPLING_INTERVAL_ENERGY)
                    self.server.data_bank.set_input_registers(0x120c, [AP_energy_L2])
                    RP_energy_L3 = get_value(0, RANGE=(0, 500), SAMPLING_INTERVAL=SAMPLING_INTERVAL_ENERGY)
                    self.server.data_bank.set_input_registers(0x122c, [RP_energy_L3])

                    # Total values
                    Total_P = P_L1 + P_L2 + P_L3
                    self.server.data_bank.set_input_registers(0x1300, [Total_P])
                    Total_Q = Q_L1 + Q_L2 + Q_L3
                    self.server.data_bank.set_input_registers(0x1308, [Total_Q])
                    Total_S = np.sqrt(Total_P**2 + Total_Q**2)
                    self.server.data_bank.set_input_registers(0x1310, [Total_S])
                    Total_PF = Total_P / Total_S if Total_S != 0 else 0
                    self.server.data_bank.set_input_registers(0x10bc, [Total_PF])

                    Total_AP_energy = AP_energy_L1 + AP_energy_L2 + AP_energy_L3
                    self.server.data_bank.set_input_registers(0x1200, [Total_AP_energy])
                    Total_RP_energy = RP_energy_L1 + RP_energy_L2 + RP_energy_L3
                    self.server.data_bank.set_input_registers(0x1220, [Total_RP_energy])

                    # Phase angles (consistent with power factors)
                    Phase_angle_L1 = np.degrees(np.arccos(PF_L1))
                    self.server.data_bank.set_input_registers(0x10f9, [Phase_angle_L1])
                    Phase_angle_L2 = np.degrees(np.arccos(PF_L2))
                    self.server.data_bank.set_input_registers(0x10fa, [Phase_angle_L2])
                    Phase_angle_L3 = np.degrees(np.arccos(PF_L3))
                    self.server.data_bank.set_input_registers(0x10fb, [Phase_angle_L3])
                    

                    self.server.data_bank.set_input_registers(0, [Urms_L1, Upeak_L1, Urms_L2, Upeak_L2, Urms_L3, Upeak_L3,
                                                                     Frequency, Voltage_angle_L1, Voltage_angle_L2, Voltage_angle_L3,
                                                                     Irms_L1, Ipeak_L1, Irms_L2, Ipeak_L2, Irms_L3, Ipeak_L3,
                                                                     P_L1, Q_L1, S_L1, PF_L1, AP_energy_L1, RP_energy_L1,
                                                                     P_L2, Q_L2, S_L2, PF_L2, AP_energy_L2, RP_energy_L2,
                                                                     P_L3, Q_L3, S_L3, PF_L3, AP_energy_L3, RP_energy_L3,
                                                                     Total_P, Total_Q, Total_S, Total_PF, Total_AP_energy, Total_RP_energy,
                                                                     Phase_angle_L1, Phase_angle_L2, Phase_angle_L3])
                    # Print the generated values
                    # print(f"Urms_L1: {Urms_L1} V, Upeak_L1: {Upeak_L1} V")
                    # print(f"Urms_L2: {Urms_L2} V, Upeak_L2: {Upeak_L2} V")
                    # print(f"Urms_L3: {Urms_L3} V, Upeak_L3: {Upeak_L3} V")
                    # print(f"Frequency: {Frequency} Hz")
                    # print(f"Voltage angles: L1: {Voltage_angle_L1}°, L2: {Voltage_angle_L2}°, L3: {Voltage_angle_L3}°")
                    # print(f"Irms_L1: {Irms_L1} A, Ipeak_L1: {Ipeak_L1} A")
                    # print(f"Irms_L2: {Irms_L2} A, Ipeak_L2: {Ipeak_L2} A")
                    # print(f"Irms_L3: {Irms_L3} A, Ipeak_L3: {Ipeak_L3} A")
                    # print(f"P_L1: {P_L1} W, Q_L1: {Q_L1} var, S_L1: {S_L1} VA, PF_L1: {PF_L1}")
                    # print(f"P_L2: {P_L2} W, Q_L2: {Q_L2} var, S_L2: {S_L2} VA, PF_L2: {PF_L2}")
                    # print(f"P_L3: {P_L3} W, Q_L3: {Q_L3} var, S_L3: {S_L3} VA, PF_L3: {PF_L3}")
                    # print(f"AP energy L1: {AP_energy_L1} kWh, RP energy L1: {RP_energy_L1} kvarh")
                    # print(f"AP energy L2: {AP_energy_L2} kWh, RP energy L2: {RP_energy_L2} kvarh")
                    # print(f"AP energy L3: {AP_energy_L3} kWh, RP energy L3: {RP_energy_L3} kvarh")
                    # print(f"Total P: {Total_P} W, Total Q: {Total_Q} var, Total S: {Total_S} VA, Total PF: {Total_PF}")
                    # print(f"Total AP energy: {Total_AP_energy} kWh, Total RP energy: {Total_RP_energy} kvarh")
                    # print(f"Phase angles: L1: {Phase_angle_L1}°, L2: {Phase_angle_L2}°, L3: {Phase_angle_L3}°")

                
                time.sleep(1)

        except Exception as e:
            logger.error('An error occurred: %s', str(e))
        finally:
            self.server.stop()
            print("[-] Server stopped.")

# Assuming you have defined the required functions and classes
if __name__ == "__main__":

    
    
    app = ModbusServerApp(meter_type="water",ip_address = "0.0.0.0", port = 5002)
    # app = ModbusServerApp(meter_type="power",ip_address = "0.0.0.0", port = 5002)
    
    app.run()

