import random

def typoglycemia(text):
    def random_word(word):
        if len(word) < 5:
            return word
        arr = list(word[1: -1])
        random.shuffle(arr)
        return word[0] + "".join(arr) + word[-1]
    return " ".join(list(map(random_word, text.split())))
text = "おきなわの ろくがつ にじゅうさんにち は いれいのひで がっこうは やすみです"
print(typoglycemia(text))
