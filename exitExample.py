import sys
while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        print('Programme Terminated...')
        sys.exit()
    print('Your input is '+response+'.')

