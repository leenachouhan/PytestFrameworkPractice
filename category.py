import utility.utils as utils

def create_category(login,data):
    response_code,response=utils.post_data(login,'categories',data)
    return response_code,response

def get_category_id(login,name):
    cate_id = utils.get_id(login,'categories',name)
    return cate_id

def update_category(login,id,data):
    response_code,respone = utils.update_with_id(login,'categories',id,data)
    return response_code,respone

def delete_category(login,id):
    response_code,response = utils.delete_with_id(login,'categories',id)
    return response_code,response