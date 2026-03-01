import requests
import pytest
from utility import utils 
import configparser

config = configparser.ConfigParser()
config.read('properties.ini')

def test_AllItems(login):
    response_code,response = utils.get_data(login,'product')
    print(response)
    assert response_code == 200


def test_GetID(login):
    id = utils.get_id(login,'uom','dozen')
    print(id)

@pytest.mark.testing
@pytest.mark.parametrize('payload',[{"name":"diaper"},{"name":"powder"},{"name":"cream"},{"name":"bottle"},{"name":"medicine"}])
def test_Creation_Of_Categories(login,payload):
    # data = [{"name":"diaper"},{"name":"powder"},{"name":"cream"},{"name":"bottle"},{"name":"medicine"}]
    # for i in range(5):
        # response_code,response_data = utils.post_data(login,'categories',data[i])
        # assert response_code == 201, f"failed, beacuse we are expecting 201 but got {response_code}"
    response_code,response_data = utils.post_data(login,'categories',payload)
    assert response_code == 201, f"failed, beacuse we are expecting 201 but got {response_code}"

#@pytest.mark.testing
def test_Update_Categories(login):
    data = {'name':'powder1'}
    powder_Id = utils.get_id(login,'categories','diaper')
    response_code,response = utils.update_with_id(login,'categories',powder_Id,data)
    assert response_code == 200, f"failed because we are expecting 200 but got {response_code}"

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
def test_Create_Item(login):
    cafe_id = utils.get_id(login,'cafe','durga')
    product_id = utils.get_id(login,'product','mango')
    uom_id = utils.get_id(login,'uom','kg')
    data = {"cafe_id": cafe_id,"product_id":product_id,"uom_id":uom_id,"quantity":6,"date":"12/30"}
    response_code,response = utils.post_data(login,'items',data)
    assert response_code == 201, f"failed because we are expecting 201 and got {response_code}"

