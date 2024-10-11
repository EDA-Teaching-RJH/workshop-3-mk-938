import random
secret_number = random.randint(1,10)
guess = 0
def guess():
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < secret_number:
        print ("too low")
        return True
    elif guess > secret_number:
        print ("too high")
        return True
    else: 
        print ("You guessed correctly!!")
        return False

while guess():
    guess()

        

