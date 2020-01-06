# Project from github Find the value of PI up to the Nth digit
# the algorithm used is the nikalantah serie

# The idea is to iterate the loop until the last two values calculated (piOld and piNew) don't differ
# between eachother in the nTh+2 digit of precicion from two iterations, this should assure that the digit
# will not change even if we kept iterating for longer, making that a sure digit of pi.
# ---- In practice this doesn't work when  n gets too high ----


import decimal


def askForInt():
    maxPrecision: int = 15


    while True:
        try:
            n = int(input('''Please, type to which precision you want to calculate Pi:'''))

        except ValueError:
            print('''This is not an Int''')
            continue

        if n > maxPrecision:
            print('''The number is too big, max value of is equal to ''' + str(maxPrecision))
        else:
            return n


def calculatePi(n):
    # TODO understand why it doesn't always work as in the stated idea with big n
    # probably because precision of the last additions is too low
    decimal.getcontext().prec = n + 2

    piOld = 0
    piNew = 3

    i = 2  # needed for the algorithm
    signVar = False  # handles the alternating + and - signs of the algorithm

    loopCount = 0  # used only to count the number of iteration
    while True:
        denom = decimal.Decimal(i * (i + 1) * (i + 2))

        if signVar:
            piNew -= 4 / denom
        else:
            piNew += 4 / denom

        signVar = not signVar  # sets signVar for the next iteration

        # Something that checks if the first n digits are correct
        if not decimal.Decimal(piNew).compare(piOld):
            # Doesn't "cut" the extra digit after n in piNew TODO remove the extra digits from the solution
            decimal.getcontext().prec = n
            print('''The value of piNew to the n=''' + str(n) + ''' precision is:\n ''', piNew)
            break
        else:
            piOld = piNew

        i = i + 2
        loopCount += 1

    print(loopCount)


print(''' Hi, This is a program that calculates Pi up to the Nth digit.\n\n''')

calculatePi(askForInt())
