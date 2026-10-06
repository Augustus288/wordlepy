import time
from pathlib import Path
import random
import os

fiveWords=Path(__file__).parent / "5words.txt"
wordList=[]
with open(fiveWords,'r') as f:
    wordList=f.read().upper().split('\n')

resultStore=[]
result=''
notInWord=''
lastGuesses=[]
word=wordList[random.randint(0,len(wordList)-1)].upper()
os.system('clear')
while True:
    if len(resultStore)==5:
        print(f"Game over! You couldn't guess in time...\nThe word was {word}!")
        break

    print("█: Letter is in word and in right order")
    print("▒: Letter is in word")
    print("░: Letter not in word\n")
    print(f"Characters not in word:{notInWord} \n")

    for resulI in range(len(resultStore)):
        print(lastGuesses[resulI])
        print(resultStore[resulI])

    guess = input("Add a 5 letters guess word: ").upper()
    while True:
        if len(guess)!=5:
            print("Not 5 letters, try again.")
        elif not (guess in wordList):
            print("Guessed is not recognized as a word.")
        else:
            break
        guess = input("Add a 5 letters word guess word: ").upper()

    for i,v in enumerate(guess):
        if v in word:
            if v==word[i]:
                result+='█'
            else:
                result+='▒'
        else:
            result+='░'
            if v not in notInWord:
                notInWord+=v
    resultStore.append(result)
    lastGuesses.append(guess)
    result=''
    os.system('clear')