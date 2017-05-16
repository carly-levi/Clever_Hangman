'''
Created on Nov 15, 2015

@author: carlylevi
'''

import random
from __builtin__ import dict

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
    return ['_']*len(secret)
#Create the list that's modificable to track letters guessed by user

def categorize(words, guess):
    dict = {}
    for word in words:
        lst = list(word)
        for i in range(len(lst)):
            if lst[i] != guess:
                lst[i] = "_"
            w = "".join(lst)
        if w not in dict:
            dict[w] = [word]
        else:
            dict[w].append(word)
    return dict
#Creates template dictionary so that You can compare each possible word to the template and the letter guessed by the user

def value(dictionary):    
    max = 0
    words = []
    for i in dictionary.values():
        if len(i) > max:
            max = len(i)
            words = i
    return words      
#Finds the key in the dictionary created by categorize that has the largest number of corresponding words

def doGame(word, words):
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
        
        dict = categorize(words, letter) #calls the dictionary created from categorize
        words = value(dict)
        word = random.choice(words) #picks a new word each time a letter is guessed
        
        if typ == "test": #Creates the corresponding displays for test mode
            tdict = {}
            for i in dict:
                if i not in tdict:
                    tdict[i] = len(dict[i])
            print "The dictionary of categories is:", tdict
            print "The secret word is:", word
            
        if letter not in letters:
            print "you've already guessed this letter"
            misses = misses
            guesses = guesses
        else:
            dex = letters.index(letter)
            del letters[dex]
            print "These are the letters you haven't guessed:", ''.join(letters)
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
    
    #Plays the hangman game

        
 
def play(allwords):
    wlen = int(raw_input("how many letters in word you'll guess? (at least 3) ")) #Allows the user to choose the number of letters in the word they want to guess
    global typ
    typ = raw_input("Which game type would you like? (test or play) ") #Lets the user choose which mode to play the game in
    words = getWords(allwords,wlen)    
    word = random.choice(words)
    doGame(word, words)

if __name__ == '__main__':
    allwords = loadWords("lowerwords.txt")
    play(allwords)
    
