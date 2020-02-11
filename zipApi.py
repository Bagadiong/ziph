import json
import app


def init():
    response=app.getData()
    return response

def getZipAll():
    zipAll=json.loads(init())
    response=zipAll
    return response
    
def getZip(num):
    response={}
    data=json.loads(init())
    for x in data:
        for y in x['arr']:
            if num.lower() in y.lower():
                response['name']=x['name']
                response['arr']=y
    print(response)
    return response

def getCity(name):
    response=[{}]
    data=json.loads(init())
    for x in data:
        for y in x['arr']:
            for z in y:
                if name.lower() in y[z].lower():
                    city={}
                    city['name']=x['name']
                    city['arr']=y
                    response.append(city)
    del response[0]
    print(response)
    return response


def getProvince(name):
    data=json.loads(init())
    response=[{}]
    for x in data:
        if name in x['name']:
            response.append(x)       
            print(x)
    return response