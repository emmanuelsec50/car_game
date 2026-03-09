command = ''
start = False
speed = 0
began = False
max_speed = 200
fuel = 200
max_fuel = 200
full = True
print('''
> help -To display commands
> start - To start the car
> stop - To stop the car
> quit - To exit
> acc - To accelerate your car
> dec - To decelerate your car
> speed - To display your speed
> refill - To refill your tank
> fuel - To display your remaining fuel capacity
''')
while True:
    if  not full:
        if start:
            print('Car has stopped since fuel is depleted')
            began = False
            start = False
    command = input('> ').lower()
    if fuel > 0:
        full = True
    elif fuel == 0:
        full = False
    if fuel <= 0:
        start = False
        began = False
        full = False
    
        # starting
    if command == 'start':
        if fuel <= 0:
            start = False
            began = False
            full = False
        if start and full:
            print('Car is already started')
        elif not start and full:
            fuel -= 1
            began = False
            speed = 0
            print(f'Car started!')
            start = True
            if fuel <= 0:
                start = False
                began = False
                full = False
        elif not full:
            print('Please refill your car!')
            # stopping
    elif command == 'stop':
        if start:
            if speed > 0:
                print(f'Car is stopped from {speed}')
            else:
                print('Car is already stopped!')
            start = False
            speed = 0
        elif not start:
            print('Car is not started yet!')
#   accellerate      
    elif command == 'acc':
        if start and full:
            if fuel <= 0:
                start = False
                began = False
                full = False
            began = True
            if speed == 200:
                print(f'You have reached the speed limit of {speed}')
            elif speed >= 180:
                print(f'You approaching a speed limit of {max_speed}')
                speed = speed + 10
                fuel = fuel - 20
                print(f'Speed increased to {speed}')
                if fuel <= 0:
                    start = False
                    began = False
                    full = False
            elif speed >= 0:
                speed = speed + 10
                print(f'Speed increased to {speed}')
                fuel = fuel - 20
                if fuel <= 0:
                    start = False
                    began = False
                    full = False
                
                            
        elif not start:
            print('Car is not started yet')
            # speed
    elif command == 'speed':
        if start and not began:
            print(f'You have not accelerated yet!')
        elif not start:
            print('Car is not started!')
        elif start:
            print(f'your speed is {speed} km/hr')
            # deccelerate
    elif command == 'dec':
        if fuel <= 0:
            start = False
            began = False
            full = False
        if speed > 0:    
            if start and full:
                speed = speed - 10
                fuel = fuel - 5
                
                if speed == 0:
                    start = False
                    began = False
                    print('Your car has stopped!')
                    
                elif speed < 0:
                    speed = 0
                    print('Car cannot be in a negative speed')
                else:
                    print(f'Your speed has decreased to {speed} km/hr')
            elif not start:
                print('Car is not started!')
        elif speed == 0:
            if not start:
                print('Car has not accelerated')
            elif start:
                print("You have'nt accelerated yet!")
             
            # refill
    elif command == 'refill':
        if fuel ==  max_fuel:
            print('Fuel is already full!')
        elif fuel < max_fuel:
            fuel = max_fuel
            print('Your tank has been refilled')
            # fuelling
    elif command == 'fuel':
        print(fuel)

        # help
    elif command == 'help':
        print('''
> help -To display commands
> start - To start the car
> stop - To stop the car
> quit - To exit
> acc - To accelerate your car
> dec - To decelerate your car
> speed - To display your speed
> refill - To refill your tank
> fuel - To display your remaining fuel capacity
''')

        
    elif command == 'quit':
        break
    
    else:
        print('Not recognized!')
    
