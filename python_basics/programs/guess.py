import random

prize = random.randint(1,100)

guess = int(input("enter a number to win a prize : "))
while prize!=guess:
    if guess<prize:
        print("guess higher\n")
        guess = int(input("enter a number to win a prize : "))
    elif guess>prize:
        print("guess lower\n")
        guess = int(input("enter a number to win a prize : "))
else:
    print("You win the prize")
print(prize,guess)