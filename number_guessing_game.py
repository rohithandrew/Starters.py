from random import randint

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty, Type 'easy' or 'hard': ")

def game(iterate:int):
    answer = randint(1, 100)
    attempts = iterate
    print(f"You have {attempts} attempts to guess the number")
    for i in range(iterate):
        num = int(input("Make a guess: "))
        if num == answer:
            print("Congrats,You have Won!!!")
            break
        elif num < answer:
            print("your guess is less than the answer")
            attempts -= 1
        elif num > answer:
            print("your guess is greater than the answer")
            attempts -= 1
        print(f"You have {attempts} attempts left")

    if attempts == 0:
        print("You have lost")

if difficulty == 'easy':
    game(10)
elif difficulty == 'hard':
    game(5)
