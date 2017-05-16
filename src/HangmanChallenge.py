'''
Created on Oct 24, 2015

@author: carlylevi
'''

import random

def loadWords(filename):
    allwords = []
    f = open(filename)
    for line in f:
        line = line.strip()
        allwords.append(line)
    f.close()
    return allwords
#read words from specified file and return a list of strings, each string is one line of the file    
     
def getWords(allwords,wordlength):
    wlist = [w for w in allwords if len(w) == wordlength]
    return wlist

#returns a list of words having a specified length from allwords

def display(guess):
    return ' '.join(guess)
#create a string from list guess to print/show user

def makeSecretList(secret):
    guess = []
    for ch in secret:
        if ch.isalpha() == True:
           guess.append("_") 
        else:
            guess.append(ch)
    return guess
#Create the list that's modificable to track letters guessed by user

def doGame(word):
    guess = makeSecretList(word)
    misses = 0
    guesses = 0
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    while True:
        if guess.count('_') == 0:
            break
        if misses == 8:
            break
        
        print "secret so far:",display(guess)
        letter = raw_input("guess a letter: ")
        
        if letter not in letters:
            print "you've already guessed this letter"
            misses = misses
            guesses = guesses
        else:
            dex = letters.index(letter)
            del letters[dex]
            print "These are the letters you haven't guessed:", letters
            guesses += 1
        print "guesses = ", guesses
        
        for index in range(len(word)):
            if word[index].lower() == letter.lower():
                guess[index] = word[index]
        if letter not in guess:
            misses += 1
        print "number of misses = ", misses
        
    if guess.count("_") == 0:
        print "word is guessed!",word
    else:
        print "you lost! word is",word
 
def play(allwords):
    wlen = int(raw_input("how many letters in song you'll guess? "))
    words = getWords(allwords,wlen)    
    word = random.choice(words)
    doGame(word)

if __name__ == '__main__':
    allwords = loadWords("songs.txt")
    play(allwords)
