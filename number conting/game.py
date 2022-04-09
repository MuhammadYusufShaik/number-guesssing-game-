import random
r=random.randint(1,10)
chances=3
while(chances>0):
    guess=int(input('Guess a number between 1 and 10:  '))
    if(guess==r):
        print('Correct!!!!YOU WON!!!')
        break
    else:
        print('Incorrect.Try Again')
    chances=chances-1
if(chances==0):
    print('You Lost.the correct number is ',r)    


         
    
