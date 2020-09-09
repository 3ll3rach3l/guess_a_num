from random import randint
print("what's your name?")
player_name = input()

secret_num = randint(1, 20)
guesses_taken = 0

input("Pick a number between 1 and 20")

while guesses_taken < 6:
    guess = int(input("Shoot your shot"))
    if guess < secret_num:
        guesses_taken += 1
        print("Your guess is too low! Try again.")
    elif guess > secret_num:
        guesses_taken += 1
        print("Your guess is too high.")
    elif guess == secret_num:
        break
if guess == secret_num:
    print('Good job {player_name}! You guessed the number in {guesses_taken} guesses!')
else:
    print('Sorry, {player_name}. You could not guess my number {secret_num}.')
