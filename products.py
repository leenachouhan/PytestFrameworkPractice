import utility.utils as utils

def create_product(login):
    response_code,response = utils.post_data(login,'product',data)
    return response_code,response