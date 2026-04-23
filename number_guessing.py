import random

num= random.randint(1, 100)
tries = 3

print("Guess the number between 1 and 100")
print("You have 3 tries!")

while tries > 0:
    guess = int(input("Enter your guess: "))

    difference = abs(num - guess)

    if guess == num:
        print("Correct! You win!")
        break
    
    elif difference <= 15:
        print("You're close")
    else:
        print("You're far")

    tries -= 1
    print("Tries left:", tries)

if tries == 0 and guess != num:
    print("Game over! The number was:", num)

