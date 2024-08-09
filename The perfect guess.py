import random
n = random.randint(1,100)

a = -1
guess = 0
while(a != n):
    a = int(input("Guess a number: "))
    if(a>n):
        print("Lower number plese")
    elif(a<n):
        print("Higher number plese")
    guess += 1

print(f"You have gussed the number correctly in {guess} attempt")