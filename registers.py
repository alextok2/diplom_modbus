

holding_registers_water_meter = [
# Set baud rate 0 40001 Uint8 1 0:1200 bps 1:2400 bps 2:4800 bps 3:9600 bps 4:19200 bps 4:19200 bps -
{"ADDR": 0, "TYPE": "uint8", "REGISTERS": ["1200", "2400", "4800", "9600", "19200"], "DEFAULT": 0},
# Set parity 1 40002 Uint8 1 0:None 1:Odd 2:Even 2:Even -
{"ADDR": 1, "TYPE": "uint8", "REGISTERS": [0], "VALUES": [None, "Odd", "Even"], "DEFAULT": 0},
# Set stop bit 2 40003 Uint8 1 0:1 bit 1:2 bits 0:1 bit - 
{"ADDR": 2, "TYPE": "uint8", "REGISTERS": [0], "VALUES": [0, 1], "DEFAULT": 0},
# Set response delay time 3 40004 Uint8 1 10 to 200 10 ms 
{"ADDR": 3, "TYPE": "uint8", "REGISTERS": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200], "DEFAULT": 10},
# Set slave address 4 40005 Uint8 1 1 to 247 1 - 
{"ADDR": 4, "TYPE": "uint8", "RANGE": [1, 247], "DEFAULT": 1},
# Set data format 4byte 5 40006 Uint8 1 0:ABCD 1:CDAB 2:BADC 3:DCBA 0:ABCD - 
{"ADDR": 5, "TYPE": "uint8", "REGISTERS": ["ABCD", "CDAB", "BADC", "DCBA"], "DEFAULT": 0},
# Set data format float 6 40007 Uint8 1 0:ABCD 1:CDAB 2:BADC 3:DCBA 0:ABCD - 
{"ADDR": 6, "TYPE": "uint8", "REGISTERS": ["ABCD", "CDAB", "BADC", "DCBA"], "DEFAULT": 0},
# Set data format 2byte 7 40008 Uint8 1 0:AB 1:BA 0:AB - 
{"ADDR": 7, "TYPE": "uint8", "REGISTERS": ["AB", "BA"], "DEFAULT": 0},
# Set data format string 8 40009 Uint8 1 0:AB 1:BA 0:AB - 
{"ADDR": 8, "TYPE": "uint8", "REGISTERS": ["AB", "BA"], "DEFAULT": 0},
# Modbus restart 9 40010 Uint8 1 0:Not execute 1:Execute 0:Not execute -
{"ADDR": 9, "TYPE": "uint8", "REGISTERS": ["Not execute", "Execute"], "DEFAULT": 0},
# Fluid type 400 40401 Uint8 1 0:Liquid 1:Gas 2:Water 3:Steam 0:Liquid - 
{"ADDR": 0, "TYPE": "uint8", "REGISTERS": ["Liquid", "Gas", "Water", "Steam"], "DEFAULT": 0},
# Flow select 401 40402 Uint8 1 0:Volume 1:Mass 2:Standard/Normal 3:Energy 0:Volume - 
{"ADDR": 1, "TYPE": "uint8", "REGISTERS": ["Volume", "Mass", "Standard/Normal", "Energy"], "DEFAULT": 0},
# Volume unit 402 40403 Uint8 1 0:m3 1:km3 2:l 3:mcf 4:cf 5:kcf 6:USgal 7:kUSgal 8:UKgal 9:kUKgal 10:mbbl 11:bbl 12:kbbl 0:m3 - 
{"ADDR": 2, "TYPE": "uint8", "REGISTERS": ["m3", "km3", "l", "mcf", "cf", "kcf", "USgal", "kUSgal", "UKgal", "kUKgal", "mbbl", "bbl", "kbbl"], "DEFAULT": 0},
# Mass unit 403 40404 Uint8 1 0:kg 1:t 2:lb 3:klb 0:kg - 
{"ADDR": 3, "TYPE": "uint8", "REGISTERS": ["kg", "t", "lb", "klb"], "DEFAULT": 0},
# Standard/Normal unit 404 40405 Uint8 1 0:(N)m3 1:k(N)m3 2:M(N)m3 3:(N)l 4:(S)m3 5:k(S)m3 6:M(S)m3 7:(S)l 8:(S)cf 9:k(S)cf 10:M(S)cf 0:(N)m3 - 
{"ADDR": 4, "TYPE": "uint8", "REGISTERS": ["(N)m3", "k(N)m3", "M(N)m3", "(N)l", "(S)m3", "k(S)m3", "M(S)m3", "(S)l", "(S)cf", "k(S)cf", "M(S)cf"], "DEFAULT": 0},
# Energy unit 405 40406 Uint8 1 0:kJ 1:MJ 2:GJ 3:TJ 4:BTU 5:kBTU 6:MBTU 0:kJ -
{"ADDR": 5, "TYPE": "uint8", "REGISTERS": ["kJ", "MJ", "GJ", "TJ", "BTU", "kBTU", "MBTU"], "DEFAULT": 0},
# Time unit 406 40407 Uint8 1 0:/s 1:/min 2:/h 3:/d 2:/h -
{"ADDR": 6, "TYPE": "uint8", "REGISTERS": ["/s", "/min", "/h", "/d"], "DEFAULT": 0},
# Flow span 407 40408 Float 2 0.0< to 99999.9 10.0 Flow unit
{"ADDR": 7, "TYPE": "float", "RANGE": [0.0, 99999.9], "DEFAULT": 10.0},
# Flow damping 409 40410 Float 2 0.0 to 200.0 4.0 s 
{"ADDR": 9, "TYPE": "float", "RANGE": [0.0, 200.0], "DEFAULT": 4.0},
# Flow lowcut 411 40412 Float 2 1/2 or equivalent of minimum flow velocity to 99999.9 0.47 Flow unit 
{"ADDR": 11, "TYPE": "float", "RANGE": [1/2, 99999.9], "DEFAULT": 0.47},
# Flow user conversion 413 40414 Uint8 1 0:Off 1:On 0:Off 
{"ADDR": 13, "TYPE": "uint8", "REGISTERS": ["Off", "On"], "DEFAULT": 0},
# - Flow user unit 414 40415 ASCII 4 - " " - 
{"ADDR": 14, "TYPE": "ascii", "LENGTH": 4, "DEFAULT": " "},
# Flow conversion factor 418 40419 Float 2 0.0< to 99999.9 1.0 - 
{"ADDR": 18, "TYPE": "float", "RANGE": [0.0, 99999.9], "DEFAULT": 1.0},
# Pulse/Status output mode 500 40501 Uint8 1 0:Off 1:Scaled pulse 2:Unscaled pulse 3:Frequency 4:Alarm switch 5:Limit switch 0:Off - 
{"ADDR": 500, "TYPE": "uint8", "REGISTERS": ["Off", "Scaled pulse", "Unscaled pulse", "Frequency", "Alarm switch", "Limit switch"], "DEFAULT": 0},
# Pulse output rate 501 40502 Float 2 0< to 99999.9 1.0 Pulse output rate unit 
{"ADDR": 501, "TYPE": "float", "RANGE": [0, 99999.9], "DEFAULT": 1.0},
# Frequency output select 503 40504 Uint8 1 0:Flow rate 1:Temperature 0:Flow rate - 
{"ADDR": 503, "TYPE": "uint8", "REGISTERS": ["Flow rate", "Temperature"], "DEFAULT": 0},
# Frequency output zero 504 40505 Float 2 0.0 to 10000.0 0.0 Hz
{"ADDR": 504, "TYPE": "float", "RANGE": [0.0, 10000.0], "DEFAULT": 0.0},
# Frequency output span 506 40507 Float 2 0.0 to 10000.0 10000.0 Hz
{"ADDR": 506, "TYPE": "float", "RANGE": [0.0, 10000.0], "DEFAULT": 10000.0},
# Status output direction 508 40509 Uint8 1 0:On active 1:Off active 0:On active - 
{"ADDR": 508, "TYPE": "uint8", "REGISTERS": ["On active", "Off active"], "DEFAULT": 0},
# Alarm switch select 509 40510 Uint8 1 0:All alarm/warning 1:All alarm 2:System/Process alarm 3:System alarm 4:Process alarm 5:Setting alarm 6:Warning 0:All alarm/warning - 
{"ADDR": 509, "TYPE": "uint8", "REGISTERS": ["All alarm/warning", "All alarm", "System/Process alarm", "System alarm", "Process alarm", "Setting alarm", "Warning"], "DEFAULT": 0},
# Limit switch select 510 40511 Uint8 1 0:Flow rate 1:Temperature 3:Totalizer 0:Flow rate - 
{"ADDR": 511, "TYPE": "uint8", "REGISTERS": ["Flow rate", "Temperature", "Totalizer"], "DEFAULT": 0},
# Limit switch mode 511 40512 Uint8 1 0:Low limit 1:High limit 0:Low limit - 
{"ADDR": 512, "TYPE": "uint8", "REGISTERS": ["Low limit", "High limit"], "DEFAULT": 0},
# Limit switch level 512 40513 Float 2 -99999.9 to 99999.9 0.0 Limit switch unit
{"ADDR": 513, "TYPE": "float", "RANGE": [-99999.9, 99999.9], "DEFAULT": 0.0},
# Limit switch hysteresis 514 40515 Float 2 0.0 to 99999.9 0.0 Limit switch unit 
{"ADDR": 515, "TYPE": "float", "RANGE": [0.0, 99999.9], "DEFAULT": 0.0},
# Display line upper 600 40601 Uint8 1 0:Flow rate(%) 1:Flow rate 2:Temperature(%) 0:Flow rate(%) - 
{"ADDR": 601, "TYPE": "uint8", "REGISTERS": ["Flow rate(%)", "Flow rate", "Temperature(%)"], "DEFAULT": 0},
# Display line lower 601 40602 Uint8 1 0:Off 1:Totalizer 2:Temperature 0:Off - 
{"ADDR": 602, "TYPE": "uint8", "REGISTERS": ["Off", "Totalizer", "Temperature"], "DEFAULT": 0},
# Display period 602 40603 Uint8 1 0:0.25s 1:0.5s 2:1s 3:2s 4:4s 5:8s 0:0.25s - 
{"ADDR": 603, "TYPE": "uint8", "REGISTERS": ["0.25s", "0.5s", "1s", "2s", "4s", "8s"], "DEFAULT": 0},
# Display startup 603 40604 Uint8 1 0:Off 1:On 0:Off - Display NE107 604 40605 Uint8 1 0:Off 1:On 0:Off - 
{"ADDR": 605, "TYPE": "uint8", "REGISTERS": ["Off", "On"], "DEFAULT": 0},
# Display format flow 605 40606 Uint8 1 0:Auto 1:0 digit 2:1 digit 3:2 digit 4:3 digit 5:4 digit 0:Auto - 
{"ADDR": 606, "TYPE": "uint8", "REGISTERS": ["Auto", "0 digit", "1 digit", "2 digit", "3 digit", "4 digit"], "DEFAULT": 0},
# Display format temperature 606 40607 Uint8 1 0:0 digit 1:1 digit 2:2 digit 3:3 digit 4:4 digit 0:0 digit - 
{"ADDR": 607, "TYPE": "uint8", "REGISTERS": ["0 digit", "1 digit", "2 digit", "3 digit", "4 digit"], "DEFAULT": 0},
# Display format pressure 607 40608 Uint8 1 0:0 digit 1:1 digit 2:2 digit 3:3 digit 4:4 digit 0:0 digit - 
{"ADDR": 608, "TYPE": "uint8", "REGISTERS": ["0 digit", "1 digit", "2 digit", "3 digit", "4 digit"], "DEFAULT": 0},
# Totalizer start/stop 700 40701 Uint8 1 0:Stop 1:Start 0:Stop -
{"ADDR": 701, "TYPE": "uint8", "REGISTERS": ["Stop", "Start"], "DEFAULT": 0},
# Totalizer reset/preset 701 40702 Uint8 1 0:Not execute 1:Reset 2:Preset 0:Not execute - 
{"ADDR": 702, "TYPE": "uint8", "REGISTERS": ["Not execute", "Reset", "Preset"], "DEFAULT": 0},
# Totalizer rate 702 40703 Float 2 0.00001 to 99999.9 1.0 Total rate unit 
{"ADDR": 703, "TYPE": "float", "RANGE": [0.00001, 99999.9], "DEFAULT": 1.0},
# Totalizer preset value 704 40705 Float 2 0.0 to 99999.9 0.0 Totalizer unit 
{"ADDR": 705, "TYPE": "float", "RANGE": [0.0, 99999.9], "DEFAULT": 0.0},
# Totalizer reset mode 706 40707 Uint8 1 0:Reset 1:Hold only display 2:Hold 0:Reset - 
{"ADDR": 707, "TYPE": "uint8", "REGISTERS": ["Reset", "Hold only display", "Hold"], "DEFAULT": 0},
# Nominal size 800 40801 Uint8 1 1:15mm 2:25mm 3:40mm 4:50mm 5:80mm 6:100mm 7:150mm 8:200mm 9:250mm 10:300mm 11:400mm 2:25mm - 
{"ADDR": 801, "TYPE": "uint8", "REGISTERS": ["15mm", "25mm", "40mm", "50mm", "80mm", "100mm", "150mm", "200mm", "250mm", "300mm", "400mm"], "DEFAULT": 2},
# Body type 801 40802 Uint8 1 0:General 1:One size down 2:Two size down 4:High pressure 0:General - 
{"ADDR": 802, "TYPE": "uint8", "REGISTERS": ["General", "One size down", "Two size down", "High pressure"], "DEFAULT": 0},
# Sensor type 802 40803 Uint8 1 0:Standard 1:Standard w/ temp sensor 2:High temperature 3:High temperature w/ temp sensor 4:Cryogenic 6:Long neck 7 Long neck w/ temp sensor 0:Standard - 
{"ADDR": 803, "TYPE": "uint8", "REGISTERS": ["Standard", "Standard w/ temp sensor", "High temperature", "High temperature w/ temp sensor", "Cryogenic", "Long neck", "Long neck w/ temp sensor"], "DEFAULT": 0},
# Connection type 803 40804 Uint8 1 0:Integral 1:Remote 0:Integral -
{"ADDR": 804, "TYPE": "uint8", "REGISTERS": ["Integral", "Remote"], "DEFAULT": 0},
#  K factor unit 804 40805 Uint8 1 0:p/l 1:p/USgal 2:p/UKgal 0:p/l - 
{"ADDR": 805, "TYPE": "uint8", "REGISTERS": ["p/l", "p/USgal", "p/UKgal"], "DEFAULT": 0},
# K factor 805 40806 Float 2 0.0< to 99999.9 68.6 K factor unit
{"ADDR": 806, "TYPE": "float", "RANGE": [0.0, 99999.9], "DEFAULT": 68.6},
# Process temperature 807 40808 Uint32 2 0:-29 to +250 degC 1:-40 to +250 degC*1 2:-40 to +450 degC*1 3:-40 to +400 degC*1 4:-196 to +250 degC 0:-29 to +250°C - 
{"ADDR": 808, "TYPE": "uint32", "REGISTERS": ["-29 to +250°C", "-40 to +250°C", "-40 to +450°C", "-40 to +400°C", "-196 to +250°C"], "DEFAULT": 0},
# Max pressure 809 40810 Float 2 0.0 to 99999.9 0.0 MPa at 38degC 
{"ADDR": 810, "TYPE": "float", "RANGE": [0.0, 99999.9], "DEFAULT": 0.0},
# Sensor S/N 811 40812 ASCII 8 - " " - Sensor backup/restore 820 40821 Uint8 1 0:Not execute 1:Backup parameter 3:Restore parameter 4:Restore parameter(factory) 0:Not execute - 
{"ADDR": 821, "TYPE": "uint8", "REGISTERS": ["Not execute", "Backup parameter", "Restore parameter", "Restore parameter(factory)"], "DEFAULT": 0},
# Temperature unit 900 40901 Uint8 1 0:degC 1:degF 2:K 0:degC - Temperature LRV 901 40902 Float 2 -999.9 to 999.9 -40.0 Temperature unit
{"ADDR": 902, "TYPE": "float", "RANGE": [-999.9, 999.9], "DEFAULT": -40.0},
# Temperature URV 903 40904 Float 2 -999.9 to 999.9 250.0 Temperature unit 
{"ADDR": 904, "TYPE": "float", "RANGE": [-999.9, 999.9], "DEFAULT": 250.0},
# Temperature damping 905 40906 Float 2 0.0 to 200.0 4.0 s Fixed temperature 907 40908 Float 2 -999.9 to 999.9 15.0 Temperature unit
{"ADDR": 908, "TYPE": "float", "RANGE": [-999.9, 999.9], "DEFAULT": 15.0},
# Base temperature 909 40910 Float 2 -999.9 to 999.9 15.0 Temperature unit 
{"ADDR": 910, "TYPE": "float", "RANGE": [-999.9, 999.9], "DEFAULT": 15.0},
# Temperature gain 911 40912 Float 2 0.0< to 99999.9 1.0 -
{"ADDR": 912, "TYPE": "float", "RANGE": [0.0, 99999.9], "DEFAULT": 1.0},
# Temperature offset 913 40914 Float 2 -999.9 to 999.9 0.0 Temperature unit
{"ADDR": 914, "TYPE": "float", "RANGE": [-999.9, 999.9], "DEFAULT": 0.0},
# Pressure unit 1100 41101 Uint8 1 0:kPa A 1:MPa A 2:bar A 3:psi A 4:kPa G 5:MPa G 6:bar G 7:psi G 1:MPa A -
{"ADDR": 1101, "TYPE": "uint8", "REGISTERS": ["kPa A", "MPa A", "bar A", "psi A", "kPa G", "MPa G", "bar G", "psi G"], "DEFAULT": 1},
# Fixed pressure 1107 41108 Float 2 abs:0.0< to 99999.9 guage:0.0 to 99999.9 0.10133 Pressure unit
{"ADDR": 1108, "TYPE": "float", "RANGE": [0.0, 99999.9], "DEFAULT": 0.10133},
# Base pressure 1109 41110 Float 2 abs:0.0< to 99999.9 guage:0.0 to 99999.9 0.10133 Pressure unit
{"ADDR": 1110, "TYPE": "float", "RANGE": [0.0, 99999.9], "DEFAULT": 0.10133},
# Air pressure 1111 41112 Float 2 0.0< to 99999.9 0.10133 Air pressure unit
{"ADDR": 1112, "TYPE": "float", "RANGE": [0.0, 99999.9], "DEFAULT": 0.10133},
# Density unit 1300 41301 Uint8 1 0:kg/m3 1:lb/cf 2:lb/USgal 3:lb/UKgal 0:kg/m3 -
{"ADDR": 1301, "TYPE": "uint8", "REGISTERS": ["kg/m3", "lb/cf", "lb/USgal", "lb/UKgal"], "DEFAULT": 0},
# Compensation type 1301 41302 Uint8 1 0:Not used 1:Built-in temp. 0:Not used -
{"ADDR": 1302, "TYPE": "uint8", "REGISTERS": ["Not used", "Built-in temp."], "DEFAULT": 0},
# Steam type 1302 41303 Uint8 1 0:Saturated steam 1:Superheated steam 0:Saturated steam -
{"ADDR": 1303, "TYPE": "uint8", "REGISTERS": ["Saturated steam", "Superheated steam"], "DEFAULT": 0},
# Fixed density 1304 41305 Float 2 0.0< to 99999.9 1000.0 Density unit
{"ADDR": 1305, "TYPE": "float", "RANGE": [0.0, 99999.9], "DEFAULT": 1000.0},
# Base density 1306 41307 Float 2 0.0< to 99999.9 1000.0 Density unit
{"ADDR": 1307, "TYPE": "float", "RANGE": [0.0, 99999.9], "DEFAULT": 1000.0},
# Dryness 1308 41309 Float 2 90.0 to 100.0 100.0 % Deviation 1310 41311 Float 2 0.0< to 99999.9 1.0 -
{"ADDR": 1311, "TYPE": "float", "RANGE": [0.0, 99999.9], "DEFAULT": 1.0},
# Temperature coefficient 1 1312 41313 Float 2 -99999.9 to 99999.9 0.0 1 / Temperature unit
{"ADDR": 1313, "TYPE": "float", "RANGE": [-99999.9, 99999.9], "DEFAULT": 0.0},
# Temperature coefficient 2 1314 41315 Float 2 -99999.9 to 99999.9 0.0 1 / Temperature unit
{"ADDR": 1315, "TYPE": "float", "RANGE": [-99999.9, 99999.9], "DEFAULT": 0.0},
# Enthalpy unit 1316 41317 Uint8 1 0:kJ/kg 1:MJ/kg 2:GJ/kg 3:TJ/kg 4:BTU/lb 0:kJ/kg - 
{"ADDR": 1317, "TYPE": "uint8", "REGISTERS": ["kJ/kg", "MJ/kg", "GJ/kg", "TJ/kg", "BTU/lb"], "DEFAULT": 0},
# Fixed enthalpy 1317 41318 Float 2 0.0< to 99999.9 1000.0 Enthalpy unit
{"ADDR": 1318, "TYPE": "float", "RANGE": [0.0, 99999.9], "DEFAULT": 1000.0},
# Set Clock Date 1700 41701 Date 2 0x00010100 to 0x001F0CFF (1900/01/01 to 2155/12/31) 0x0001017B (2023/01/01) -
{"ADDR": 1701, "TYPE": "date", "RANGE": [0x00010100, 0x001F0CFF], "DEFAULT": 0x0001017B},
# Set Clock Time 1702 41703 Time 2 0x00000000 to 0xA4CB7FFF (00:00:00 to 23:59:59) 0x00000000 (00:00:00) -
{"ADDR": 1703, "TYPE": "time", "RANGE": [0x00000000, 0xA4CB7FFF], "DEFAULT": 0x00000000},
# Model 1800 41801 ASCII 8 - "VY Series " - 
{"ADDR": 1801, "TYPE": "ascii", "LENGTH": 8, "DEFAULT": "VY Series"},
# Tag 1808 41809 ASCII 4 - " " - 
{"ADDR": 1809, "TYPE": "ascii", "LENGTH": 4, "DEFAULT": " "},
# Long tag 1812 41813 ASCII 16 - " " - 
{"ADDR": 1813, "TYPE": "ascii", "LENGTH": 16, "DEFAULT": " "},
# Device revision 1828 41829 ASCII 8 - " " - 
{"ADDR": 1829, "TYPE": "ascii", "LENGTH": 8, "DEFAULT": " "},
# Memo 1 1836 41837 ASCII 8 - " " - 
{"ADDR": 1837, "TYPE": "ascii", "LENGTH": 8, "DEFAULT": " "},
# Memo 2 1844 41845 ASCII 8 - " " - 
{"ADDR": 1845, "TYPE": "ascii", "LENGTH": 8, "DEFAULT": " "},
# Memo 3 1852 41853 ASCII 8 - " " - 
{"ADDR": 1853, "TYPE": "ascii", "LENGTH": 8, "DEFAULT": " "},
# Transmitter S/N 1861 41862 ASCII 8 - " " - 
{"ADDR": 1862, "TYPE": "ascii", "LENGTH": 8, "DEFAULT": " "},
# Hardware revision 1869 41870 ASCII 8 - "S1.01 " - 
{"ADDR": 1870, "TYPE": "ascii", "LENGTH": 8, "DEFAULT": "S1.01"},
# Release date 1877 41878 Date 2 0x00010100 to 0x001F0CFF (1900/01/01 to 2155/12/31) 0x0001017B (2023/01/01) - 
{"ADDR": 1878, "TYPE": "date", "RANGE": [0x00010100, 0x001F0CFF], "DEFAULT": 0x0001017B},
# Distributor name 1879 41880 ASCII 8 - "YOKOGAWA " - 
{"ADDR": 1880, "TYPE": "ascii", "LENGTH": 8, "DEFAULT": "YOKOGAWA"},
# Sensor MS code 1 2400 42401 ASCII 8 - " " - 
{"ADDR": 2401, "TYPE": "ascii", "LENGTH": 8, "DEFAULT": " "},
# Sensor MS code 2 2408 42409 ASCII 8 - " " - 
{"ADDR": 2409, "TYPE": "ascii", "LENGTH": 8, "DEFAULT": " "},
# Sensor MS code 3 2416 42417 ASCII 8 - " " - 
{"ADDR": 2417, "TYPE": "ascii", "LENGTH": 8, "DEFAULT": " "},
# Sensor MS code 4 2424 42425 ASCII 8 - " " - 
{"ADDR": 2425, "TYPE": "ascii", "LENGTH": 8, "DEFAULT": " "},
# Sensor MS code 5 2432 42433 ASCII 8 - " " - 
{"ADDR": 2433, "TYPE": "ascii", "LENGTH": 8, "DEFAULT": " "},
# Sensor MS code 6 2440 42441 ASCII 8 - " " - 
{"ADDR": 2441, "TYPE": "ascii", "LENGTH": 8, "DEFAULT": " "},
# Sensor style code 2448 42449 ASCII 8 - " " - 
{"ADDR": 2449, "TYPE": "ascii", "LENGTH": 8, "DEFAULT": " "},
# Transmitter MS code 1 2600 42601 ASCII 8 - " " - 
{"ADDR": 2601, "TYPE": "ascii", "LENGTH": 8, "DEFAULT": " "},
# Transmitter MS code 2 2608 42609 ASCII 8 - " " - 
{"ADDR": 2609, "TYPE": "ascii", "LENGTH": 8, "DEFAULT": " "},
# Transmitter MS code 3 2616 42617 ASCII 8 - " " - 
{"ADDR": 2617, "TYPE": "ascii", "LENGTH": 8, "DEFAULT": " "},
# Transmitter MS code 4 2624 42625 ASCII 8 - " " - 
{"ADDR": 2625, "TYPE": "ascii", "LENGTH": 8, "DEFAULT": " "},
# Transmitter MS code 5 2632 42633 ASCII 8 - " " - 
{"ADDR": 2633, "TYPE": "ascii", "LENGTH": 8, "DEFAULT": " "},
# Transmitter MS code 6 2640 42641 ASCII 8 - " " - 
{"ADDR": 2641, "TYPE": "ascii", "LENGTH": 8, "DEFAULT": " "},
# Transmitter style code 2648 42649 ASCII 8 - " " - 
{"ADDR": 2649, "TYPE": "ascii", "LENGTH": 8, "DEFAULT": " "},
# Special order number 1 2800 42801 ASCII 8 - " " - 
{"ADDR": 2801, "TYPE": "ascii", "LENGTH": 8, "DEFAULT": " "},
# Special order number 2 2808 42809 ASCII 8 - " " - 
{"ADDR": 2809, "TYPE": "ascii", "LENGTH": 8, "DEFAULT": " "},
# Sizing number 2816 42817 ASCII 8 - " " - 
{"ADDR": 2817, "TYPE": "ascii", "LENGTH": 8, "DEFAULT": " "},
# Name plate tag number 2824 42825 ASCII 8 - " " - 
{"ADDR": 2825, "TYPE": "ascii", "LENGTH": 8, "DEFAULT": " "},
# Instruction manual number 2832 42833 ASCII 8 - " " - 
{"ADDR": 2833, "TYPE": "ascii", "LENGTH": 8, "DEFAULT": " "},
# Communication select 2840 42841 Uint8 1 4:Modbus 4:Modbus -
{"ADDR": 2841, "TYPE": "uint8", "RANGE": [1, 4], "DEFAULT": 4},
# Option built-in temperature 2841 42842 Uint8 1 0:Off 1:On 0:Off - 
{"ADDR": 2842, "TYPE": "uint8", "RANGE": [0, 1], "DEFAULT": 0},
# Option display installation 2843 42844 Uint8 1 0:Off 1:On 0:Off - 
{"ADDR": 2844, "TYPE": "uint8", "RANGE": [0, 1], "DEFAULT": 0},
# Option cryogenic 2845 42846 Uint8 1 0:Off 1:On 0:Off - 
{"ADDR": 2846, "TYPE": "uint8", "RANGE": [0, 1], "DEFAULT": 0},
# Option built-in verification 2846 42847 Uint8 1 0:Off 1:On 1:On - 
{"ADDR": 2847, "TYPE": "uint8", "RANGE": [0, 1], "DEFAULT": 1},
# Prediction function 2847 42848 Uint8 1 0:Off 1:On 1:On -
{"ADDR": 2848, "TYPE": "uint8", "RANGE": [0, 1], "DEFAULT": 1},
# Option SI unit 2848 42849 Uint8 1 0:All 1:JP only 0:All - 
{"ADDR": 2849, "TYPE": "uint8", "RANGE": [0, 1], "DEFAULT": 0},
# Key code 3000 43001 Uint16 1 0 to 50000 0 - 
{"ADDR": 3001, "TYPE": "uint16", "RANGE": [0, 50000], "DEFAULT": 0},
# New password 3001 43002 ASCII 4 - " " - 
{"ADDR": 3002, "TYPE": "ascii", "LENGTH": 4, "DEFAULT": " "},
# Enable write 10 min 3005 43006 ASCII 4 - " " - 
{"ADDR": 3006, "TYPE": "ascii", "LENGTH": 4, "DEFAULT": " "},
# Change user role 3009 43010 Uint16 1 0 to 9999 0 -
{"ADDR": 3010, "TYPE": "uint16", "RANGE": [0, 9999], "DEFAULT": 0},
# Maintenance PIN 3010 43011 Uint16 1 0 to 9999 0 - 
{"ADDR": 3011, "TYPE": "uint16", "RANGE": [0, 9999], "DEFAULT": 0},
# Specialist PIN 3011 43012 Uint16 1 0 to 9999 0 - 
{"ADDR": 3012, "TYPE": "uint16", "RANGE": [0, 9999], "DEFAULT": 0},
# Reset PIN code 3012 43013 Uint16 1 0 to 9999 0 - 
{"ADDR": 3013, "TYPE": "uint16", "RANGE": [0, 9999], "DEFAULT": 0},
# Alarm status select 3200 43201 Uint8 1 0:All alarm/warning 1:All alarm 2:System/Process alarm 0:All alarm/warning - 
{"ADDR": 3201, "TYPE": "uint8", "REGISTERS": ["Allalarm/warning", "All alarm", "System/Process alarm"], "DEFAULT": 0},
# Alarm record select 3400 43401 Uint8 1 0:All alarm/warning 1:All alarm 2:System/Process alarm 0:All alarm/warning - 
{"ADDR": 3401, "TYPE": "uint8", "REGISTERS": ["Allalarm/warning", "All alarm", "System/Process alarm"], "DEFAULT": 0},
# Alarm record clear 3401 43402 Uint8 1 0:Not execute 1:Execute 0:Not execute - 
{"ADDR": 3402, "TYPE": "uint8", "REGISTERS": ["Not execute", "Execute"], "DEFAULT": 0},
# Auto delete time 3402 43403 Uint16 1 0 to 9999 60 day 
{"ADDR": 3403, "TYPE": "uint16", "RANGE": [0, 9999], "DEFAULT": 60},
# Flow sensor alarm action 3600 43601 Uint8 1 1:Hold 2:Zero 3:Measured value 2:Zero - 
{"ADDR": 3601, "TYPE": "uint8", "REGISTERS": ["Hold", "Zero", "Measured value"], "DEFAULT": 2},
# Temperature sensor alarm action 3601 43602 Uint8 1 1:Hold 2:Zero 3:Fixed value 2:Zero - 
{"ADDR": 3602, "TYPE": "uint8", "REGISTERS": ["Hold", "Zero", "Fixed value"], "DEFAULT": 2},
# Fluctuating level 3603 43604 Float 2 0.0 to 100.0 10.0 % 
{"ADDR": 3604, "TYPE": "float", "RANGE": [0.0, 100.0], "DEFAULT": 10.0},
# Transient noise count 3605 43606 Uint8 1 0 to 99 12 - 
{"ADDR": 3606, "TYPE": "uint8", "RANGE": [0, 99], "DEFAULT": 12},
# High vibration action 3606 43607 Uint8 1 0:Zero 1:Hold 2:Measured value 2:Measured value - 
{"ADDR": 3607, "TYPE": "uint8", "REGISTERS": ["Zero", "Hold", "Measured value"], "DEFAULT": 2},
# High vibration time 3607 43608 Uint8 1 0 to 99 10 s 
{"ADDR": 3608, "TYPE": "uint8", "RANGE": [0, 99], "DEFAULT": 10},
# Critical vibration action 3608 43609 Uint8 1 0:Zero 1:Hold 2:Measured value 1:Hold - 
{"ADDR": 3609, "TYPE": "uint8", "REGISTERS": ["Zero", "Hold", "Measured value"], "DEFAULT": 1},
# Critical vibration level 3609 43610 Float 2 0.0 to 100.0 5.0 % 
{"ADDR": 3610, "TYPE": "float", "RANGE": [0.0, 100.0], "DEFAULT": 5.0},
# Critical vibration time 3611 43612 Uint8 1 0 to 99 5 s 
{"ADDR": 3612, "TYPE": "uint8", "RANGE": [0, 99], "DEFAULT": 5},
# Clogging time 3612 43613 Uint8 1 0 to 99 30 s 
{"ADDR": 3613, "TYPE": "uint8", "RANGE": [0, 99], "DEFAULT": 30},
# Sensor circuit threshold 3613 43614 Uint16 1 0 to 65535 150 - 
{"ADDR": 3614, "TYPE": "uint16", "RANGE": [0, 65535], "DEFAULT": 150},
# Sensor capacitance threshold 3614 43615 Float 2 0.0 to 99999.9 33.0 pF 
{"ADDR": 3615, "TYPE": "float", "RANGE": [0.0, 99999.9], "DEFAULT": 33.0},
# Sensor resistance threshold 3616 43617 Float 2 0.0 to 99999.9 50.0 kohm 
{"ADDR": 3617, "TYPE": "float", "RANGE": [0.0, 99999.9], "DEFAULT": 50.0},
# Verification Exe 3800 43801 Uint8 1 0:Not execute 1:Execute 0:Not execute - 
{"ADDR": 3801, "TYPE": "uint8", "REGISTERS": ["Not execute", "Execute"], "DEFAULT": 0},
# Verification target 3802 43803 Uint8 1 0x0001:Sensor circuit 0x0002:Signal processing circuit 0x0004:Calculation circuit 0x0008:Alarm status 0x0010:Alarm record b0~b4:on - 
{"ADDR": 3803, "TYPE": "uint8", "REGISTERS": ["Sensor circuit", "Signal processing circuit", "Calculation circuit", "Alarm status", "Alarm record"], "DEFAULT": 0},
# Verification select 3803 43804 Uint8 1 0:Latest 1:Previous 2:Factoty 0:Latest - 
{"ADDR": 3804, "TYPE": "uint8", "REGISTERS": ["Latest", "Previous", "Factory"], "DEFAULT": 0},
# Prediction execution 4000 44001 Uint8 1 0:Not execute 1:Execute 0:Not execute - 
{"ADDR": 4001, "TYPE": "uint8", "REGISTERS": ["Not execute", "Execute"], "DEFAULT": 0},
# Prediction select 4001 44002 Uint8 1 0:A/B ratio 1:Sensor sensitivity 2:Signal A 3:Signal B 4:Signal C 0:A/B ratio - 
{"ADDR": 4002, "TYPE": "uint8", "REGISTERS": ["A/B ratio", "Sensor sensitivity", "Signal A", "Signal B", "Signal C"], "DEFAULT": 0},
# Prediction period 4002 44003 Uint16 1 1 to 65535 60 min 
{"ADDR": 4003, "TYPE": "uint16", "RANGE": [1, 65535], "DEFAULT": 60},
# Prediction level 4003 44004 Float 2 0.0 to 99999.9 0.0 - 
{"ADDR": 4004, "TYPE": "float", "RANGE": [0.0, 99999.9], "DEFAULT": 0.0},
# Prediction alarm time 4005 44006 Uint16 1 0 to 65535 0 h 
{"ADDR": 4006, "TYPE": "uint16", "RANGE": [0, 65535], "DEFAULT": 0},
# Prediction type 4006 44007 Uint8 1 0:Type 1 1:Type 2 2:Type 3 0:Type 1 - 
{"ADDR": 4007, "TYPE": "uint8", "REGISTERS": ["Type 1", "Type 2", "Type 3"], "DEFAULT": 0},
# Signal latch execution 5500 45501 Uint8 1 0:Not execute 1:Execute 0:Not execute - 
{"ADDR": 5501, "TYPE": "uint8", "REGISTERS": ["Not execute", "Execute"], "DEFAULT": 0},
# Signal latch target 5501 45502 Uint8 1 0:Latest 1:Sensor alarm record 1 2:Sensor alarm record 2 3:Sensor alarm record 3 4:Sensor alarm record 4 5:Sensor alarm record 5 0:Latest - 
{"ADDR": 5502, "TYPE": "uint8", "REGISTERS": ["Latest", "Sensor alarm record 1", "Sensor alarm record 2", "Sensor alarm record 3", "Sensor alarm record 4", "Sensor alarm record 5"], "DEFAULT": 0},
# Test mode 6000 46001 Uint8 1 0x0002:Pulse output 0x0004:Status output b0~b7:off - 
{"ADDR": 6001, "TYPE": "uint8", "REGISTERS": ["Pulse output", "Status output"], "DEFAULT": 0},
# Test pulse output 6001 46002 Float 2 0.0 to 10000.0 0.0 Hz
{"ADDR": 6002, "TYPE": "float", "RANGE": [0.0, 10000.0], "DEFAULT": 0.0},
# Test status output 6003 46004 Uint8 1 0:Off(Open) 1:On(Close) 0:Off(Open) - 
{"ADDR": 6004, "TYPE": "uint8", "REGISTERS": ["Off(Open)", "On(Close)"], "DEFAULT": 0},
# Simulation mode 6004 46005 Uint8 1 0x0001:Vortex frequency 0x0002:Vortex frequency(HW) 0x0004:Built-in temperature b0~b7:off - 
{"ADDR": 6005, "TYPE": "uint8", "REGISTERS": ["Vortex frequency", "Vortex frequency(HW)", "Built-in temperature"], "DEFAULT": 0},
# Simulation vortex frequency 6005 46006 Float 2 0.0 to 10000.0 0.0 Hz 
{"ADDR": 6006, "TYPE": "float", "RANGE": [0.0, 10000.0], "DEFAULT": 0.0},
# Simulation vortex frequency(HW) 6007 46008 Float 2 0.0 to 10000.0 0.0 Hz
{"ADDR": 6008, "TYPE": "float", "RANGE": [0.0, 10000.0], "DEFAULT": 0.0},
# Simulation built-in temperature 6009 46010 Float 2 -999.9 to 999.9 0.0 Temperature unit 
{"ADDR": 6010, "TYPE": "float", "RANGE": [-999.9, 999.9], "DEFAULT": 0.0},
# Device variable simulation mode 6013 46014 Uint8 1 0x0001:Flow rate 0x0002:Temperature 0x0004:Pressure b0~b7:off - 
{"ADDR": 6014, "TYPE": "uint8", "REGISTERS": ["Flow rate", "Temperature", "Pressure"], "DEFAULT": 0},
# Simulation flow rate 6014 46015 Float 2 0.0 to 99999.9 0.0 Flow unit 
{"ADDR": 6015, "TYPE": "float", "RANGE": [0.0, 99999.9], "DEFAULT": 0.0},
# Simulation temperature 6016 46017 Float 2 -999.9 to 999.9 0.0 Temperature unit 
{"ADDR": 6017, "TYPE": "float", "RANGE": [-999.9, 999.9], "DEFAULT": 0.0},
# Simulation pressure 6018 46019 Float 2 0.0 to 99999.9 0.0 Pressure unit 
{"ADDR": 6019, "TYPE": "float", "RANGE": [0.0, 99999.9], "DEFAULT": 0.0},
# Auto release time 6020 46021 Uint8 1 0:10min 1:30min 2:60min 3:3h 4:6h 5:12h 1:30min - 
{"ADDR": 6021, "TYPE": "uint8", "REGISTERS": ["10min", "30min", "60min", "3h", "6h", "12h"], "DEFAULT": 0},
# Display test 6021 46022 Uint8 1 0:Not execute 1:Execute 2:All on 3:All off 4:Only numeric 5:Only unit 6:Only icon 0:Not execute - 
{"ADDR": 6022, "TYPE": "uint8", "REGISTERS": ["Not execute", "Execute", "All on", "All off", "Only numeric", "Only unit", "Only icon"], "DEFAULT": 0},
# Squawk 6022 46023 Uint8 1 0:Off 1:On 2:Once 0:Off - 
{"ADDR": 6023, "TYPE": "uint8", "REGISTERS": ["Off", "On", "Once"], "DEFAULT": 0},
# Device reset 6024 46025 Uint8 1 0:Not execute 1:Execute 0:Not execute - 
{"ADDR": 6025, "TYPE": "uint8", "REGISTERS": ["Not execute", "Execute"], "DEFAULT": 0},
# Sensor reset 6026 46027 Uint8 1 0:Not execute 1:Execute 0:Not execute - 
{"ADDR": 6027, "TYPE": "uint8", "REGISTERS": ["Not execute", "Execute"], "DEFAULT": 0},
# Flow rate gain 6200 46201 Float 2 0.0< to 99999.9 1.0 - 
{"ADDR": 6201, "TYPE": "float", "RANGE": [0.0, 99999.9], "DEFAULT": 1.0},
# Instrument error adjust 6202 46203 Uint8 1 0:Off 1:On 0:Off - 
{"ADDR": 6203, "TYPE": "uint8", "REGISTERS": ["Off", "On"], "DEFAULT": 0},
# Adjust vortex frequency 1 6203 46204 Float 2 0.0 to 10000.0 0.0 Hz 
{"ADDR": 6204, "TYPE": "float", "RANGE": [0.0, 10000.0], "DEFAULT": 0.0},
# Adjust value 1 6205 46206 Float 2 -50.00 to 50.00 0.0 % 
{"ADDR": 6206, "TYPE": "float", "RANGE": [-50.0, 50.0], "DEFAULT": 0.0},
# Adjust vortex frequency 2 6207 46208 Float 2 0.0 to 10000.0 0.0 Hz 
{"ADDR": 6208, "TYPE": "float", "RANGE": [0.0, 10000.0], "DEFAULT": 0.0},
# Adjust value 2 6209 46210 Float 2 -50.00 to 50.00 0.0 % 
{"ADDR": 6210, "TYPE": "float", "RANGE": [-50.0, 50.0], "DEFAULT": 0.0},
# Adjust vortex frequency 3 6211 46212 Float 2 0.0 to 10000.0 0.0 Hz 
{"ADDR": 6212, "TYPE": "float", "RANGE": [0.0, 10000.0], "DEFAULT": 0.0},
# Adjust value 3 6213 46214 Float 2 -50.00 to 50.00 0.0 % 
{"ADDR": 6214, "TYPE": "float", "RANGE": [-50.0, 50.0], "DEFAULT": 0.0},
# Adjust vortex frequency 4 6215 46216 Float 2 0.0 to 10000.0 0.0 Hz 
{"ADDR": 6216, "TYPE": "float", "RANGE": [0.0, 10000.0], "DEFAULT": 0.0},
# Adjust value 4 6217 46218 Float 2 -50.00 to 50.00 0.0 % 
{"ADDR": 6218, "TYPE": "float", "RANGE": [-50.0, 50.0], "DEFAULT": 0.0},
# Adjust vortex frequency 5 6219 46220 Float 2 0.0 to 10000.0 0.0 Hz 
{"ADDR": 6220, "TYPE": "float", "RANGE": [0.0, 10000.0], "DEFAULT": 0.0},
# Adjust value 5 6221 46222 Float 2 -50.00 to 50.00 0.0 % 
{"ADDR": 6222, "TYPE": "float", "RANGE": [-50.0, 50.0], "DEFAULT": 0.0},
# Reynolds adjust 6223 46224 Uint8 1 0:Off 1:On 0:Off - 
{"ADDR": 6224, "TYPE": "uint8", "REGISTERS": ["Off", "On"], "DEFAULT": 0},
# Viscosity unit 6224 46225 Uint8 1 0:mPa•s 1:Pa•s 2:cP 3:P 4:m2/s 5:cSt 6:St 0:mPa•s - 
{"ADDR": 6225, "TYPE": "uint8", "REGISTERS": ["mPa•s", "Pa•s", "cP", "P", "m2/s", "cSt", "St"], "DEFAULT": 0},
# Viscosity 6225 46226 Float 2 0.0< to 99999.9 1.0 Viscosity unit 
{"ADDR": 6226, "TYPE": "float", "RANGE": [0.0, 99999.9], "DEFAULT": 1.0},
# Adjust reynolds number 1 6227 46228 Float 2 0.0 to 99999.9 5500.0 - 
{"ADDR": 6228, "TYPE": "float", "RANGE": [0.0, 99999.9], "DEFAULT": 5500.0},
# Re adjust value 1 6229 46230 Float 2 -50.0 to 50.0 -11.4 % 
{"ADDR": 6230, "TYPE": "float", "RANGE": [-50.0, 50.0], "DEFAULT": -11.4},
# Adjust reynolds number 2 6231 46232 Float 2 0.0 to 99999.9 8000.0 - 
{"ADDR": 6232, "TYPE": "float", "RANGE": [0.0, 99999.9], "DEFAULT": 8000.0},
# Re adjust value 2 6233 46234 Float 2 -50.0 to 50.0 -6.5 % 
{"ADDR": 6234, "TYPE": "float", "RANGE": [-50.0, 50.0], "DEFAULT": -6.5},
# Adjust reynolds number 3 6235 46236 Float 2 0.0 to 99999.9 12000.0 - 
{"ADDR": 6236, "TYPE": "float", "RANGE": [0.0, 99999.9], "DEFAULT": 12000.0},
# Re adjust value 3 6237 46238 Float 2 -50.0 to 50.0 -3.6 %
{"ADDR": 6238, "TYPE": "float", "RANGE": [-50.0, 50.0], "DEFAULT": -3.6},
# Adjust reynolds number 4 6239 46240 Float 2 0.0 to 99999.9 20000.0 -
{"ADDR": 6240, "TYPE": "float", "RANGE": [0.0, 99999.9], "DEFAULT": 20000.0},
# Re adjust value 4 6241 46242 Float 2 -50.0 to 50.0 -1.0 % 
{"ADDR": 6242, "TYPE": "float", "RANGE": [-50.0, 50.0], "DEFAULT": -1.0},
# Adjust reynolds number 5 6243 46244 Float 2 0.0 to 99999.9 40000.0 -
{"ADDR": 6244, "TYPE": "float", "RANGE": [0.0, 99999.9], "DEFAULT": 000.0},
# Re adjust value 5 6245 46246 Float 2 -50.0 to 50.0 0.0 % 
{"ADDR": 6246, "TYPE": "float", "RANGE": [-50.0, 50.0], "DEFAULT": 0.0},
# Expansion factor adjust 6247 46248 Uint8 1 0:Off 1:On 0:Off - 
{"ADDR": 6248, "TYPE": "uint8", "REGISTERS": ["Off", "On"], "DEFAULT": 0},
# Signal level 6400 46401 Float 2 0.1 to 20.0 1.0 - 
{"ADDR": 6401, "TYPE": "float", "RANGE": [0.1, 20.0], "DEFAULT": 1.0},
# Trigger level mode 6402 46403 Uint8 1 0:Fix 1:Tracking 1:Tracking - 
{"ADDR": 6403, "TYPE": "uint8", "REGISTERS": ["Fix", "Tracking"], "DEFAULT": 1},
# Trigger level(TLA) 6403 46404 Float 2 0.1 to 20.0 1.0 - 
{"ADDR": 6404, "TYPE": "float", "RANGE": [0.1, 20.0], "DEFAULT": 1.0},
# Noise balance mode 6405 46406 Uint8 1 0:Auto 1:Manual 0:Auto - 
{"ADDR": 6406, "TYPE": "uint8", "REGISTERS": ["Auto", "Manual"], "DEFAULT": 0},
# Noise ratio(manual) 6406 46407 Float 2 -2.0 to 2.0 0.0 - 
{"ADDR": 6407, "TYPE": "float", "RANGE": [-2.0, 2.0], "DEFAULT": 0.0},
# Tuning at zero 6409 46410 Uint8 1 0:Not execute 1:Execute 0:Not execute -
{"ADDR": 6410, "TYPE": "uint8", "REGISTERS": ["Not execute", "Execute"], "DEFAULT": 0},
]


# https://eldis24.ru/upload/iblock/424/j1ksqyqlj5k643iiqqfcbyc8nc9sd0ze/WB-MAP3E_Modbus_Power_Meter.pdf
holding_registers_power_meter = [
# 110 0x006E Holding RW u16 Скорость порта RS-485. Настройка параметров подключения по RS-485 x100, Боды 12 — 1200 бит/с, 24 — 2400 бит/с, 48 — 4800 бит/с, 96 — 9600 бит/с, 192 — 19 200 бит/с, 384 — 38 400 бит/с, 576 — 57 600 бит/с, 1152 — 115 200 Кбит/с 
{"ADDR": 110, "TYPE": "uint16", "RANGE": [12, 24, 48, 96, 192, 384, 576, 1152], "DEFAULT": 96},
# 111 0x006F Holding RW u16 Настройка бита чётности порта RS-485 0 — нет бита чётности (none), 1 — нечётный (odd), 2 — чётный (even)
{"ADDR": 111, "TYPE": "uint8", "REGISTERS": ["none", "odd", "even"], "DEFAULT": 0},
# 112 0x0070 Holding RW u16 Количество стоп-битов порта RS-485 1, 2 
{"ADDR": 112, "TYPE": "uint8", "RANGE": [1, 2], "DEFAULT": 2},
# 120 0x0078 Holding RW u16 Сохранение состояния при перезагрузке устройства 0 - сохраняет, >0 - без сохранения
{"ADDR": 120, "TYPE": "uint8", "REGISTERS": ["save", "no save"], "DEFAULT": 0},
# 128 0x0080 Holding RW u16 Modbus-адрес устройства (подробнее) 
{"ADDR": 128, "TYPE": "uint16", "RANGE": [1, 255], "DEFAULT": 1},
# 129 0x0081 Holding RW u16 Перевод в режим обновления прошивки на 2 минуты 0 - выключен, >0 - включен 
{"ADDR": 129, "TYPE": "uint8", "REGISTERS": ["off", "on"], "DEFAULT": 0},
# 290- 301 0x0122 - 0x012D Holding RO string Сигнатура прошивки 
{"ADDR": 290, "TYPE": "string", "LENGTH": 16, "DEFAULT":""},
# 330- 336 0x014A - 0x0150 Holding RO string Версия загрузчика
{"ADDR": 330, "TYPE": "string", "LENGTH": 8, "DEFAULT":""},
# 0x0F0 Holding RW u16 Период таймера сброса пиковых значений (в секундах) для канала X Для WB-MAP3E, WB-MAP12E с 60 до версии 2.3.0 
{"ADDR": 240, "TYPE": "uint16", "RANGE": [60, 65535], "DEFAULT": 60},
# 0xX460 Holding RW u16 Коэффициент трансформации для токового трансформатора на фазе L1 (A) канала X 0 2.1 
{"ADDR": 1120, "TYPE": "uint16", "RANGE": [0, 65535], "DEFAULT": 0},
# 0xX461 Holding RW u16 Коэффициент трансформации для токового трансформатора на фазе L2 (B) канала X 0 2.1 
{"ADDR": 1121, "TYPE": "uint16", "RANGE": [0, 65535], "DEFAULT": 0},
# 0xX462 Holding RW u16 Коэффициент трансформации для токового трансформатора на фазе L3 (C) канала X 0 2.1 
{"ADDR": 1122, "TYPE": "uint16", "RANGE": [0, 65535], "DEFAULT": 0},
# 0xX463 Holding RW s16 Фазовая задержка токового трансформатора на фазе L1 (A) канала X x, ° -32768 - 32767 (0) 2.1 
{"ADDR": 1123, "TYPE": "int16", "RANGE": [-32768, 32767], "DEFAULT": 0},
# 0xX464 Holding RW s16 Фазовая задержка токового трансформатора на фазе L2 (B) канала X x, ° -32768 - 32767 (0) 2.1 
{"ADDR": 1124, "TYPE": "int16", "RANGE": [-32768, 32767], "DEFAULT": 0},
# 0xX465 Holding RW s16 Фазовая задержка токового трансформатора на фазе L3 (C) канала X x, ° -32768 - 32767 (0) 2.1 
{"ADDR": 1125, "TYPE": "int16", "RANGE": [-32768, 32767], "DEFAULT": 0},
# 0x4A0 Holding RW u16 Фаза токового трансформатора подключенного ко входу CT1 канала X 1 - L1(A), 2 - L2(B), 3 - L3(C) Для WB-MAP3E, WB-MAP12E 2 2.3.2 
{"ADDR": 1184, "TYPE": "uint8", "RANGE": [1, 3], "DEFAULT": 2},
# 0xX4A1 Holding RW u16 Фаза токового трансформатора подключенного ко входу CT2 канала X 1 - L1(A), 2 - L2(B), 3 - L3(C) Для WB-MAP3E, WB-MAP12E 2 2.3.2 
{"ADDR": 1185, "TYPE": "uint8", "RANGE": [1, 3], "DEFAULT": 2},
# 0xX4A2 Holding RW u16 Фаза токового трансформатора подключенного ко входу CT3 канала X 1 - L1(A), 2 - L2(B), 3 - L3(C) Для WB-MAP3E, WB-MAP12E 2 2.3.2
{"ADDR": 1186, "TYPE": "uint8", "RANGE": [1, 3], "DEFAULT": 2},
]




input_registers_power_meter = [
    # Current baud rate 0 30001 Uint8 1 0:1200 bps 1:2400 bps 2:4800 bps 3:9600 bps 4:19200 bps 4:19200 bps - 
    {"ADDR": 1, "TYPE": "uint8", "REGISTERS": ["1200 bps", "2400 bps", "4800 bps", "9600 bps", "19200 bps"], "DEFAULT": 4},
    # Current parity 1 30002 Uint8 1 0:None 1:Odd 2:Even 2:Even -
    {"ADDR": 2, "TYPE": "uint8", "REGISTERS": ["None", "Odd", "Even"], "DEFAULT": 2},

]




input_registers_water_meter = [
# Current baud rate 0 30001 Uint8 1 0:1200 bps 1:2400 bps 2:4800 bps 3:9600 bps 4:19200 bps 4:19200 bps - 
{"ADDR": 1, "TYPE": "uint8", "REGISTERS": ["1200 bps", "2400 bps", "4800 bps", "9600 bps", "19200 bps"], "DEFAULT": 4},
# Current parity 1 30002 Uint8 1 0:None 1:Odd 2:Even 2:Even -
{"ADDR": 2, "TYPE": "uint8", "REGISTERS": ["None", "Odd", "Even"], "DEFAULT": 2},
# Current stop bit 2 30003 Uint8 1 0:1 bit 1:2 bits 0:1 bit -
{"ADDR": 3, "TYPE": "uint8", "REGISTERS": ["1 bit", "2 bits"], "DEFAULT": 0},
# Current response delay time 3 30004 Uint8 1 10 to 200 10 ms
{"ADDR": 4, "TYPE": "uint8", "RANGE": [10, 200], "DEFAULT": 10},
# Current slave address 4 30005 Uint8 1 1 to 247 1 -
{"ADDR": 5, "TYPE": "uint8", "RANGE": [1, 247], "DEFAULT": 1},
# Current data format 4byte 5 30006 Uint8 1 0:ABCD 1:CDAB 2:BADC 3:DCBA 0:ABCD -
{"ADDR": 6, "TYPE": "uint8", "REGISTERS": ["ABCD", "CDAB", "BADC", "DCBA"], "DEFAULT": 0},
# Current data format float 6 30007 Uint8 1 0:ABCD 1:CDAB 2:BADC 3:DCBA 0:ABCD -
{"ADDR": 7, "TYPE": "uint8", "REGISTERS": ["ABCD", "CDAB", "BADC", "DCBA"], "DEFAULT": 0},
# Current data format 2byte 7 30008 Uint8 1 0:AB 1:BA 0:AB -
{"ADDR": 8, "TYPE": "uint8", "REGISTERS": ["AB", "BA"], "DEFAULT": 0},
# Current data format string 8 30009 Uint8 1 0:AB 1:BA 0:AB -
{"ADDR": 9, "TYPE": "uint8", "REGISTERS": ["AB", "BA"], "DEFAULT": 0},
# Flow rate(%) data quality-limit status 300 30301 Uint8 1 0x00F0:Good-Constant 0x00E0:Good-High limited 0x00D0:Good-Low limited 0x00C0:Good-Not limited 0x00B0:Manual / Fixed-Constant 0x00A0:Manual / Fixed-High limited 0x0090:Manual / Fixed-Low limited 0x0080:Manual / Fixed-Not limited 0x0070:Poor accuracy-Constant 0x0060:Poor accuracy-High limited 0x0050:Poor accuracy-Low limited 0x0040:Poor accuracy-Not limited 0x0030:Bad-Constant 0x0020:Bad-High limited 0x0010:Bad-Low limited 0x0000:Bad-Not limited b0~b7:off - 
{"ADDR": 300, "TYPE": "uint8", "REGISTERS": ["Good-Constant", "Good-High limited", "Good-Low limited", "Good-Not limited", "Manual / Fixed-Constant", "Manual / Fixed-High limited", "Manual / Fixed-Low limited", "Manual / Fixed-Not limited", "Poor accuracy-Constant", "Poor accuracy-High limited", "Poor accuracy-Low limited", "Poor accuracy-Not limited", "Bad-Constant", "Bad-High limited", "Bad-Low limited", "Bad-Not limited"], "DEFAULT": 0},
# Flow rate data qualitylimit status 301 30302 Uint8 1 0x00F0:Good-Constant 0x00E0:Good-High limited 0x00D0:Good-Low limited 0x00C0:Good-Not limited 0x00B0:Manual / Fixed-Constant 0x00A0:Manual / Fixed-High limited 0x0090:Manual / Fixed-Low limited 0x0080:Manual / Fixed-Not limited 0x0070:Poor accuracy-Constant 0x0060:Poor accuracy-High limited 0x0050:Poor accuracy-Low limited 0x0040:Poor accuracy-Not limited 0x0030:Bad-Constant 0x0020:Bad-High limited 0x0010:Bad-Low limited 0x0000:Bad-Not limited b0~b7:off -
{"ADDR": 301, "TYPE": "uint8", "REGISTERS": ["Good-Constant", "Good-High limited", "Good-Low limited", "Good-Not limited", "Manual / Fixed-Constant", "Manual / Fixed-High limited", "Manual / Fixed-Low limited", "Manual / Fixed-Not limited", "Poor accuracy-Constant", "Poor accuracy-High limited", "Poor accuracy-Low limited", "Poor accuracy-Not limited", "Bad-Constant", "Bad-High limited", "Bad-Low limited", "Bad-Not limited"], "DEFAULT": 0},
# Temperature(%) data quality-limit status 302 30303 Uint8 1 0x00F0:Good-Constant 0x00E0:Good-High limited 0x00D0:Good-Low limited 0x00C0:Good-Not limited 0x00B0:Manual / Fixed-Constant 0x00A0:Manual / Fixed-High limited 0x0090:Manual / Fixed-Low limited 0x0080:Manual / Fixed-Not limited 0x0070:Poor accuracy-Constant 0x0060:Poor accuracy-High limited 0x0050:Poor accuracy-Low limited 0x0040:Poor accuracy-Not limited 0x0030:Bad-Constant 0x0020:Bad-High limited 0x0010:Bad-Low limited 0x0000:Bad-Not limited b0~b7:off -
{"ADDR": 302, "TYPE": "uint8", "REGISTERS": ["Good-Constant", "Good-High limited", "Good-Low limited", "Good-Not limited", "Manual / Fixed-Constant", "Manual / Fixed-High limited", "Manual / Fixed-Low limited", "Manual / Fixed-Not limited", "Poor accuracy-Constant", "Poor accuracy-High limited", "Poor accuracy-Low limited", "Poor accuracy-Not limited", "Bad-Constant", "Bad-High limited", "Bad-Low limited", "Bad-Not limited"], "DEFAULT": 0},
# Temperature data quality-limit status 303 30304 Uint8 1 0x00F0:Good-Constant 0x00E0:Good-High limited 0x00D0:Good-Low limited 0x00C0:Good-Not limited 0x00B0:Manual / Fixed-Constant 0x00A0:Manual / Fixed-High limited 0x0090:Manual / Fixed-Low limited 0x0080:Manual / Fixed-Not limited 0x0070:Poor accuracy-Constant 0x0060:Poor accuracy-High limited 0x0050:Poor accuracy-Low limited 0x0040:Poor accuracy-Not limited 0x0030:Bad-Constant 0x0020:Bad-High limited 0x0010:Bad-Low limited 0x0000:Bad-Not limited b0~b7:off -
{"ADDR": 303, "TYPE": "uint8", "REGISTERS": ["Good-Constant", "Good-High limited", "Good-Low limited", "Good-Not limited", "Manual / Fixed-Constant", "Manual / Fixed-High limited", "Manual / Fixed-Low limited", "Manual / Fixed-Not limited", "Poor accuracy-Constant", "Poor accuracy-High limited", "Poor accuracy-Low limited", "Poor accuracy-Not limited", "Bad-Constant", "Bad-High limited", "Bad-Low limited", "Bad-Not limited"], "DEFAULT": 0},
# Totalizer data qualitylimit status 306 30307 Uint8 1 0x00F0:Good-Constant 0x00E0:Good-High limited 0x00D0:Good-Low limited 0x00C0:Good-Not limited 0x00B0:Manual / Fixed-Constant 0x00A0:Manual / Fixed-High limited 0x0090:Manual / Fixed-Low limited 0x0080:Manual / Fixed-Not limited 0x0070:Poor accuracy-Constant 0x0060:Poor accuracy-High limited 0x0050:Poor accuracy-Low limited 0x0040:Poor accuracy-Not limited 0x0030:Bad-Constant 0x0020:Bad-High limited 0x0010:Bad-Low limited 0x0000:Bad-Not limited b0~b7:off -
{"ADDR": 306, "TYPE": "uint8", "REGISTERS": ["Good-Constant", "Good-High limited", "Good-Low limited", "Good-Not limited", "Manual / Fixed-Constant", "Manual / Fixed-High limited", "Manual / Fixed-Low limited", "Manual / Fixed-Not limited", "Poor accuracy-Constant", "Poor accuracy-High limited", "Poor accuracy-Low limited", "Poor accuracy-Not limited", "Bad-Constant", "Bad-High limited", "Bad-Low limited", "Bad-Not limited"], "DEFAULT": 0},
# Density data qualitylimit status 307 30308 Uint8 1 0x00F0:Good-Constant 0x00E0:Good-High limited 0x00D0:Good-Low limited 0x00C0:Good-Not limited 0x00B0:Manual / Fixed-Constant 0x00A0:Manual / Fixed-High limited 0x0090:Manual / Fixed-Low limited 0x0080:Manual / Fixed-Not limited 0x0070:Poor accuracy-Constant 0x0060:Poor accuracy-High limited 0x0050:Poor accuracy-Low limited 0x0040:Poor accuracy-Not limited 0x0030:Bad-Constant 0x0020:Bad-High limited 0x0010:Bad-Low limited 0x0000:Bad-Not limited b0~b7:off -
{"ADDR": 307, "TYPE": "uint8", "REGISTERS": ["Good-Constant", "Good-High limited", "Good-Low limited", "Good-Not limited", "Manual / Fixed-Constant", "Manual / Fixed-High limited", "Manual / Fixed-Low limited", "Manual / Fixed-Not limited", "Poor accuracy-Constant", "Poor accuracy-High limited", "Poor accuracy-Low limited", "Poor accuracy-Not limited", "Bad-Constant", "Bad-High limited", "Bad-Low limited", "Bad-Not limited"], "DEFAULT": 0},
# Density ratio data quality-limit status 308 30309 Uint8 1 0x00F0:Good-Constant 0x00E0:Good-High limited 0x00D0:Good-Low limited 0x00C0:Good-Not limited 0x00B0:Manual / Fixed-Constant 0x00A0:Manual / Fixed-High limited 0x0090:Manual / Fixed-Low limited 0x0080:Manual / Fixed-Not limited 0x0070:Poor accuracy-Constant 0x0060:Poor accuracy-High limited 0x0050:Poor accuracy-Low limited 0x0040:Poor accuracy-Not limited 0x0030:Bad-Constant 0x0020:Bad-High limited 0x0010:Bad-Low limited 0x0000:Bad-Not limited b0~b7:off -
{"ADDR": 308, "TYPE": "uint8", "REGISTERS": ["Good-Constant", "Good-High limited", "Good-Low limited", "Good-Not limited", "Manual / Fixed-Constant", "Manual / Fixed-High limited", "Manual / Fixed-Low limited", "Manual / Fixed-Not limited", "Poor accuracy-Constant", "Poor accuracy-High limited", "Poor accuracy-Low limited", "Poor accuracy-Not limited", "Bad-Constant", "Bad-High limited", "Bad-Low limited", "Bad-Not limited"], "DEFAULT": 0},
# Enthalpy data qualitylimit status 309 30310 Uint8 1 0x00F0:Good-Constant 0x00E0:Good-High limited 0x00D0:Good-Low limited 0x00C0:Good-Not limited 0x00B0:Manual / Fixed-Constant 0x00A0:Manual / Fixed-High limited 0x0090:Manual / Fixed-Low limited 0x0080:Manual / Fixed-Not limited 0x0070:Poor accuracy-Constant 0x0060:Poor accuracy-High limited 0x0050:Poor accuracy-Low limited 0x0040:Poor accuracy-Not limited 0x0030:Bad-Constant 0x0020:Bad-High limited 0x0010:Bad-Low limited 0x0000:Bad-Not limited b0~b7:off - 
{"ADDR": 309, "TYPE": "uint8", "REGISTERS": ["Good-Constant", "Good-High limited", "Good-Low limited", "Good-Not limited", "Manual / Fixed-Constant", "Manual / Fixed-High limited", "Manual / Fixed-Low limited", "Manual / Fixed-Not limited", "Poor accuracy-Constant", "Poor accuracy-High limited", "Poor accuracy-Low limited", "Poor accuracy-Not limited", "Bad-Constant", "Bad-High limited", "Bad-Low limited", "Bad-Not limited"], "DEFAULT": 0},
# Vortex frequency data quality-limit status 310 30311 Uint8 1 0x00F0:Good-Constant 0x00E0:Good-High limited 0x00D0:Good-Low limited 0x00C0:Good-Not limited 0x00B0:Manual / Fixed-Constant 0x00A0:Manual / Fixed-High limited 0x0090:Manual / Fixed-Low limited 0x0080:Manual / Fixed-Not limited 0x0070:Poor accuracy-Constant 0x0060:Poor accuracy-High limited 0x0050:Poor accuracy-Low limited 0x0040:Poor accuracy-Not limited 0x0030:Bad-Constant 0x0020:Bad-High limited 0x0010:Bad-Low limited 0x0000:Bad-Not limited b0~b7:off - 
{"ADDR": 310, "TYPE": "uint8", "REGISTERS": ["Good-Constant", "Good-High limited", "Good-Low limited", "Good-Not limited", "Manual / Fixed-Constant", "Manual / Fixed-High limited", "Manual / Fixed-Low limited", "Manual / Fixed-Not limited", "Poor accuracy-Constant", "Poor accuracy-High limited", "Poor accuracy-Low limited", "Poor accuracy-Not limited", "Bad-Constant", "Bad-High limited", "Bad-Low limited", "Bad-Not limited"], "DEFAULT": 0},
# Built-in temperature data quality-limit status 311 30312 Uint8 1 0x00F0:Good-Constant 0x00E0:Good-High limited 0x00D0:Good-Low limited 0x00C0:Good-Not limited 0x00B0:Manual / Fixed-Constant 0x00A0:Manual / Fixed-High limited 0x0090:Manual / Fixed-Low limited 0x0080:Manual / Fixed-Not limited 0x0070:Poor accuracy-Constant 0x0060:Poor accuracy-High limited 0x0050:Poor accuracy-Low limited 0x0040:Poor accuracy-Not limited 0x0030:Bad-Constant 0x0020:Bad-High limited 0x0010:Bad-Low limited 0x0000:Bad-Not limited b0~b7:of
{"ADDR": 311, "TYPE": "uint8", "REGISTERS": ["Good-Constant", "Good-High limited", "Good-Low limited", "Good-Not limited", "Manual / Fixed-Constant", "Manual / Fixed-High limited", "Manual / Fixed-Low limited", "Manual / Fixed-Not limited", "Poor accuracy-Constant", "Poor accuracy-High limited", "Poor accuracy-Low limited", "Poor accuracy-Not limited", "Bad-Constant", "Bad-High limited", "Bad-Low limited", "Bad-Not limited"], "DEFAULT": 0},
# Flow unit 400 30401 Uint8 1 0:m3 /s 1:m3 /min 2:m3 /h 3:m3 /d 4:km3 /s 5:km3 /min 6:km3 /h 7:km3 /d 8:l/s 9:l/min 10:l/h 11:l/d 12:mcf/s 13:mcf/min 14:mcf/h 15:mcf/d 16:cf/s 17:cf/min 18:cf/h 19:cf/d 20:kcf/s 21:kcf/min 22:kcf/h 23:kcf/d 24:USgal/s 25:USgal/min 26:USgal/h 27:USgal/d 28:kUSgal/s 29:kUSgal/min 30:kUSgal/h 31:kUSgal/d 32:UKgal/s 33:UKgal/min 34:UKgal/h 35:UKgal/d 36:kUKgal/s 37:kUKgal/min 38:kUKgal/h 39:kUKgal/d 40:mbbl/s 41:mbbl/min 42:mbbl/h 43:mbbl/d 44:bbl/s 45:bbl/min 46:bbl/h 47:bbl/d 48:kbbl/s 49:kbbl/min 50:kbbl/h 51:kbbl/d 52:kg/s 53:kg/min 54:kg/h 55:kg/d 56:t/s 57:t/min 58:t/h 59:t/d 60:lb/s 61:lb/min 62:lb/h 63:lb/d 64:klb/s 65:klb/min 66:klb/h 67:klb/d 68:(N)m3 /s 69:(N)m3 /min 70:(N)m3 /h 71:(N)m3 /d 72:k(N)m3 /s 73:k(N)m3 /min 74:k(N)m3 /h 75:k(N)m3 /d 76:M(N)m3 /s 77:M(N)m3 /min 78:M(N)m3 /h 79:M(N)m3 /d 80:(N)l/s 81:(N)l/min 82:(N)l/h 83:(N)l/d 84:(S)m3 /s 85:(S)m3 /min 86:(S)m3 /h 87:(S)m3 /d 88:k(S)m3 /s 89:k(S)m3 /min 90:k(S)m3 /h 91:k(S)m3 /d 92:M(S)m3 /s 93:M(S)m3 /min 94:M(S)m3 /h 95:M(S)m3 /d 96:(S)l/s 97:(S)l/min 98:(S)l/h 99:(S)l/d 100:(S)cf/s 101:(S)cf/min 102:(S)cf/h 103:(S)cf/d 104:k(S)cf/s 105:k(S)cf/min 106:k(S)cf/h 107:k(S)cf/d 108:M(S)cf/s 109:M(S)cf/min 110:M(S)cf/h 111:M(S)cf/d 112:kJ/s 113:kJ/min 114:kJ/h 115:kJ/d 116:MJ/s 117:MJ/min 118:MJ/h 119:MJ/d 120:GJ/s 121:GJ/min 122:GJ/h 123:GJ/d 124:TJ/s 125:TJ/min 126:TJ/h 127:TJ/d 128:BTU/s 129:BTU/min 130:BTU/h 131:BTU/d 132:kBTU/s 133:kBTU/min 134:kBTU/h 135:kBTU/d 136:MBTU/s 137:MBTU/min 138:MBTU/h 139:MBTU/d 140:SPE. 2:m3 /h -
{"ADDR": 400, "TYPE": "uint8", "REGISTERS": ["m3 /s", "m3 /min", "m3 /h", "m3 /d", "km3 /s", "km3 /min", "km3 /h", "km3 /d", "l/s", "l/min", "l/h", "l/d", "mcf/s", "mcf/min", "mcf/h", "mcf/d", "cf/s", "cf/min", "cf/h", "cf/d", "kcf/s", "kcf/min", "kcf/h", "kcf/d", "USgal/s", "USgal/min", "USgal/h", "USgal/d", "kUSgal/s", "kUSgal/min", "kUSgal/h", "kUSgal/d", "UKgal/s", "UKgal/min", "UKgal/h", "UKgal/d", "kUKgal/s", "kUKgal/min", "kUKgal/h", "kUKgal/d", "mbbl/s", "mbbl/min", "mbbl/h", "mbbl/d", "bbl/s", "bbl/min", "bbl/h", "bbl/d", "kbbl/s", "kbbl/min", "kbbl/h", "kbbl/d", "kg/s", "kg/min", "kg/h", "kg/d", "t/s", "t/min", "t/h", "t/d", "lb/s", "lb/min", "lb/h", "lb/d", "klb/s", "klb/min", "klb/h", "klb/d", "(N)m3 /s", "(N)m3 /min", "(N)m3 /h", "(N)m3 /d", "k(N)m3 /s", "k(N)m3 /min", "k(N)m3 /h", "k(N)m3 /d", "M(N)m3 /s", "M(N)m3 /min", "M(N)m3 /h", "M(N)m3 /d", "(N)l/s", "(N)l/min", "(N)l/h", "(N)l/d", "(S)m3 /s", "(S)m3 /min", "(S)m3 /h", "(S)m3 /d", "k(S)m3 /s", "k(S)m3 /min", "k(S)m3 /h", "k(S)m3 /d", "M(S)m3 /s", "M(S)m3 /min", "M(S)m3 /h", "M(S)m3 /d", "(S)l/s", "(S)l/min", "(S)l/h", "(S)l/d", "(S)cf/s", "(S)cf/min", "(S)cf/h", "(S)cf/d", "k(S)cf/s", "k(S)cf/min", "k(S)cf/h", "k(S)cf/d", "M(S)cf/s", "M(S)cf/min", "M(S)cf/h", "M(S)cf/d", "kJ/s", "kJ/min", "kJ/h", "kJ/d", "MJ/s", "MJ/min", "MJ/h", "MJ/d", "GJ/s", "GJ/min", "GJ/h", "GJ/d", "TJ/s", "TJ/min", "TJ/h", "TJ/d", "BTU/s", "BTU/min", "BTU/h", "BTU/d", "kBTU/s", "kBTU/min", "kBTU/h","kBTU/d", "MBTU/s", "MBTU/min", "MBTU/h", "MBTU/d"], "DEFAULT": 2},
# Lowcut limit 401 30402 Float 2 0 to 99999.0 0.0 Flow unit\
{"ADDR": 401, "TYPE": "float", "RANGE": [0.0, 99999.0], "DEFAULT": 0.0},
# Flow user base unit 403 30404 Uint8 1 0:m3 /s 1:m3 /min 2:m3 /h 3:m3 /d 4:km3 /s 5:km3 /min 6:km3 /h 7:km3 /d 8:l/s 9:l/min 10:l/h 11:l/d 12:mcf/s 13:mcf/min 14:mcf/h 15:mcf/d 16:cf/s 17:cf/min 18:cf/h 19:cf/d 20:kcf/s 21:kcf/min 22:kcf/h 23:kcf/d 24:USgal/s 25:USgal/min 26:USgal/h 27:USgal/d 28:kUSgal/s 29:kUSgal/min 30:kUSgal/h 31:kUSgal/d 32:UKgal/s 33:UKgal/min 34:UKgal/h 35:UKgal/d 36:kUKgal/s 37:kUKgal/min 38:kUKgal/h 39:kUKgal/d 40:mbbl/s 41:mbbl/min 42:mbbl/h 43:mbbl/d 44:bbl/s 45:bbl/min 46:bbl/h 47:bbl/d 48:kbbl/s 49:kbbl/min 50:kbbl/h 51:kbbl/d 52:kg/s 53:kg/min 54:kg/h 55:kg/d 56:t/s 57:t/min 58:t/h 59:t/d 60:lb/s 61:lb/min 62:lb/h 63:lb/d 64:klb/s 65:klb/min 66:klb/h 67:klb/d 68:(N)m3 /s 69:(N)m3 /min 70:(N)m3 /h 71:(N)m3 /d 72:k(N)m3 /s 73:k(N)m3 /min 74:k(N)m3 /h 75:k(N)m3 /d 76:M(N)m3 /s 77:M(N)m3 /min 78:M(N)m3 /h 79:M(N)m3 /d 80:(N)l/s 81:(N)l/min 82:(N)l/h 83:(N)l/d 84:(S)m3 /s 85:(S)m3 /min 86:(S)m3 /h 87:(S)m3 /d 88:k(S)m3 /s 89:k(S)m3 /min 90:k(S)m3 /h 91:k(S)m3 /d 92:M(S)m3 /s 93:M(S)m3 /min 94:M(S)m3 /h 95:M(S)m3 /d 96:(S)l/s 97:(S)l/min 98:(S)l/h 99:(S)l/d 100:(S)cf/s 101:(S)cf/min 102:(S)cf/h 103:(S)cf/d 104:k(S)cf/s 105:k(S)cf/min 106:k(S)cf/h 107:k(S)cf/d 108:M(S)cf/s 109:M(S)cf/min 110:M(S)cf/h 111:M(S)cf/d 112:kJ/s 113:kJ/min 114:kJ/h 115:kJ/d 116:MJ/s 117:MJ/min 118:MJ/h 119:MJ/d 120:GJ/s 121:GJ/min 122:GJ/h 123:GJ/d 124:TJ/s 125:TJ/min 126:TJ/h 127:TJ/d 128:BTU/s 129:BTU/min 130:BTU/h 131:BTU/d 132:kBTU/s 133:kBTU/min 134:kBTU/h 135:kBTU/d 136:MBTU/s 137:MBTU/min 138:MBTU/h 139:MBTU/d 2:m3 /h -
{"ADDR": 403, "TYPE": "uint8", "REGISTERS": ["m3 /s", "m3 /min", "m3 /h", "m3 /d", "km3 /s", "km3 /min", "km3 /h", "km3 /d", "l/s", "l/min", "l/h", "l/d", "mcf/s", "mcf/min", "mcf/h", "mcf/d", "cf/s", "cf/min", "cf/h", "cf/d", "kcf/s", "kcf/min", "kcf/h", "kcf/d", "USgal/s", "USgal/min", "USgal/h", "USgal/d", "kUSgal/s", "kUSgal/min", "kUSgal/h", "kUSgal/d", "UKgal/s", "UKgal/min", "UKgal/h", "UKgal/d", "kUKgal/s", "kUKgal/min", "kUKgal/h", "kUKgal/d", "mbbl/s", "mbbl/min", "mbbl/h", "mbbl/d", "bbl/s", "bbl/min", "bbl/h", "bbl/d", "kbbl/s", "kbbl/min", "kbbl/h", "kbbl/d", "kg/s", "kg/min", "kg/h", "kg/d", "t/s", "t/min", "t/h", "t/d", "lb/s", "lb/min", "lb/h", "lb/d", "klb/s", "klb/min", "klb/h", "klb/d"], "DEFAULT": 2},
# Pulse output rate unit 500 30501 Uint8 1 0:m3 /p 1:km3 /p 2:l/p 3:mcf/p 4:cf/p 5:kcf/p 6:USgal/p 7:kUSgal/p 8:UKgal/p 9:kUKgal/p 10:mbbl/p 11:bbl/p 12:kbbl/p 13:kg/p 14:t/p 15:lb/p 16:klb/p 17:(N)m3 /p 18:k(N)m3 /p 19:M(N)m3 /p 20:(N)l/p 21:(S)m3 /p 22:k(S)m3 /p 23:M(S)m3 /p 24:(S)l/p 25:(S)cf/p 26:k(S)cf/p 27:M(S)cf/p 28:kJ/p 29:MJ/p 30:GJ/p 31:TJ/p 32:BTU/p 33:kBTU/p 34:MBTU/p 35:SPE./p 36:(Blank) 0:m3 /p - 
{"ADDR": 500, "TYPE": "uint8", "REGISTERS": ["m3 /p", "km3 /p", "l/p", "mcf/p", "cf/p", "kcf/p", "USgal/p", "kUSgal/p", "UKgal/p", "kUKgal/p", "mbbl/p", "bbl/p", "kbbl/p", "kg/p", "t/p", "lb/p", "klb/p", "(N)m3 /p", "k(N)m3 /p", "M(N)m3 /p", "(N)l/p", "(S)m3 /p", "k(S)m3 /p", "M(S)m3 /p", "(S)l/p", "(S)cf/p", "k(S)cf/p", "M(S)cf/p", "kJ/p", "MJ/p", "GJ/p", "TJ/p", "BTU/p", "kBTU/p", "MBTU/p"], "DEFAULT": 0},
# Status output condition 501 30502 Uint8 1 0:Not active 1:Active 0:Not active -
{"ADDR": 501, "TYPE": "uint8", "REGISTERS": ["Not active", "Active"], "DEFAULT": 0},
]

# 30001 1 Phase 1 line to neutral volts. Volts 00 00 √ X √
# 30003 2 Phase 2 line to neutral volts. Volts 00 02 √ X X 
# 30005 3 Phase 3 line to neutral volts. Volts 00 04 √ X X 
# 30007 4 Phase 1 current. Amps 00 06 √ √ √ 
# 30009 5 Phase 2 current. Amps 00 08 √ √ X 
# 30011 6 Phase 3 current. Amps 00 0A √ √ X 
# 30013 7 Phase 1 power. Watts 00 0C √ X √ 
# 30015 8 Phase 2 power. Watts 00 0E √ X √ 
# 30017 9 Phase 3 power. Watts 00 10 √ X X 
# 30019 10 Phase 1 volt amps. VoltAmps 00 12 √ X √ 
# 30021 11 Phase 2 volt amps. VoltAmps 00 14 √ X X 
# 30023 12 Phase 3 volt amps. VoltAmps 00 16 √ X X 
# 30025 13 Phase 1 volt amps reactive. VAr 00 18 √ X √ 
# 30027 14 Phase 2 volt amps reactive. VAr 00 1A √ X X 
# 30029 15 Phase 3 volt amps reactive. VAr 00 1C √ X X 
# 30031 16 Phase 1 power factor (1). None 00 1E √ X √ 
# 30033 17 Phase 2 power factor (1). None 00 20 √ X X 
# 30035 18 Phase 3 power factor (1). None 00 22 √ X X 
# 30037 19 Phase 1 phase angle. Degrees 00 24 √ X √ 
# 30039 20 Phase 2 phase angle. Degrees 00 26 √ X X 
# 30041 21 Phase 3 phase angle. Degrees 00 28 √ X X 
# 30043 22 Average line to neutral volts. Volts 00 2A √ X X 
# 30047 24 Average line current. Amps 00 2E √ √ √ 
# 30049 25 Sum of line currents. Amps 00 30 √ √ √ 
# 30053 27 Total system power. Watts 00 34 √ √ √ 
# 30057 29 Total system volt amps. VA 00 38 √ √ √ 
# 30061 31 Total system VAr. VAr 00 3C √ √ √ 
# 30063 32 Total system power factor (1). None 00 3E √ √ √ 
# 30067 34 Total system phase angle. Degrees 00 42 √ √ √ 
# 30071 36 Frequency of supply voltages. Hz 00 46 √ √ √ 
# 30073 37 Import Wh since last reset (2). kWh/MWh 00 48 √ √ √ 
# 30075 38 Export Wh since last reset (2). kWh/MWh 00 4A √ √ √ 
# 30077 39 Import VArh since last reset (2). kVArh/MVArh 00 4C √ √ √ 
# 30079 40 Export VArh since last reset (2). kVArh/MVArh 00 4E √ √ √ 
# 30081 41 VAh since last reset (2). kVAh/MVAh 00 50 √ √ √ 
# 30083 42 Ah since last reset (3). Ah/kAh 00 52 √ √ √ 
# 30085 43 Total system power demand (4). Watts 00 54 √ √ √ 
# 30087 44 Maximum total system power demand (4). Watts 00 56 √ √ √ 
# 30101 51 Total system VA demand. VA 00 64 √ √ √ 
# 30103 52 Maximum total system VA demand. VA 00 66 √ √ √ 
# 30105 53 Neutral current demand. Amps 00 68 √ X X 
# 30107 54 Maximum neutral current demand. Amps 00 6A √ X X 
# 30201 101 Line 1 to Line 2 volts. Volts 00 C8 √ √ X 
# 30203 102 Line 2 to Line 3 volts. Volts 00 CA √ √ X 
# 30205 103 Line 3 to Line 1 volts. Volts 00 CC √ √ X 
# 30207 104 Average line to line volts. Volts 00 CE √ √ X
# 30225 113 Neutral current. Amps 00 E0 √ X X 
# 30235 118 Phase 1 L/N volts THD % 00 EA √ X √ 
# 30237 119 Phase 2 L/N volts THD % 00 EC √ X X 
# 30239 120 Phase 3 L/N volts THD % 00 EE √ X X 
# 30241 121 Phase 1 Current THD % 00 F0 √ √ √ 
# 30243 122 Phase 2 Current THD % 00 F2 √ √ X 
# 30245 123 Phase 3 Current THD % 00 F4 √ √ X 
# 30249 125 Average line to neutral volts THD. % 00 F8 √ X √ 
# 30251 126 Average line current THD. % 00 FA √ √ √ 
# 30255 128 -Total system power factor (5). Degrees 00 FE √ √ √ 
# 30259 130 Phase 1 current demand. Amps 01 02 √ √ √ 
# 30261 131 Phase 2 current demand. Amps 01 04 √ √ X 
# 30263 132 Phase 3 current demand. Amps 01 06 √ √ X 
# 30265 133 Maximum phase 1 current demand. Amps 01 08 √ √ √ 
# 30267 134 Maximum phase 2 current demand. Amps 01 0A √ √ X 
# 30269 135 Maximum phase 3 current demand. Amps 01 0C √ √ X 
# 30335 168 Line 1 to line 2 volts THD. % 01 4E √ √ X 
# 30337 169 Line 2 to line 3 volts THD. % 01 50 √ √ X 
# 30339 170 Line 3 to line 1 volts THD. % 01 52 √ √ X 
# 30341 171 Average line to line volts THD. % 01 54 √ √ X 
# 30343 172 Total active energy kWh 01 56 √ √ √ 
# 30345 173 Total reactive energy kVarh 01 58 √ √ √ 
# 30347 174 Phase 1 import active energy kWh 01 5a √ √ √ 
# 30349 175 Phase 2 import active energy kWh 01 5c √ √ √ 
# 30351 176 Phase 3 import active energy kWh 01 5e √ √ √ 
# 30353 177 Phase 1 export active energy kWh 01 60 √ √ √ 
# 30355 178 Phase 2 export active energy kWh 01 62 √ √ √ 
# 30357 179 Phase 3 export active energy kWh 01 64 √ √ √ 
# 30359 180 Phase 1 total active energy kWh 01 66 √ √ √ 
# 30361 181 Phase 2 total active energy kWh 01 68 √ √ √ 
# 30363 182 Phase 3 total active energy kWh 01 6a √ √ √ 
# 30365 183 Phase 1 import reactive energy kVArh 01 6c √ √ √ 
# 30367 184 Phase 2 import reactive energy kVArh 01 6e √ √ √ 
# 30369 185 Phase 3 import reactive energy kVArh 01 70 √ √ √ 
# 30371 186 Phase 1 export reactive energy kVArh 01 72 √ √ √ 
# 30373 187 Phase 2 export reactive energy kVArh 01 74 √ √ √ 
# 30375 188 Phase 3 export reactive energy kVArh 01 76 √ √ √ 
# 30377 189 Phase 1 total reactive energy kVArh 01 78 √ √ √ 
# 30379 190 Phase 2 total reactive energy kVArh 01 7a √ √ √ 
# 30381 191 Phase 3 total reactive energy kVArh 01 7c √ √ √






# 0x10d9	input	u16	big endian	(voltage)		Urms L1	Напряжение (RMS) на фазе L1	В	 
# 0x1810	input	s32	little endian	(voltage)		Upeak L1	Пиковое значение напряжения на фазе L1	В	 
# 0x10da	input	u16	big endian	(voltage)		Urms L2	Напряжение (RMS) на фазе L2	В	 
# 0x1812	input	s32	little endian	(voltage)		Upeak L2	Пиковое значение напряжения на фазе L2	В	 
# 0x10db	input	u16	big endian	(voltage)		Urms L3	Напряжение (RMS) на фазе L3	В	 
# 0x1814	input	s32	little endian	(voltage)		Upeak L3	Пиковое значение напряжения на фазе L3	В	 
# 0x10f8	input	u16	big endian	(value)		Frequency	Частота	Гц	 
# 0x10fd	input	s16	big endian	(value)	0.1	Voltage angle L1	Фазовый угол сдвига напряжения между фазами (всегда 0, отсчет ведется от фазы L1)	°	
# 0x10fe	input	s16	big endian	(value)	0.1	Voltage angle L2	Фазовый угол сдвига напряжения между фазами L1 и L2	°	
# 0x10ff	input	s16	big endian	(value)	0.1	Voltage angle L3	Фазовый угол сдвига напряжения между фазами L1 и L3	°	
# 0x10dd	input	u16	big endian	(value)		Irms L1	Ток (RMS) на фазе L1	А	
# 0x1818	input	s32	little endian	(value)		Ipeak L1	Пиковое значение тока на фазе L1	А	
# 0x1302	input	s32	big endian	(power)		P L1	Активная мощность для фазы L1	Вт	 
# 0x130a	input	s32	big endian	(value)		Q L1	Реактивная мощность для фазы L1	вар	 
# 0x1312	input	s32	big endian	(value)		S L1	Кажущаяся мощность для фазы L1	В·А	 
# 0x10bd	input	s16	big endian	(value)		PF L1	Коэффициент мощности для фазы L1		
# 0x1204	input	u64	little endian	(power_consumption)		AP energy L1	Прямая активная энергия для фазы L1	кВт·ч	 
# 0x1224	input	u64	little endian	(value)		RP energy L1	Прямая реактивная энергия для фазы L1	квар·ч	 
# 0x10de	input	u16	big endian	(value)		Irms L2	Ток (RMS) на фазе L2	А	
# 0x181a	input	s32	little endian	(value)		Ipeak L2	Пиковое значение тока на фазе L2	А	
# 0x1304	input	s32	big endian	(power)		P L2	Активная мощность для фазы L2	Вт	
# 0x130c	input	s32	big endian	(value)		Q L2	Реактивная мощность для фазы L2	вар	
# 0x1314	input	s32	big endian	(value)		S L2	Кажущаяся мощность для фазы L2	В·А	 
# 0x10be	input	s16	big endian	(value)		PF L2	Коэффициент мощности для фазы L2		 
# 0x1208	input	u64	little endian	(power_consumption)		AP energy L2	Прямая активная энергия для фазы L2	кВт·ч	 
# 0x1228	input	u64	little endian	(value)		RP energy L2	Прямая реактивная энергия для фазы L2	квар·ч	
# 0x10df	input	u16	big endian	(value)		Irms L3	Ток (RMS) на фазе L3	А	
# 0x181c	input	s32	little endian	(value)		Ipeak L3	Пиковое значение тока на фазе L2	А	
# 0x1306	input	s32	big endian	(power)		P L3	Активная мощность для фазы L3	Вт	
# 0x130e	input	s32	big endian	(value)		Q L3	Реактивная мощность для фазы L3	вар	 
# 0x1316	input	s32	big endian	(value)		S L3	Кажущаяся мощность для фазы L3	В·А	 
# 0x10bf	input	s16	big endian	(value)		PF L3	Коэффициент мощности для фазы L3		 
# 0x120c	input	u64	little endian	(power_consumption)		AP energy L3	Прямая активная энергия для фазы L3	кВт·ч	
# 0x122c	input	u64	little endian	(value)		RP energy L3	Прямая реактивная энергия для фазы L3	квар·ч	
# 0x1300	input	s32	big endian	(power)		Total P	Суммарная активная мощность	Вт	
# 0x1308	input	s32	big endian	(value)		Total Q	Суммарная реактивная мощность	вар	
# 0x1310	input	s32	big endian	(value)		Total S	Суммарная кажущаяся мощность	В·А	
# 0x10bc	input	s16	big endian	(value)		Total PF	Суммарный коэффициент мощности		 
# 0x1200	input	u64	little endian	(power_consumption)		Total AP energy	Суммарная прямая активная энергия	кВт·ч	
# 0x1220	input	u64	little endian	(value)		Total RP energy	Суммарная прямая реактивная энергия	квар·ч	
# 0x10f9	input	s16	big endian	(value)	0.1	Phase angle L1	Угол фазового сдвига между напряжением и током для фазы L1	°	
# 0x10fa	input	s16	big endian	(value)	0.1	Phase angle L2	Угол фазового сдвига между напряжением и током для фазы L2	°	
# 0x10fb	input	s16	big endian	(value)	0.1	Phase angle L3	Угол фазового сдвига между напряжением и током для фазы L3	°	

# 0x10d9    input    u16    big endian    (voltage)        Urms L1    Voltage (RMS) on phase L1    V     
# 0x1810    input    s32    little endian    (voltage)        Upeak L1    Peak voltage on phase L1    V     
# 0x10da    input    u16    big endian    (voltage)        Urms L2    Voltage (RMS) on phase L2    V     
# 0x1812    input    s32    little endian    (voltage)        Upeak L2    Peak voltage on phase L2    V     
# 0x10db    input    u16    big endian    (voltage)        Urms L3    Voltage (RMS) on phase L3    V     
# 0x1814    input    s32    little endian    (voltage)        Upeak L3    Peak voltage on phase L3    V     
# 0x10f8    input    u16    big endian    (value)        Frequency    Frequency    Hz     
# 0x10fd    input    s16    big endian    (value)        Voltage angle L1    Phase shift angle of voltage between phases (always 0, counted from phase L1)    °    
# 0x10fe    input    s16    big endian    (value)        Voltage angle L2    Phase shift angle of voltage between phases L1 and L2    °    
# 0x10ff    input    s16    big endian    (value)        Voltage angle L3    Phase shift angle of voltage between phases L1 and L3    °    
# 0x10dd    input    u16    big endian    (value)        Irms L1    Current (RMS) on phase L1    A    
# 0x1818    input    s32    little endian    (value)        Ipeak L1    Peak current on phase L1    A    
# 0x1302    input    s32    big endian    (power)        P L1    Active power for phase L1    W     
# 0x130a    input    s32    big endian    (value)        Q L1    Reactive power for phase L1    var     
# 0x1312    input    s32    big endian    (value)        S L1    Apparent power for phase L1    VA     
# 0x10bd    input    s16    big endian    (value)        PF L1    Power factor for phase L1        
# 0x1204    input    u64    little endian    (power_consumption)        AP energy L1    Forward active energy for phase L1    kWh     
# 0x1224    input    u64    little endian    (value)        RP energy L1    Forward reactive energy for phase L1    kvarh     
# 0x10de    input    u16    big endian    (value)        Irms L2    Current (RMS) on phase L2    A    
# 0x181a    input    s32    little endian    (value)        Ipeak L2    Peak current on phase L2    A    
# 0x1304    input    s32    big endian    (power)        P L2    Active power for phase L2    W    
# 0x130c    input    s32    big endian    (value)        Q L2    Reactive power for phase L2    var    
# 0x1314    input    s32    big endian    (value)        S L2    Apparent power for phase L2    VA     
# 0x10be    input    s16    big endian    (value)        PF L2    Power factor for phase L2         
# 0x1208    input    u64    little endian    (power_consumption)        AP energy L2    Forward active energy for phase L2    kWh     
# 0x1228    input    u64    little endian    (value)        RP energy L2    Forward reactive energy for phase L2    kvarh    
# 0x10df    input    u16    big endian    (value)        Irms L3    Current (RMS) on phase L3    A    
# 0x181c    input    s32    little endian    (value)        Ipeak L3    Peak current on phase L2    A    
# 0x1306    input    s32    big endian    (power)        P L3    Active power for phase L3    W    
# 0x130e    input    s32    big endian    (value)        Q L3    Reactive power for phase L3    var     
# 0x1316    input    s32    big endian    (value)        S L3    Apparent power for phase L3    VA     
# 0x10bf    input    s16    big endian    (value)        PF L3    Power factor for phase L3         
# 0x120c    input    u64    little endian    (power_consumption)        AP energy L3    Forward active energy for phase L3    kWh    
# 0x122c    input    u64    little endian    (value)        RP energy L3    Forward reactive energy for phase L3    kvarh    
# 0x1300    input    s32    big endian    (power)       Total P    Total active power    W    
# 0x1308    input    s32    big endian    (value)       Total Q    Total reactive power    var    
# 0x1310    input    s32    big endian    (value)       Total S    Total apparent power    VA    
# 0x10bc    input    s16    big endian    (value)     Total PF    Total power factor         
# 0x1200    input    u64    little endian    (power_consumption)       Total AP energy    Total forward active energy    kWh    
# 0x1220    input    u64    little endian    (value)        Total RP energy    Total forward reactive energy    kvarh    
# 0x10f9    input    s16    big endian    (value)        Phase angle L1    Phase shift angle between voltage and current for phase L1    °    
# 0x10fa    input    s16    big endian    (value)        Phase angle L2    Phase shift angle between voltage and current for phase L2    °    
# 0x10fb    input    s16    big endian    (value)        Phase angle L3    Phase shift angle between voltage and current for phase L3    °    



        # Urms_L1 = random.uniform(220.0, 240.0)
        # Urms_L2 = random.uniform(220.0, 240.0)
        # Urms_L3 = random.uniform(220.0, 240.0)
        
        # # Simulating peak voltage values (Upeak) for three phases in volts (V)
        # Upeak_L1 = random.uniform(300.0, 340.0)
        # Upeak_L2 = random.uniform(300.0, 340.0)
        # Upeak_L3 = random.uniform(300.0, 340.0)
        
        # # Simulating frequency in Hz
        # Frequency = random.uniform(49.0, 51.0)
        
        # # Simulating phase shift angles (Voltage angle) in degrees
        # Voltage_angle_L1 = 0  # Always 0 for L1
        # Voltage_angle_L2 = random.uniform(110.0, 130.0)
        # Voltage_angle_L3 = random.uniform(230.0, 250.0)
        
        # # Simulating current values (Irms) for three phases in amps (A)
        # Irms_L1 = random.uniform(0.0, 50.0)
        # Irms_L2 = random.uniform(0.0, 50.0)
        # Irms_L3 = random.uniform(0.0, 50.0)
        
        # # Simulating peak current values (Ipeak) for three phases in amps (A)
        # Ipeak_L1 = random.uniform(0.0, 70.0)
        # Ipeak_L2 = random.uniform(0.0, 70.0)
        # Ipeak_L3 = random.uniform(0.0, 70.0)
        
        # # Simulating power values (P, Q, S) for three phases in watts (W), vars (var), and volt-amperes (VA)
        # P_L1 = random.uniform(0.0, 10000.0)
        # Q_L1 = random.uniform(-10000.0, 10000.0)
        # S_L1 = random.uniform(0.0, 12000.0)
        
        # P_L2 = random.uniform(0.0, 10000.0)
        # Q_L2 = random.uniform(-10000.0, 10000.0)
        # S_L2 = random.uniform(0.0, 12000.0)
        
        # P_L3 = random.uniform(0.0, 10000.0)
        # Q_L3 = random.uniform(-10000.0, 10000.0)
        # S_L3 = random.uniform(0.0, 12000.0)
        
        # # Simulating power factor (PF) for three phases
        # PF_L1 = random.uniform(0.0, 1.0)
        # PF_L2 = random.uniform(0.0, 1.0)
        # PF_L3 = random.uniform(0.0, 1.0)
        
        # # Simulating energy values (AP energy, RP energy) in kWh and kvarh
        # AP_energy_L1 = random.uniform(0.0, 5000.0)
        # RP_energy_L1 = random.uniform(0.0, 3000.0)
        
        # AP_energy_L2 = random.uniform(0.0, 5000.0)
        # RP_energy_L2 = random.uniform(0.0, 3000.0)
        
        # AP_energy_L3 = random.uniform(0.0, 5000.0)
        # RP_energy_L3 = random.uniform(0.0, 3000.0)
        
        # Total_P = P_L1 + P_L2 + P_L3
        # Total_Q = Q_L1 + Q_L2 + Q_L3
        # Total_S = S_L1 + S_L2 + S_L3
        
        # Total_PF = (PF_L1 + PF_L2 + PF_L3) / 3
        
        # Total_AP_energy = AP_energy_L1 + AP_energy_L2 + AP_energy_L3
        # Total_RP_energy = RP_energy_L1 + RP_energy_L2 + RP_energy_L3
        
        # Phase_angle_L1 = random.uniform(-30.0, 30.0)
        # Phase_angle_L2 = random.uniform(-30.0, 30.0)
        # Phase_angle_L3 = random.uniform(-30.0, 30.0)