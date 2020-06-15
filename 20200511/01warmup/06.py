def n_gram(target, n):
    result = []
    for i in range(0, len(target) - n + 1):
        result.append(target[i:i + n])

    return result

x = set(n_gram('paraparaparadise', 2))
print('X=' + str(x))
y = set(n_gram('paragraph', 2))
print('Y=' + str(y))

wa = x.union(y)
print(str(wa))

seki = x.intersection(y)
print(str(seki))

sa = x.difference(y)
print(str(sa))

print('seがXに含まれる' + str('se' in x))
print('seがYに含まれる' + str('se' in y))

