import requests
import pytest
from utility import utils 
import configparser
import json
import items
import logging as logger

config = configparser.ConfigParser()
config.read('properties.ini')

with open('testdata.json') as f:
    test_data = json.load(f)

#@pytest.mark.testing
@pytest.mark.parametrize('payload',[{"name":"diaper"},{"name":"powder"},{"name":"cream"},{"name":"bottle"},{"name":"medicine"}])
def test_Creation_Of_Categories(login,payload):
    # data = [{"name":"diaper"},{"name":"powder"},{"name":"cream"},{"name":"bottle"},{"name":"medicine"}]
    # for i in range(5):
        # response_code,response_data = utils.post_data(login,'categories',data[i])
        # assert response_code == 201, f"failed, beacuse we are expecting 201 but got {response_code}"
    response_code,response_data = utils.post_data(login,'categories',payload)
    assert response_code == 201, f"failed, beacuse we are expecting 201 but got {response_code}"

@pytest.mark.testing
def test_Update_Categories(login):
    # with hardcoaded data
    # data = {'name':'powder1'}
    # powder_Id = utils.get_id(login,'categories','diaper')
    # response_code,response = utils.update_with_id(login,'categories',powder_Id,data)
    # assert response_code == 200, f"failed because we are expecting 200 but got {response_code}"
    #with data from json
    Id = utils.get_id(login,'categories','powder')
    response_code,response = utils.update_with_id(login,'categories',Id,test_data["update_category"][0]["payload"])
    assert response_code == test_data['update_category'][0]['expected_status']
    

#@pytest.mark.testing
def test_Delete_data(login):
    id = utils.get_id(login,config['data']['category'],'powder')
    response_code,response = utils.delete_with_id(login,config['data']['category'],id)
    assert response_code == 200, f"failed, because we are expecting status code 200 but got {response_code}"

@pytest.mark.uom
def test_Create_uom(login):
    data = {'name':'Dozen'} 
    response_code,response = utils.post_data(login,'uom',data)
    assert response_code == 201, f"failed because we are expecting 201 and got {response_code}"

@pytest.mark.uom
def test_Update_uom(login):
    data = {'name':'kg'}
    id = utils.get_id(login,'uom','dozen')
    response_code,response = utils.update_with_id(login,'uom',id,data)
    assert response_code == 200, f"failed because we are expecting 200 and got {response_code}"

@pytest.mark.item
def test_add_item_with_quantity_6(login):
    logger.info("test_add_item_with_quantity_6")
    response_code,response = items.create_item(login,'durga','mango','kg',6)
    assert response_code == 201, f"item creation failed: because we are expecting 201 and got {response_code}"
    id = response['id']
    data = items.get_item(login,87658)
    print(data)
    assert data is not None, f"item not found after creation: not getting data as id not found, getting {data} in return"



#@pytest.mark.paramaterize('input,outpu,msg',[({'name':'leena'},200,"cate created")])