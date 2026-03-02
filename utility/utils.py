#get by id, put byt id, post, delete by id
import requests
import pytest
import configparser
from conftest import * 


config = configparser.ConfigParser()
config.read('/home/lagnesh/Desktop/pytest/properties.ini')

def get_data_by_id(login,endpoint,id):
    header = {'authorization':f"Bearer {login}",'Content-Type':'application/json'}
    response = requests.get(config['api']['base_url2']+config['endpoint'][endpoint],headers=header)
    for i in response.json():
        if i['id'] == id:
            return i
    

def get_id(login,endpoint,name):
    header = {'authorization':f"Bearer {login}",'Content-Type':'application/json'}
    response = requests.get(config['api']['base_url2']+config['endpoint'][endpoint],headers=header)
    for i in response.json():
        if i['name'] == name:
            return i['id']
        
def post_data(login,endpoint,data):
    header = {'authorization':f"Bearer {login}",'Content-Type':'application/json'}
    response = requests.post(config['api']['base_url2']+config['endpoint'][endpoint],headers=header,json=data)
    return response.status_code,response.json()

def update_with_id(login,endpoint,id,data):
    header = {'authorization':f"Bearer {login}",'Content-Type':'application/json'}
    response = requests.patch(config['api']['base_url2']+config['endpoint'][endpoint]+"/"+id,headers=header,json=data)
    return response.status_code,response.json()

def delete_with_id(login,endpoint,id):
    header = {'authorization':f"Bearer {login}",'Content-Type':'application/json'}
    response = requests.delete(config['api']['base_url2']+config['endpoint'][endpoint]+"/"+id,headers=header)
    return response.status_code,response.json()


