import re
str = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
word = re.split(r'[,.]? ?', str)
word = list(filter(lambda w: w != '', word))

word_len = list(map(len, word))

print(word_len)
