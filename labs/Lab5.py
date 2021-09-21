import random
random_num=random.randint(1,10)

print('Try to guess the number I am thinking of. Please enter a number between 1 and 10:')

user_number = int(input())

while user_number != random_num:
    if random_num != user_number:
        print('Try again:')

        user_number = int(input())

print('You guessed correctly! Good Job.')




