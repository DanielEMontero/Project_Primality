
def primalidad(number):
    for i in range(2,number+1):
        if i != 1 and i != number:
            if number % i != 0:
                continue
            else:
                return False
    return True        

def run():
    number = input('Please insert a number: ')
    try:
        number = int(number)
    except:
        print('Please, insert only integer numbers.')
        quit
    if primalidad(number) == False:
        print('The number is not a prime number')
    else:
        print('The number is a prime number')


if __name__ == "__main__":
    run()