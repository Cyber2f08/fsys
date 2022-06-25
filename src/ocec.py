def typeval(value, atype):
    if type(value) != atype:
        return False, type(value);
    return True, type(value);

def conchk(value):
    if value.status_code != 200:
        return False, value.status_code;
    return True, value.status_code;

