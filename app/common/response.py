def success(code=200, msg="success", data=None):
    return {
        "code": code,
        "msg": msg,
        "data": data
    }

def error(code=400, msg="error", data=None):
    return {
        "code": code,
        "msg": msg,
        "data": data
    }
