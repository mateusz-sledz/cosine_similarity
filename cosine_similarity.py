from collections import Counter
from math import sqrt


sen1 = input("Type first sentence:")

sen2 = input("Type second sentence:")

def cosine_similarity(sen1, sen2):
    sen1 = sen1.lower()
    sen1 = sen1.translate({ord(i): None for i in '.,!?;-'})

    sen2 = sen2.lower()
    sen2 = sen2.translate({ord(i): None for i in '.,!?;-'})

    words1 = sen1.split()
    words2 = sen2.split()
    
    counter1 = Counter(words1)
    counter2 = Counter(words2)
    
    allwords = tuple(set.union(set(words1), set(words2)))
    
    vector1, vector2 = [], []
    
    for word in allwords:
        vector1.append(counter1[word])
        vector2.append(counter2[word])
    
    sumAB = 0
    sumAsqr = 0
    sumBsqr = 0
    
    for a, b in zip(vector1, vector2):
        sumAB += a*b
        sumAsqr += a*a
        sumBsqr += b*b
    
    print("\nCosine similarity of sentences equals", sumAB/(sqrt(sumAsqr)*sqrt(sumBsqr)))


cosine_similarity(sen1, sen2)