import random

target=random.randint(1,100)
while True:
    userchoice=int(input('enter the target:'))
    if (userchoice==target):
        print('success:correct guess!!')
        break
    elif(userchoice<target):
        print('your number was too small.take a bigger guess...')
    else:
        print('your number was too large.take a smaller guess...')

    print('----------GAME OVER-----------')    