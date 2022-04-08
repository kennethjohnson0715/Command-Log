#import literal_eval from ast module
from ast import literal_eval
 
RADIO_RAW = '0x1F0B'
THRUSTER_DIRECT_CMD = '0x2401'
 
# conversion
dec1 = literal_eval(RADIO_RAW)
dec2 = literal_eval(THRUSTER_DIRECT_CMD)
 
print("The hexadecimal string is: ", RADIO_RAW, THRUSTER_DIRECT_CMD)
print("The decimal number is: ", dec1,dec2)
