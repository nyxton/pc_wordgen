# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

import random

wantedWords = 10000

consanants = "bcdfghjklmnpqrstvwxz"
vowels = "aeiouy"

wordlist = ""

def makeWord(syllables):
    global wordlist
    word = ""
    s = 0
    while s < syllables:
        if(s == 0):
            word += random.choice(consanants).capitalize()
        else:
            word += random.choice(consanants)

        word += random.choice(vowels)
        if random.randint(0, 3) == 0:
            word += random.choice(vowels)
        s = s + 1
    
    wordlist += (f'{word}\n')

w = 0
while w < wantedWords:
    rand = random.randint(2, 4)
    makeWord(rand)
    w = w + 1

with open('wordlist.txt', 'a') as f:
    f.write(wordlist)
    f.close()