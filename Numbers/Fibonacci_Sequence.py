# This program calculates the fibonacci sequence


def askForInt():
    maxIteration: int = 30

    while True:
        try:
            n = int(input('''Please, type how many steps of the fibonacci sequence you want to calculate:'''))

        except ValueError:
            print('''This is not an Int''')
            continue

        if n > maxIteration:
            print('''The number is too big, max value of is equal to ''' + str(maxIteration))
        else:
            return n


def calculateFibonacci(n):

    first = 1
    second = 1
    result = 0
    while n > 0:
        result = first+second
        first, second = second, second + first
        n = n - 1
        print(first)

    return result


calculateFibonacci(askForInt())
