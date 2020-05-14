sentensce = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

x = [1, 5, 6, 7, 8, 9, 15, 16, 19]

words = sentensce.split()

y = {}

for it, word in enumerate(words):
    if it + 1 in x:
        y[it+1] = word[0]
    else:
        y[it+1] = word[:2]

print(y)
