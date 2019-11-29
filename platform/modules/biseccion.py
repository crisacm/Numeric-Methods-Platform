def validate_function(f):
    try:
        x = 0
        eval(f)
        return True
    except:
        return False