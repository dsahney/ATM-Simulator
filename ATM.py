print('Hello, welcome to "Guess the Number"!')
import string
import random

string.ascii_lowercase # string.ascisi_lowercase = 'abcdefghijklmnopqrstuvwxyz'
name_initial = list(string.ascii_lowercase)
question1 = 'Please type your name:'
question2 = 'Please type the amount (in dollars) you would like:'
question3 = 'Would you like to withdraw an amount of $1000 or less? Please type yes or no:'

def function1a(x):
    if x == 'prompt1a':
        print('Your request is being processed. Please pick up your money from the bottom of the machine.')
        for variable in range(1):
            print('Thank you. Your withdrawal number is:', random.randint(1, 1000))

def function1b(x):
    if x == 'prompt1b':
        print('Your request is being processed. Please pick up your money from the bottom of the machine.')
        for variable in range(1):
            print('Thank you. Your withdrawal number is:', random.randint(1, 1000))
            break

print('Welcome,', input(question1),'.')
    
answer_q2 = float(input(question2))

if 0 < answer_q2 <= 1000.0:
    function1a('prompt1a') 
elif answer_q2 > 1000.0:
    print('That is a lot of money, please talk to a bank teller for such a withdrawal.')
    answer_q3 = input(question3)
    if answer_q3 == 'yes':
        while not 0 < answer_q2 <= 1000:
            print('Please try again.')
            answer_q2 = float(input(question2))
        if 0 < answer_q2 <= 1000:
            function1b('prompt1b') 
        else:
            print('Please try again')
    elif answer_q3 == 'no':
        print('Thank you, we are sorry we cannot accomodate withdrawals over $1000')
    else:
        print('You have not entered a valid value, good bye.')
        answer_q3
else:
    while answer_q2 <= 0:
        print('You have entered an invalid amount, please try again until you enter a valid amount.')
        answer_q2 = float(input(question2))
        if 0 < answer_q2 <= 1000:
            function1b('prompt1b') 
        elif answer_q2 > 1000:
            print('That is a lot of money, please talk to a bank teller for such a withdrawal.')
            question3 = 'Would you like to withdraw an amount of $1000 or less? Please answer: "yes" or "no".'
            answer_q3 = input(question3)
            if answer_q3 == 'yes':
                while not 0 < answer_q2 <= 1000:
                    print('Please try again.')
                    answer_q2 = float(input(question2))
                if 0 < answer_q2 <= 1000:
                    function1b('prompt1b') 
            elif answer_q3 == 'no':
                print('Thank you, we are sorry we cannot accomodate withdrawals over $1000')
            else:
                print('You have not entered a valid value, good bye.')
                answer_q3
        else:
            print('Try again')
