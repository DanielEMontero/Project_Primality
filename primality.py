def run():
    number = input('Please insert a number: ')
    try:
        number = int(number)
    except:
        print('Please, insert only integer numbers.')
        quit
    

if __name__ == "__main__":
    run()