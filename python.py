command = ''
start = False
print('''
> help -To display commands
> start - To start the car
> stop - To stop the car
> quite - To exit
> acc - To accelerate your car
> dec - To decelerate your car
> speed - To display your speed
''')
while True:
    
    command = input('> ').lower()
    if command == 'start':
        if start:
            print('Car is already started')
        elif not start:
            began = False
            speed = 0
            print(f'Car started!')
            start = True
    elif command == 'stop':
        if start:
            print('Car is stopped!')
            start = False
            speed = 0
        elif not start:
            print('Car is alredy stationary!')
    elif command == 'acc':
        if start:
            began = True
            speed = speed + 10
            print(f'speed increased to {speed} km/hr!')
        elif not start:
            print('Car is stopped')
    elif command == 'speed':
        if start and not began:
            print(f'You have not accelerated yet!')
        elif not start:
            print('Car is not started!')
        elif start:
            print(f'your speed is {speed} km/hr')
    elif command == 'dec':
        if start:
            speed = speed - 10
            print(f'Your speed has decreased to {speed} km/hr')
            if speed == 0:
                start = False
                print('Your car has stopped!')
        elif not start:
            print('Car is not started!')
    elif command == help:
        print('''
> help -To display commands
> start - To start the car
> stop - To stop the car
> quite - To exit
> acc - To accelerate your car
> dec - To decelerate your car
> speed - To display your speed
''')

        
    elif command == 'quit':
        break
    else:
        print('Not recognized!')
    


