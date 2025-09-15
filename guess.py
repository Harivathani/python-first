import random
'''def guessing(x):
    number=random.randint(1,x)
    guess=0
    while number!=guess:
        guess=int(input("Enter a guessing number:"))
        if guess<number:
            print("your guess is low")
        elif guess>number:
            print("Your guess is high")
        else:
            print("your guess is correct")
guessing(15)'''

number=random.randint(1,10)
guess=0
while number!=guess:
    guess=int(input("Enter a guessing number:"))
    if guess<number:
        print("your guess is low")
    elif guess>number:
        print("Your guess is high")
    else:
        print("your guess is correct")