import random

answer = ''
count = 0
optional_count = 0
input_optional_count = ''
inputed = False
while True:
    answer = input('Roll the dice? (y/n): ').lower()
    if answer == 'y' and not inputed:
        input_optional_count = input('Would you like to roll the dice a specific number of times? (y/n): ')
        inputed = True
        if input_optional_count == 'y':
            optional_count = int(input('Enter the number of times: '))
    if answer == 'n':
        break
    elif answer == 'y':
        
        number1 = random.randint(1, 7)
        number2 = random.randint(1, 7)
        result = [number1, number2]
        print(result)
        count += 1
        print(f'You have rolled {count} times')
        if count == optional_count:
            break
    else:
        print('Invalid')






