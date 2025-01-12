def make_response_data(data=None, message='成功', code=200):
    response = {
        'code': code,
        'message': message,
        'data': data
    }
    return response
