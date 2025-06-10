


def assert_upload(data):
    errstring = ""
    
    if "username" not in data:
        errstring += "User field null! "
        
    if "actual_data" not in data:
        errstring += "Actual data field null! "
    
    assert errstring == ""
    
    return errstring or "No issues"