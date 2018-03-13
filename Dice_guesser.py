import random

dice_result = random.randint(1, 6)

question1 = 'Hello, please guess what number has been rolled by the die. Note that a die has six sides and therefore can land on either 1, 2, 3, 4, 5, or 6.'

tries = 0
while int(input(question1)) != dice_result:
    print('Please try again.')
    tries += 1

if int(input(question1)) == dice_result:
    print('Congratulations! You have correctly guessed the side the die has landed on. It took you', tries, 'to guess the correct answer.')


