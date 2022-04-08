import csv
from xml.sax import parseString



thisdict =	{}
cmdlog = open("Command_Log.txt", "w")



with open("Command Dictionary.csv", "r") as f:
   reader = csv.reader(f)
   for line in reader:
        
        thisdict[(line[0])]=line[1]

with open("02_02_2022_cmd_history_v1.csv", "r") as f:
    reader = csv.reader(f)

    lastcmd = ""
    last_time = ""

    for i, line in enumerate(reader): 
        if i==0:
            pass
        if lastcmd != thisdict.get(line[2]):

            
            

            
            lastcmd = thisdict.get(line[2])
            print('line[{}] = {} {} '.format(i, line[0], thisdict.get(line[2]))) 
            cmdlog.write('line[{}] = {} {}\n '.format(i, line[0], thisdict.get(line[2]))) 
            
            

cmdlog.close()








