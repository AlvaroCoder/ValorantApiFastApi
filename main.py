# Primeros pasos en FastApi
from fastapi import FastAPI
import requests
import json

app = FastAPI()
url = 'https://valorant-api.com/v1/agents'

@app.get("/")
async def root():
    return {
        "message":"Bienvenido a la App de Valorant"
    }

@app.get("/agentes")
async def root():
    res = requests.get(url)
    response = res.json()
    data = [{"uuid":i['uuid'],"name":i['displayName'],"description":i['description']} for i in response['data'] ]

    return {
        "data":data
    }

@app.get("/agentes/{nameAgent}")
async def root(nameAgent):
    res_name = requests.get(url,params={"isPlayableCharacter":True})
    response_name = res_name.json()['data'] 
    filter_name = list(filter(lambda x :nameAgent.lower() in x['displayName'].lower() , response_name))
    data = [{"uuid":i['uuid'],"name":i['displayName'],"description":i['description']} for i in filter_name ]    
    return{
        "data": data
    }
