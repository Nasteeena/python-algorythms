def find_palindrom(value):
    res_value = value.lower().strip()
    if res_value[::-1] == value:
        return True
    else:
        return False