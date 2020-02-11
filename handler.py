import json
import requests
import zipApi

def response(text):
    respHeaders ={
        'Acces-Control-Allow-Origin':'*'
    }
    return {
        'statusCode':200,
        'headers': respHeaders,
        'body': json.dumps(text)
    }

def hello(event, context):
    print(event)
    path=event['requestContext']['resourcePath']
    pathParams=event['pathParameters']
    if(path=='/zip/all'):
        body=zipApi.getZipAll()
    elif(path=='/zipnumber/{zip-number}'):
        body=zipApi.getZip(pathParams['zip-number'])
    elif(path=='/province/{province-name}'):
        body=zipApi.getProvince(pathParams['province-name'])
    elif(path=='/city/{city-name}'):
        body=zipApi.getCity(pathParams['city-name'])

    

    return response(body)