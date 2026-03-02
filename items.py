import utility.utils as utils

def create_item(login,cafe_name,product_name,uom_name,quantity):
    cafe_id = utils.get_id(login,'cafe',cafe_name)
    product_id = utils.get_id(login,'product',product_name)
    uom_id = utils.get_id(login,'uom',uom_name)
    data = {"cafe_id": cafe_id,"product_id":product_id,"uom_id":uom_id,"quantity":quantity,"date":"12/30"}
    response_code,response = utils.post_data(login,'items',data)
    return response_code,response

def get_item(login,item_id):
    data = utils.get_data_by_id(login,'items',item_id)
    return data
    