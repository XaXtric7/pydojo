import random
n = random.randint(1, 100)
a = 0
guesses = 0
while (a != n):
    guesses += 1
    a = int(input("Guess the number: "))
    if (a > n):
        print("Guess a lower number please!")
    else:
        print("Guess a higher number please!")
print(f"You have guessed {n} correctly in {guesses} attempts.")
