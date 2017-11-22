import re
def alphanumeric(texto):
    if re.search('^[0-9a-zA-Z]+$',texto) == None:
        return False
    else:
        return True

print(alphanumeric("hello_w0rld"))
