#Guess the Number Program 
import random

def random_number():
    r_start = int(input('Choose your start point: '))
    r_end = int(input('choose your end point: '))
    the_random = random.randint(r_start, r_end)
    number_of_tries = 0
    while True:
        x = int(input('Guess the random number: '))
        if x > the_random:
            number_of_tries += 1
            print('Your guess is greater than the random')
        elif x < the_random:
            number_of_tries += 1
            print('Your guess is less than the random')
        elif x == the_random:
            print('You are correct')
            break
    number_range = r_end - r_start
    print(f'It took you {number_of_tries} number of tries to guess a range of {number_range} numbers')

random_number()

