import random
print("lets play the guessing number system")
print("the Range is between 1 and 100")
user=int(input("Enter the secret number:"))
low=1
high=100
guess=0
while user!=guess:
    guess=random.randint(low,high)
    if guess<user:
        print(f"{guess} It is small")
        low=guess+1
    elif user<guess:
        print(f"{guess} It is large")
        high=guess-1
    else:
        print(f"{guess}Brilliant you are guess is correct")