from random import *

def secret_list(max_range): #Generates 5 random numbers
    secret_list = []
    for i in range(5):
        secret_list.append(randint(1,max_range))
    return secret_list

mastermind_list = secret_list(6)
print(mastermind_list)

print("Start")

correct = 0
tries = 0

while correct < 5 : #User attempt
    guess1 = int(input("Guess the first number : "))
    guess2 = int(input("Guess the second number : "))
    guess3 = int(input("Guess the third number : "))
    guess4 = int(input("Guess the fourth number : "))
    guess5 = int(input("Guess the fifth number : "))
    tries += 1 #Test counter

#Count the number of fair value
    if guess1 == mastermind_list[0]:
        correct += 1
    if guess2 == mastermind_list[1]:
        correct += 1
    if guess3 == mastermind_list[2]:
        correct += 1
    if guess4 == mastermind_list[3]:
        correct += 1
    if guess5 == mastermind_list[4]:
        correct += 1
    
    if correct < 5 : #Correct number of values
        correct == 1
        print("Guessed",str(correct),"number correctly.")
        correct = 0
    else :
        if tries == 1 :
            print("You won in",str(tries),"try.")
        else :
            print("You won in",str(tries),"tries.")  