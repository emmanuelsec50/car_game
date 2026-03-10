import random



while True:
    try:
        desired_max_range = int(input('Input your desired maximum range value: '))
        desired_min_range = int(input('Input your desired minimum range value: '))
        secret_number = random.randint(desired_min_range, desired_max_range)
        count = 0
        if desired_min_range < desired_max_range:
            while True:
                try:
                    guessed_number = int(input(f'Guess number between ({desired_min_range} and {desired_max_range}): '))
                    if guessed_number >= desired_min_range and guessed_number <= desired_max_range:
                        count += 1
                        if secret_number == guessed_number:
                            print(f'Congratulations! You guessed the right number in {count} attempts!')
                            break
                        elif guessed_number > secret_number:
                            print('The guessed number is greater than the secret number!')
                        elif guessed_number < secret_number:
                            print('The guessed number is lesser than the secret number!')
                    else:
                        print(f'Please enter a number between {desired_min_range} and {desired_max_range}')
                except ValueError:
                    print('Please enter numerical values!')
        else:
            print('Please check your values again')
    except ValueError:
        print('Please enter numerical values!')
