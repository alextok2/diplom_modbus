
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


from delete import get_value


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

        for register in input_registers:
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
    
    

    def set_validated_holding_registers(self, address, values):

        for register in self.holding_registers:
            if address == register["ADDR"]:
                if "RANGE" in register:
                    min_value, max_value = register["RANGE"]
                    print(register["RANGE"],min_value, max_value, values)
                    values = min(max(min_value, values), max_value)  
                    self.set_holding_registers(address, [values])

                elif "REGISTERS" in register:
                    if values not in register["REGISTERS"]:
                        print(register["REGISTERS"])
                        values = register["DEFAULT"]
                        self.set_holding_registers(address, [values])
                break

        

    



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
        # self.conn = sqlite3.connect('database copy 2.db')
        # self.c = self.conn.cursor()
        # self.create_logs_table()

    def configure_logger(self):
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler = logging.FileHandler('myapp.log')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    def create_logs_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS logs
                        (id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp REAL, input_registers BLOB)''')

    # def store_input_registers(self, registers):
    #     timestamp = time.time()
    #     registers_json = json.dumps(registers)
    #     self.c.execute("INSERT INTO logs (timestamp, input_registers) VALUES (?, ?)", (timestamp, registers_json))
    #     self.conn.commit()

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
                # data = {
                #     "flow_rate": new_flow_rate,
                #     "temperature": new_temperature,
                #     "pressure": new_pressure,
                #     "density": new_density,
                #     "board_temp": new_board_temp,
                #     "velocity": new_velocity,
                #     "vortex_frequency": new_vortex_frequency,
                #     "enthalpy": new_enthalpy
                # }
                # self.store_input_registers(data)
                
                time.sleep(1)

        except Exception as e:
            logger.error('An error occurred: %s', str(e))
        finally:
            self.server.stop()
            print("[-] Server stopped.")

# Assuming you have defined the required functions and classes
if __name__ == "__main__":

    
    
    app = ModbusServerApp(meter_type="water",ip_address = "46.167.103.130", port = 502)
    # app = ModbusServerApp(meter_type="power",ip_address = "127.0.0.1", port = 5002)
    
    app.run()




























































# # Configure the logger
# logger.setLevel(logging.DEBUG)  # Set the desired log level
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# # Create a file handler and set the formatter
# file_handler = logging.FileHandler('myapp.log')
# file_handler.setFormatter(formatter)

# # Add the file handler to the logger
# logger.addHandler(file_handler)







# start_time = time.time()

# server_ip_address = "127.0.0.1"
# server_port = 5002

# mydatabank = MyDataBank(holding_registers_water_meter, input_registers)
# server = ModbusServer(server_ip_address, server_port, no_block=True, data_bank=mydatabank)



# try:
#     server.start()
#     print("[+] Server is working on: IP: " + server_ip_address + " and PORT:" + str(server_port) + "")
#     print("[+] Type 'quit' to stop the server.")
    
#     srv_info = ModbusServer.ServerInfo()
#     srv_info.recv_frame = ModbusServer.Frame()
#     srv_info.recv_frame.mbap = ModbusServer.MBAP(unit_id=1)  # Set the desired unit_id
    



#     state = [0]
#     i = 0
#     while True:





            



#         new_flow_rate = get_interpolated_instantaneous_flow_rate()
#         new_temperature = get_temperature_value()
#         new_pressure = get_interpolated_pressure()
#         new_density = get_density_value(new_temperature)
        
#         new_board_temp = get_board_temperature()
#         new_velocity = get_velocity_value()
#         new_vortex_frequency = get_vortex_frequency(new_velocity)
#         new_enthalpy = get_enthalpy_value(new_temperature, new_pressure)

#         # print(new_temperature, new_pressure, new_density, new_board_temp, new_velocity, new_vortex_frequency, new_enthalpy)
#         # new_battery_level = round(100 - random.random(), 2)
#         # print(new_flow_rate, voltage_VNL1, new_temperature, voltage_VNL2, new_pressure, voltage_VNL3, new_battery_level)
        
#         import sqlite3

#         # Connect to SQLite3 database
#         conn = sqlite3.connect('database copy 2.db')
#         c = conn.cursor()

#         # Create the "logs" table if it doesn't exist
#         c.execute('''CREATE TABLE IF NOT EXISTS logs
#                     (id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp REAL, input_registers BLOB)''')

#         # Function to store Input Registers in the database
#         def store_input_registers(registers):
            
#             timestamp = time.time()
#             # Convert the list to a JSON string before storing
#             registers_json = json.dumps(registers)
#             c.execute("INSERT INTO logs (timestamp, input_registers) VALUES (?, ?)", (timestamp, registers_json))
#             conn.commit()

#         # Function to store the data in the database
#         data = {
#             "flow_rate": new_flow_rate,
#             "temperature": new_temperature,
#             "pressure": new_pressure,
#             "density": new_density,
#             "board_temp": new_board_temp,
#             "velocity": new_velocity,
#             "vortex_frequency": new_vortex_frequency,
#             "enthalpy": new_enthalpy
#         }
#         store_input_registers(data)




#         server.data_bank.set_input_registers(0, [new_flow_rate, new_temperature, new_pressure, new_density, new_board_temp, new_velocity, new_vortex_frequency, new_enthalpy])

#         sleep(1)

# except Exception as e:
#     logger.error('An error occurred: %s', str(e))
# finally:
#     server.stop()
#     print("[-] Server stopped.")









"""

Control Coils: turning the water flow on or off.
Status Coils: indicate whether a pump is currently running or not.
Alarm Coils: signal when certain conditions are met, such as when a temperature or pressure threshold is exceeded.
Interlock Coils:  prevent certain operations from occurring until certain conditions are met. For example, a coil could prevent a pump from starting until a valve is fully open.



Coils (0xxxx):

* Meter status flags (e.g., power status, error conditions)
* Control commands (e.g., reset meter, start/stop flow)


Discrete Inputs (1xxxx):

* Tamper detection flags
* Alarm conditions (e.g., low/high flow, leak detection)
* Meter event indicators (e.g., reverse flow, air detection)


Input Registers (3xxxx):

* Instantaneous flow rate. Calculation formula: Velocity × water area × 3600 seconds = instantaneous flow rate (cubic meters/hour). 
* Accumulated total consumption (e.g., cubic meters)
* Temperature readings
* Pressure readings
* Battery level or voltage
* Meter diagnostic values
реле протока


Flow rate
Temperature
Density
pressure
Vortex frequency
Velocity
Built-in temperature
Board temperature









does one of this input registers have wave representation in graph?

Holding Registers (4xxxx):

* Meter configuration parameters (e.g., pulse output settings, units)
* Billing data (e.g., tariff rates, consumption periods)
* Meter identification information (e.g., serial number, model)
* Firmware version
* User-configurable settings (e.g., alarm thresholds, date/time)
* Accumulated consumption data (e.g., monthly, yearly totals)
* Meter event logs or historical data











To visualize the changes in the mentioned indicators on a graph, various mathematical functions can be employed. Here are some suggestions for each indicator:

Instantaneous Flow Rate:

Sine or cosine functions can be used to simulate a periodic fluctuation in the flow rate, resembling a wave-like pattern.
For a more realistic simulation, you can combine multiple sine or cosine functions with different amplitudes, frequencies, and phase shifts to create a more complex waveform.


Accumulated Total Consumption:

A monotonically increasing function, such as a linear function or a quadratic function, can represent the continuous accumulation of consumption over time.
If there are periods of constant consumption followed by periods of varying consumption, you can use piecewise linear or piecewise polynomial functions.


Temperature Readings:

Sine or cosine functions can be used to simulate diurnal or seasonal temperature variations.
For more complex temperature patterns, you can combine multiple sine or cosine functions with different amplitudes, frequencies, and phase shifts.
If you want to simulate temperature fluctuations influenced by external factors, you can use random noise functions or stochastic processes.


Pressure Readings:

If the pressure readings are relatively stable, you can use a constant function or a function with small fluctuations around a mean value.
If there are periodic pressure variations, you can use sine or cosine functions.
For more complex pressure patterns, you can combine multiple trigonometric functions or use piecewise functions.


Battery Level or Voltage:

A decreasing exponential function or a hyperbolic function can be used to simulate the gradual discharge of a battery over time.
If there are charging events, you can use piecewise functions or step functions to represent the battery level increasing at specific intervals.


Meter Diagnostic Values:

If the diagnostic values are discrete and represent different states or conditions, you can use step functions or piecewise constant functions.
For continuous diagnostic values, you can use various functions depending on the expected behavior, such as linear functions, polynomials, or trigonometric functions.



It's important to note that the choice of mathematical functions will depend on the specific requirements and characteristics of the data you want to simulate. You may need to combine multiple functions or adjust their parameters to achieve the desired behavior.
Additionally, you can introduce random noise or stochastic processes to simulate real-world variability and add more realistic fluctuations to the simulated data.
"""