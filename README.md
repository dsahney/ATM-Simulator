# ATM-Simulator

name_initial = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


question1 = "What is the first letter of your last name (in lowercase)?"

input(question1)

while input(question1) not in name_initial:
    print('Try again from the start.')

if input(question1) in name_initial:
    print("Thank you, let's begin the withdrawal process")
    # The while loop above can be replaced with an else statement below this print statement.

question2 = "How much money (in dollars) would you like?"

input(question2) # Allow the user to answer, telling us how much money they want.

if input(question2) > 1000.0:
    print("That is a lot of money, please talk to a bank teller before withdrawing this amount")

elif 0 < input(question2) <= 1000.0:
    print("Your request is being processed. Please pick up your money from the bottom of the machine")


else:
    print("You have entered an invalid amount, please try again")
    while input(question2) <= 0:
        input(question2)


import random

for variable in range(1):
    print("Thank you. Your withdrawal number is:", random.randint(1, 1000))

