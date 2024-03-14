import base64
import json
# print(base64.b64decode('DumlkrqalRjQWYbWVvQMIRTEmTwRuymTjSHUcwTNjm4=').hex())
# print(base64.b64decode('APFEUjXyFIxZhlhxafwbzYh7CNTQCGjfVpb/9AlW6GQ=').hex())
#constants_num = "3"
for i in range(1, 17):
    constants_num = str(i)
    with open("constants/"+constants_num+"_old.json", "r") as file:
                constants = json.load(file)

    C = constants["C"]
    M = constants["M"]
    data = {}
    data["C"] = []
    data["M"] = []
    for i in range(len(C)):
        data["C"].append("0x"+base64.b64decode(C[i]).hex())
    for x in range(len(M)):
        data["M"].append([])
        for y in range(len(M[x])):
            data["M"][x].append("0x"+base64.b64decode(M[x][y]).hex())

    constants_num = str((int(constants_num) + 1))
    with open("constants/"+constants_num+".json", "w") as file:
            json.dump(data, file, indent=4)