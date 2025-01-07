import random
def guess_number():
    number=random.randint(1,100)
    attempts=0
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess=int(input("Enter your guess: "))
        attempts+=1
        if guess<number:
            print("Too low! Try again.")
        elif guess>number:
            print("Too High! Try again.")
        else:
            print(f"Correct! You guessed the number in {attempts}attempts.")
            break
if __name__ == "__main__":
    guess_number()   