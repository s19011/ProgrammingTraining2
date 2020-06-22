import re

def cipher(src):
    return re.sub(r'[a-z]', lambda m: chr(219 - ord(m.group(0))), src)
x = 'buuuu baaaaa gil;gsjlaut faoijddkl'
print (cipher(x))
print(cipher(cipher(x)))
