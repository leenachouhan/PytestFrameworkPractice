import utility.utils as utils

def create_uom(login,data):
    response_code,response=utils.post_data(login,'uom',data)
    return response_code,response

def get_uom_id(login,name):
    cate_id = utils.get_id(login,'uom',name)
    return cate_id

def update_uom(login,id,data):
    response_code,respone = utils.update_with_id(login,'uom',id,data)
    return response_code,respone

def delete_uom(login,id):
    response_code,response = utils.delete_with_id(login,'uom',id)
    return response_code,response