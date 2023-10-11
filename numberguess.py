import random
random.randint(1,100)
number=random.randint(1,100)
guess=int(input("Enter your guess : ") )
if guess < number :
        print("Your guess is low.")
elif guess > number:
    print("Your guess is high.")
else:
      print("Your guess is correct.")
