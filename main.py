import random

print("Welcome to hangman")
print("-------------------------")

wordDictionary = ["random", "house", "diamond", "hello", "howdy", "piece", "cake"]

# choose a random word
randomWord = random.choice(wordDictionary)

for x in randomWord:
  print("_", end=" ")
  
def printHangman(wrong):
  if(wrong == 0):
    print("\n+---+")
    print("    |")
    print("    |")
    print("    |")
    print("   ===")
  elif(wrong == 1):
    print("\n+---+")
    print("O   |")
    print("    |")
    print("    |")
    print("   ===")
  elif(wrong == 2):
    print("\n+---+")
    print("O   |")
    print("|   |")
    print("    |")
    print("   ===")
  elif(wrong == 3):
    print("\n+---+")
    print(" O  |")
    print("/|  |")
    print("    |")
    print("   ===")
  elif(wrong == 4):
    print("\n+---+")
    print(" O  |")
    print("/|\ |")
    print("    |")
    print("   ===")
  elif(wrong == 5):
    print("\n+---+")
    print(" O  |")
    print("/|\ |")
    print("/   |")
    print("   ===")
  elif(wrong == 6):
    print("\n+---+")
    print(" O  |")
    print("/|\ |")
    print("/ \ |")
    print("   ===")
    
def printWord(guessedLetters):
  counter=0
  rightLetters=0
  for char in randomWord:
    if(char in guessedLetters):
      print(randomWord[counter], end=" ")
      rightLetters+=1
    else:
      print(" ", end=" ")
    counter+=1
  return rightLetters

def printLines():
  print("\r")
  for char in randomWord:
    print("\u203E", end=" ")
    
lengthWordGuessed = len(randomWord)
amountTimesWrong = 0
currentIndexGuessed = 0
currentLettersGuessed = []
currentLettersRight = 0

while(amountTimesWrong != 6 and currentLettersRight != lengthWordGuessed):
  print("\nLetters guessed so far: ")
  for letter in currentLettersGuessed:
    print(letter, end=" ")
  #Prompt user for input
  letterGuessed = input("\nGuess a letter: ")
  #User is right
  if(randomWord[currentIndexGuessed] == letterGuessed):
    printHangman(amountTimesWrong)
    #Print word
    currentIndexGuessed+=1
    currentLettersGuessed.append(letterGuessed)
    currentLettersRight = printWord(currentLettersGuessed)
    printLines()
  #User is wrong
  else:
    amountTimesWrong+=1
    currentLettersGuessed.append(letterGuessed)
    #Update the drawing
    printHangman(amountTimesWrong)
    #Print word
    currentLettersRight = printWord(currentLettersGuessed)
    printLines()
      
print("Game is over")