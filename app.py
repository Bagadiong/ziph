
import json
f=open("data.txt","r")
data=[{}]
checker=True
counter=0
my_list=[]
while checker:
    line=f.readline()
    if line:
        for x in line:
            if x == "*":
                
                tempo={}
                print(line[1:])
                tempo["name"]=line[1:]
                data.append(tempo)
                data[counter+1]["arr"]=[]
                counter+=1
                
                break
            else:
                tempo={}
                data_name=line[0:4]
                data_value=line[6:]
                tempo[data_name]=data_value
                data[counter]["arr"].append(tempo)
                print(data_name+":"+data_value)
                break
                
    else: 
        break
del data[0]


f.close()
n=open("data.json","w")
n.write(json.dumps(data))
n.close()

