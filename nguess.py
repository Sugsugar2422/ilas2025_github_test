import random

answer = random.randint(1, 100)
flag = True

while flag:
    guess = int(input('guess='))
    print('Your guess is', guess)
    if guess == answer :
        print('Good guess')
        flag = False
    elif guess < answer:
        print('Too low')
    else:
        print('Too high')