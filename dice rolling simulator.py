import random
while True:
    roll=input('do you want to roll the dice?(yes/no)')

    if roll=="yes":
        number=random.randint(1,6)
        print('you rolled:',number)

    elif roll=="no":
        print('thanks for playing:')
        break
    else:
        print('please enter yes or no:')    
