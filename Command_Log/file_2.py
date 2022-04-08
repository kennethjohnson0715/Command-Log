import pandas as pd

df = pd.read_csv("03_03_2022_cmd_history_v1.csv")
byte_1 = df['LAST_ACC_CMD_BYTES1']
byte_2 = df['LAST_ACC_CMD_BYTES2']

for index in range(0, len(df)):
    
    if (int(byte_1[index]) == 36 and int(byte_2[index]) == 1) \
        or (int(byte_1[index]) == 31 and int(byte_2[index]) == 11):
        print(f"{df.iloc[index].to_frame().T.to_string(header=False, index=False)}")
