# https://stepik.org/lesson/316052/step/12?unit=301794

def process(sentences):
    result = []
    subresult = []
    for s in sentences:
        words = [word if word.isalpha() else None for word in s.split(' ')]
        for w in words:
            if w is not None:
                subresult.append(w)
        result.append(' '.join(subresult))
        subresult = []

    return result

s = ['1 thousand devils', 'My name is 9Pasha', 'Room #125 costs $100']

print(process(s))
