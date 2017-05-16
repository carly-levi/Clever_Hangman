
'''
Created on Oct 6, 2015

@author: ola
'''
import random

def getWords():
    f = open("kwords5.txt")
    st = f.read()
    words = st.split()
    #error checking
    for w in words:
        if len(w) != 5:
            print "error:",w
    return words

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

if __name__ == '__main__':
    words = getWords()
    print "read",len(words),"words"
    play(words)
