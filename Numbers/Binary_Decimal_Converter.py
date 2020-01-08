
def askForInt():
    decimal = ['d', 'D', 'decimal', 'Decimal']
    binary = ['b', 'B', 'binary', 'Binary']
    direction = 'empty'
    n = 'empty'

    # This loop gets the direction of the conversion
    while True:
        direction = input('What kind of number you want to convert to? Binary or Decimal?')
        if direction in decimal:
            print('You chose to convert from binary to decimal')
            break
        elif direction in binary:
            print('You choose to convert from decimal to binary')
            break
        else:
            print('This is not a valid input. \n '
                  'Valid inputs are:\n' + str(binary) + '\n' + str(decimal))

    # This loop gets the actual number to convert and
    # if the number has to be binary checks that it is
    while True:
        try:
            n = int(input('Please, type a number (int) to translate:'))

            i = n
            if direction in decimal:
                while i % 10 == 0 or i % 10 == 1:
                    i = i // 10  # We move to the next digit check

            if i == 0:
                break
            else:
                print('enter an binary number pls')
                continue

        except ValueError:
            print('''This is not an Int''')

    return [n, direction]


def converterFunction(x):
    n = x[0]
    direction = x[1]
    decimal = ['d', 'D', 'decimal', 'Decimal']
    binary = ['b', 'B', 'binary', 'Binary']
    if direction in decimal:
        print('Converting ' + str(n) + ' from binary to decimal:\n.\n.\n.')


converterFunction(askForInt())
