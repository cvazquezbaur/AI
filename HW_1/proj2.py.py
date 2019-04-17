'''
Class: CPSC427
Team Member: Carlos Andres Vazquez Baur
Submitted by: Carlos Andres Vazquez BAur
GU username: cvazquezbaur
file name: proj2.py
program: illustrates basic python skills
to run: python proj2.py
'''

import re
import string

def tokenize(theText):

    good_chars = [chr(value) for value in range(ord('A'),ord('Z') + 1)]
    print ("These are the good characters\n")
    print (good_chars)
    #for char in '-.,?!\n':
        #stringIn = stringIn.replace(char, ' ')
    ##good_chars.append(' ')
    words = re.split(r'\W+', theText)
    wordsUpper = [word.upper() for word in words]
    countDict = dict.fromkeys(good_chars,0)
    for word in wordsUpper:
    	length = len(word)
    	if (word [0] != c for c in string.punctuation):
    		if (word[length-1] != d for d in string.punctuation):
    			for char in good_chars:
    				if (char == word[0]):
    					countDict[word[0]++
    
    return countDict
    		
    
    
'''
pre: stringIn is a string being read in
post: returns a dictionary where the key is an element of stringIn
    and the value is the number of times it appears
'''
def frequencyTable(stringIn):
    countDict = {}
##    for char in '-.,\n':
##        stringIn = stringIn.replace(char, ' ')
    stringIn = stringIn.lower()
    wordList = stringIn.split()
    for word in wordList:
        if word in countDict:
            countDict[word] = countDict[word] + 1
        else:
            countDict[word] = 1
    
    return countDict


def openFile():
    print("What file do you want to tokenize?")
    while(True):
        fin = raw_input('Enter an input file name \n')
        try:
            fin = open(fin, 'rt')
            break
        except:
            print("Invalid file name, try again")
    return fin


def displayFrequency(dictionaryCount):
    for entry in dictionaryCount:
    	print entry, dictionaryCount[entry]

def main():
    fin = openFile()
    theBook = fin.read()
    fin.close()
    countedDictionary = tokenize(theBook)
    displayFrequency(countedDictionary)

main()
