import random
number = random.randint(1,9)
chances = 5

if(chances < 6 & chances > 0):
    print("Number guessing game")
    guesses = input("Enter your guess : ")
    if(guesses == number):
        print("Congradulation You Won!!!")
    if(guesses < number):
        print("Your guess was too low ; Guess a number higher than ", guesses)
        guesses = input("Enter your guess : ")
        chances = chances-1
    if(guesses > number):
        print("Your guess was too high ; Guess a number lower than ", guesses)
        guesses = input("Enter your guess : ")
        chances = chances-1
if(chances == 0):
    print("YOU LOSE!!! The number is ", number)

