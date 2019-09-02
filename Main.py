from random import *

nouns = []
verbs = []
adjectives = []

for i in range (6):
    nounsInputted = input("Enter some nouns for this MadLibs exercise: ")
    nouns.append(nounsInputted)
    i+=1

print(nouns)

for j in range (7):
    verbsInputted = input("Enter some verbs: ")
    verbs.append(verbsInputted)
    j+=1

print(verbs)


for k in range (10):
    adjInputted = input("Enter some descriptive words: ")
    adjectives.append(adjInputted)
    k+=1

print(adjectives)
