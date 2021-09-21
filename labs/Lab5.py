import random
random_num=random.randint(1,10)

print('Try to guess the number I am thinking of. Please enter a number between 1 and 10:')

while True:
    try:
        user_number = int(input())

        while user_number < 1 or user_number > 10:
            print("Your number is not between 1 and 10, try again:")
            user_number = int(input())

        while user_number != random_num:
            if user_number < random_num:
                print('Your number was too low, try again:')
                user_number = int(input())

            elif user_number > random_num:
                print("Your number was too high, try again:")
                user_number = int(input())

        break
    except ValueError:
        print('Something is not right. I am looking for a number that is an integer between 1 and 10. Try again:')


print('You guessed correctly! Good Job.')




