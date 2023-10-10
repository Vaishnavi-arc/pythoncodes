import random
random.randint(1,100)
number=random.randint(1,100)
guess=int(input("Enter your guess : ") )
counter =1
while guess!=number:
    if guess < number :
        print("Guess Higher.")
    else:
        print("Guess Lower.")
    guess=int(input("Enter your guess : ") )
    counter=counter+1

print("you won")
print("you took",counter,"attemps.")