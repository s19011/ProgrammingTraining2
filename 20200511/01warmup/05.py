def n_gram(target, n):
    return [ target[idx:idx + n] for idx in range(len(target) - n + 1)]

target = "I am an NLPer"
print(n_gram(target, 1))

words = target.split(' ')
print(n_gram(words, 1))
