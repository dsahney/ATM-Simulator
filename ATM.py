# ATM Machine Simulator
import string
import random

string.ascii_lowercase # string.ascisi_lowercase = 'abcdefghijklmnopqrstuvwxyz'
name_initial = list(string.ascii_lowercase)

question1 = 'What is the first letter of your last name (lowercase)?'

while input(question1) not in name_initial:
    print('Try again from the start.')
    
question2 = 'How much money (in dollars) would you like?'
answer_q2 = float(input(question2))

if 0 < answer_q2 <= 1000.0:
    print('Your request is being processed. Please pick up your money from the bottom of the machine')
    for variable in range(1):
        print('Thank you. Your withdrawal number is:', random.randint(1, 1000))
elif answer_q2 > 1000.0:
    print('That is a lot of money, please talk to a bank teller for such a withdrawal.')
    question3 = 'Would you like to withdraw an amount of $1000 or less? Please answer: "yes" or "no".'
    answer_q3 = input(question3)
    if answer_q3 == 'yes':
        input(question2)
    elif answer_q3 == 'no':
        print('Thank you, we are sorry we cannot accomodate withdrawals over $1000')
    else:
        print('Please provide a valid answer: "yes" or "no".')
        answer_q3
else:
    while float(input(question2)) <= 0:
        print('You have entered an invalid amount, please try again until you enter a valid amount.')        
