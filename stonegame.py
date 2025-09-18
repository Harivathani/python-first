import random
print("Welcome to stone paper scissors")
possibilities=['stone','paper','scissors']
user=input("Enter your turn (stone/paper/scissors):").lower()
computer=random.choice(possibilities)
print(f"{computer}: chosen by computer")
if user == computer:
    print("The game is draw")
elif (user == "stone" and computer == "scissors") or (user == "paper" and computer == "stone") or (user == "scissors" and computer == "paper"):
    print("you won the game")
else:
    print("computer won")