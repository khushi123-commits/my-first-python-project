import random
choice=['rock','paper','scissors']

computer=random.choice(choice)
print('rock paper scissors game!!')
user=input('choose rock,paper,or scissors:').lower()

if user not in choice:
  print('invalid choice! please try again.')
else:
  print('you choose:',user)
  print('computer choose:',computer)
  if user==computer:
    print('its a draw!!')
  elif(
      (user=='rock'and computer=='scissors')
    or (user=='paper'and computer=='rock')
    or (user=='scissors'and computer=='paper')
    ):
       print('you win!!')
  else:
       print('computer win!!')