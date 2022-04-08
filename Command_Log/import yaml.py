import opcode
import yaml


with open('cmd_vE.yaml') as f:
    
    data = yaml.load(f, Loader=yaml.BaseLoader)
    print(data[0])
    
    for doc in data:

        print(doc.get("opcode") + " " + doc.get("name"))
