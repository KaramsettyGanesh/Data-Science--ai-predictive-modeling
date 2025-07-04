import random
print("Welcome to the My Python  World!")
print("Welcome to the Number Guessing Game!")
a=random.randint(1,100)
while True:
    Guess=int(input("Enter the Your Guess number:"))
    if Guess < a:
        print("It is very low number:")
    elif Guess > a:
        print("It is very high number:")
    else:
        print("you have Successfully Guessed the Random number Congratulations")
        break
