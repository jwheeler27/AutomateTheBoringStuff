#   Program to run the Collatz sequence
#
#   Given and integer, the function will:
#
#   if even -> return num // 2
#   if odd -> return 3 * num +1
#
#   Keep running this sequence till the return
#   value is 1

def collatz(number):

    if number == 1:
        return number
    elif number % 2 == 0:
        result = number // 2
        print(result)
        collatz(result)
    else:
        result = 3 * number + 1
        print(result)
        collatz(result)


if __name__ == '__main__':

    collatz(int(input('Type in an integer: ')))
