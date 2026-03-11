import random

chose = ''
choices = ('r', 'p', 's')
while True:
    chose = str(input('Rock, Paper, Scissors? (r/p/s): '))
    if chose not in choices:
        print('Invalid choice!')
        continue
    mynumber = random.randint(1,3)
    if mynumber == 1:
        computer = 'Computer chose Rock'
    elif mynumber == 2:
        computer = 'Computer chose paper'
    else:
        computer = 'Computer chose Scissors'
    if ((chose == 'r' and mynumber == 3) or (chose == 'p' and mynumber == 1) or (chose == 's' and mynumber == 2)):
        print(computer)
        print('You won')
    elif ((chose == 'r' and mynumber == 1) or (chose == 'p' and mynumber == 2) or (chose == 's' and mynumber == 3)):
        print('You had a tie')
    else:
        print(computer)
        print('You lose')
    print(mynumber)
    while True:
        wish = str(input('Would you like to continue? (y/n): '))
        if wish == 'n':
            break
        elif wish == 'y':
            pass
        else:
            print('Enter a valid input')





    
    
    
    
    
    
    
    

