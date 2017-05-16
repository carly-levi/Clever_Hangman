'''
Created on Oct 25, 2015

@author: carlylevi
'''

import random
from encore.storage.tests.static_url_store_test import count


def getWords():
    f = open("kwords5.txt")
    st = f.read()
    words = st.split()
    #error checking
    for w in words:
        if len(w) != 5:
            print "error:",w
    return words

def loadWords(filename):
    global words
    f = open(filename).read().split()
    global wordlist
    wordlist = [i for i in f]
    words = wordlist

def startGame():
    global wordlist
    global count
    count = 0
    global words
    
def getGuess():
    global words
    global count
    count +=1
    return random.choice(words)

def guessCount():
    global count
    return count

def common(a,b):
    """
    Returns number of letters in common between given strings a and b,
    no matter where those letters occur within the strings
    """
    alist = list(a)
    blist = list(b)
    for c in alist:
        if c in blist:
            blist[blist.index(c)] = '*'
    return blist.count("*")

def play(words):
    print "Jotto: Think of a five-letter word, I'll guess your word"
    print "enter number of letters in common, 6 if correct word"
    
    while True:
  
        guess = random.choice(words)
 
        print "I'm considering",len(words),"different words"
        print "my guess:",guess
        same = raw_input("how many in common (6 if word guessed)? ")
        sameInt = int(same)
        if sameInt == 6:
            print "I win!!"
            break
        words = [w for w in words if common(w, guess) == sameInt]
        
    print "thank you for playing Duke Jotto"
    
def processCommon(guess,count):
    global words
    words = [w for w in words if common(w, guess) == count]
    return len(words)
    words.remove(guess)

if __name__ == '__main__':
    words = getWords()
    print "read",len(words),"words"
    play(words)
