import csv
from xml.sax import parseString
import ast
import pandas as pd



thisdict =	{}
cmdlog = open("Command_Log.txt", "w")



with open("Command Dictionary.csv", "r") as f:
   reader = csv.reader(f)
   for line in reader:
        
        thisdict[(line[0])]=line[1]

with open("03_03_2022_cmd_history_v1.csv", "r") as f:
    reader = csv.reader(f)

    lastcmd = ""
    last_time = ""

    #for x in range():
        #print(x)

    for i, line in enumerate(reader): 
        if i==0:
            pass
        if lastcmd != thisdict.get(line[2]):        
            

            
            lastcmd = thisdict.get(line[2])
            #print('line[{}] = {} {} '.format(i, line[0], thisdict.get(line[2]))) 
            #cmdlog.write('line[{}] = {} {}\n '.format(i, line[0], thisdict.get(line[2]))) 



#---------using panda data tool- to do this use -pip install panda or -import pandas as pd---------#
rt = pd.read_csv("03_03_2022_cmd_history_v1.csv") #rt is variable for RADIO_RAW and THRUSTER_DIRECT_CMD 

byte_1 = rt['LAST_ACC_CMD_BYTES1']
byte_2 = rt['LAST_ACC_CMD_BYTES2']
byte_6 = rt['LAST_ACC_CMD_BYTES6'] #_RADIO_RAW enumerate 6th byte
byte_3 = rt['LAST_ACC_CMD_BYTES3'] #_THRUSTER_DIRECT_CMD enumerate 3rd byte

lastcmd = ""
lastcmd2 = ""
#last_time = ""

for index in range(0, len(rt)):

#for index in range(1170, 1190):
   
    if (int(byte_1[index]) == 36 and int(byte_2[index]) == 1):
        #print(byte_3[index])
        #cmdlog.write((byte_3[index]))

        #if lastcmd != byte_1[index] and lastcmd2 != byte_2[index]:
            #lastcmd = byte_1[index]

        
            print(('THRUSTER_DIRECT_CMD 3rd byte @ ''line[{}] = {} {} = {}\n'.format(index, rt['time'][index],\
                 rt['TAI_SECONDS'][index], rt['LAST_ACC_CMD_BYTES3'][index])))
            
            cmdlog.write(('THRUSTER_DIRECT_CMD 3rd byte @ ''line[{}] = {} {} = {}\n'.format(index, rt['time'][index],\
                 rt['TAI_SECONDS'][index], rt['LAST_ACC_CMD_BYTES3'][index])))

        
            #print(f"{rt.iloc[index].to_frame().T.to_string(header=False, index=False)}\n")
            #cmdlog.write(f"{rt.iloc[index].to_frame().T.to_string(header=False, index=False)}\n")       

    
    
    if (int(byte_1[index]) == 31 and int(byte_2[index]) == 11):
        #print(byte_6[index])

        #if lastcmd != byte_1[index]:
            #lastcmd = byte_1[index]

            print(('RADIO_RAW 6th byte @ ''line[{}] = {} {} = {}\n'.format(index, rt['time'][index],\
                 rt['TAI_SECONDS'][index], rt['LAST_ACC_CMD_BYTES6'][index]))) 
            
            cmdlog.write(('RADIO_RAW 6th byte @ ''line[{}] = {} {} = {}\n'.format(index, rt['time'][index],\
                 rt['TAI_SECONDS'][index], rt['LAST_ACC_CMD_BYTES6'][index])))        


        
            #print(f"{rt.iloc[index].to_frame().T.to_string(header=False, index=False)}\n")
            #cmdlog.write(f"{rt.iloc[index].to_frame().T.to_string(header=False, index=False)}\n")



#s = ast.literal_eval('0x1f0b')
#print(s)           
            
        
cmdlog.close()




##########KENJOJO