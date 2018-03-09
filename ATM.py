# ATM Machine Simulator

import string

string.ascii_lowercase # string.ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'

name_initial = list(string.ascii_lowercase)

question1 = 'What is the first letter of your last name (in lowercase)?'

if input(question1) in name_initial:
    print('Thank you, let\'s begin the withdrawal process')

else:
    print('Try again from the start.')

question2 = 'How much money (in dollars) would you like?'

# Allow the user to answer, telling us how much money they want.

answer_q2 = float(input(question2))

if answer_q2 > 1000.0:
    print('That is a lot of money, please talk to a bank teller before withdrawing this amount')

elif 0 < answer_q2 <= 1000.0:
    print('Your request is being processed. Please pick up your money from the bottom of the machine')

    import random

    for variable in range(1):
    
        print('Thank you. Your withdrawal number is:', random.randint(1, 1000))

else:
    print('You have entered an invalid amount, please try again until you enter a valid amount.')
    while answer_q2 <= 0:
        input(question2)
