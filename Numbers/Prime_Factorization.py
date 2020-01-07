# Just a fun to handle input
def askForInt():
    maxValue: int = 10000

    while True:
        try:
            n = int(input('Please, type an Int to factorize:'))

        except ValueError:
            print('''This is not an Int''')
            continue

        if n > maxValue:
            print('''The number is too big, max value of is equal to ''' + str(maxValue))
        else:
            return n


def primeFactors(n):
    # Is the list that has to be filled with the factors in the format: n=150 [[2, 1], [3, 1], [5, 2]]
    # Maybe the problem is the initialization? Maybe it's the scope?
    factorsList = []

    # This variable is here to make operations on n freely and still be able to print the value at the end
    yourNumber = n

    for i in range(2, n + 1):

        factorCount = 0
        while (n / i).is_integer():
            factorCount += 1
            n = n / i

        if factorCount != 0:
            factorsList.append([i, factorCount])

    print('The prime factors of ' + str(yourNumber) + ' are: ')
    for i in range(len(factorsList)):
        print(str(factorsList[i][0]) + '*' + str(factorsList[i][1]))


primeFactors(askForInt())
