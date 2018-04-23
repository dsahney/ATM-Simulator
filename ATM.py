print('Hello, welcome to Dhruv\'s Bank.\n Let us begin.')

import string
import random

string.ascii_lowercase # string.ascisi_lowercase = 'abcdefghijklmnopqrstuvwxyz'
name_initial = list(string.ascii_lowercase)

name_prompt = 'Please type your name:'
money_prompt = 'Please type the amount (in dollars) you would like:'
yes_no_prompt = 'Would you like to withdraw an amount of $1000 or less? Please type yes or no:'

def request_processor(x):
    if x == 'process request':
        print('Your request is being processed. Please pick up your money from the bottom of the machine.')
        for variable in range(1):
            print('Thank you. Your withdrawal number is:', random.randint(1, 1000))
            # break ?

print('Welcome,', input(name_prompt),'.')

answer_money_amount = float(input(money_amount))

if 0 < answer_money_amount <= 1000.0:
    request_processor('process request')
    
elif answer_money_amount > 1000.0:
    print('That is a lot of money, please talk to a bank teller for such a withdrawal.')
    answer_yes_no = input(yes_no_prompt)
    if answer_yes_no == 'yes':
        while not 0 < answer_money_amount <= 1000:
            print('Please try again.')
            answer_money_amount = float(input(money_amount))
        if 0 < answer_money_amount <= 1000:
            request_processor('process request') 
        else:
            print('Please try again')
    elif answer_yes_no == 'no':
        print('Thank you, we are sorry we cannot accomodate withdrawals over $1000')
    else:
        print('You have not entered a valid value, good bye.')
        answer_yes_no
        
else:
    while answer_money_amount <= 0:
        print('You have entered an invalid amount, please try again until you enter a valid amount.')
        answer_money_amount = float(input(money_amount))
        if 0 < answer_money_amount <= 1000:
            request_processor('process request') 
        elif answer_money_amount > 1000:
            print('That is a lot of money, please talk to a bank teller for such a withdrawal.')
            yes_no_prompt = 'Would you like to withdraw an amount of $1000 or less? Please answer: "yes" or "no".'
            answer_yes_no = input(yes_no_prompt)
            if answer_yes_no == 'yes':
                while not 0 < answer_money_amount <= 1000:
                    print('Please try again.')
                    answer_money_amount = float(input(money_amount))
                if 0 < answer_money_amount <= 1000:
                    request_processor('process request') 
            elif answer_yes_no == 'no':
                print('Thank you, we are sorry we cannot accomodate withdrawals over $1000')
            else:
                print('You have not entered a valid value, good bye.')
                answer_yes_no
        else:
            print('Try again')
