# Word Jumble0
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random

# create a sequence of words to choose from
WORDS = ("python", "jumble",'diyam','computer', "binary", "network", "application", "programming")


print(
"""
           Welcome to Word Jumble!

   Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
"""
)


play=input("Do you want to play? (yes or no)")
while play=="yes":
    # pick one word randomly from the sequence
    word = random.choice(WORDS)
    # create a variable to use later to see if the guess is correct
    correct = word

    # create a jumbled version of the word
    jumble =""
    while word:
        position = random.randrange(len(word))
        jumble += word[position]
        word = word[:position] + word[(position + 1):]


    print("The jumble is:", jumble)
    guess = input("\nYour guess: ")
    if guess != correct and guess != "":
        print("Sorry, that's not it.")
        
        # giving the hint for those who don`t know
        
        hint=input("Do you need a hint?")
        if hint=="yes":
            if correct=="python":
                print("Its a snake...")
            elif correct=="jumble":
                print("Rhymes with rumble")
            elif correct== "binary":
                print("it is a type of language..")
            elif correct=="network":
                print("we can`t talk on mobile without this...")
            elif correct=="diyam":
                print("it`s me ...")
            elif correct=="computer":
                print("This is a device")
            elif correct=="application":
                print("this is app.")
            elif correct=="programming":
                print("you can code any program.if your ____________ skill is good...")
            print("\n","Thanks for taking the hint...")
        guess = input("\n""Your guess: ")
        if guess != correct and guess != "":
            
        # if user again give incorrect answer then he receive the next jumble
            
            print("\n""Better luck next time..\n Try this one.. ""\n")

    # if user is correct
    
    if guess == correct:
        print("\n""That's it!  You guessed it!")
        print("You won 10000 rs. cash prize.\n your money will transfered in your bank account soon .""\n")
        play=input("Do you want to play again? (yes or no)")
    elif guess== "":
        print("You failed...")
        play=input("Do you want to play again? (yes or no)")

# At the end

print("\n""Thanks for playing.""\n"'#dmt')

input("\n\nPress the enter key to exit.")


                                                                           #dmt
 
