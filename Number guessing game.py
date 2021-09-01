import random

top_of_range = input("Enter the Highest Number for Range: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please enter a number greater than 0 next time")
        quit()
else :
    print("Please enter a number next time")
    quit()

random_number = random.randint(1, top_of_range)
guesses = 0
print(random_number)
while True:
    guesses += 1
    guess = input("Make a Guess: ")
    
    if guess.isdigit():
        guess = int(guess)
        if guess <= 0:
            print("Please enter a number greater than 0 next time")
            quit()
    else :
        print("Please enter a number next time")
        quit()

    if guess == random_number:
        print("Hurrah :)")
        break
    elif guess < random_number:
        print("You were below the Number")
    elif guess > random_number:
        print("You were above the Number")

print("You got it in",guesses ,"guesses")