def collatz(number):
    while number >= 2:
        if number % 2 == 0:
            print(number//2)        # Integer division
            number = number//2
        elif number % 2 == 1:
            print(3*number+1)
            number = 3*number+1
    if number == 0:
        try:
            print('You have entered 0, please enter a positive integer.')
            number = int(input())
            collatz(number)
        except:
            print('You must enter a positive integer below, try again...')
            number = int(input())
            collatz(number)    
    elif number < 0:
        try:
            print('You have entered a negative integer, please enter a positive integer.')
            number = int(input())
            collatz(number)
        except:
            print('You must enter a positive integer below, try again...')
            number = int(input())
            collatz(number)

    
print('This program is about Collatz sequence.')
print('You give this program any positive integer you will finally get 1.\n')
print('Please type an integer below...')
try:
    numbergiven = int(input())
    collatz(numbergiven)
except:
    print('You must enter a positive integer below, try again...')
    numbergiven = int(input())
    collatz(numbergiven)

