import random

with open('sowpods.txt') as f:
    words = list(f)

secret = random.choice(words).strip().lower()

print("Welcome to Hangman!")

arr = ["_"] * len(secret)

print(" ".join(arr))

guesses = 6

while "_" in arr:
    letter = raw_input("Guess your letter: ")
    if letter in secret:
        for i in range(len(arr)):
            if secret[i] != letter:
                continue
            else:
                arr[i] = letter
        print(" ".join(arr))
    else:
        guesses -= 1
        if guesses == 0:
            break
        print("Incorrect! You have %s chances left" %guesses)



if guesses > 0:
    print("You Win!")
else:
    print("You lose! Your word is {}".format(secret))
