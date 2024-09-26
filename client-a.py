import random
number = random.randint(1,10)

#print(number)
attempts = 1

while attempts <= 3:
    guess = int(input("Guess a number [1-10]: "))
    if guess == number:
        break
    else:
        print("Not it!")
    attempts += 1

if guess == number:
    print(f"You got it in {attempts} attempt(s)")
else:
    print("Better luck next time!") 