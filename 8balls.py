import random

def getAnswer(ansNumber):
    if ansNumber == 1:
        return 'You look so cool'
    elif ansNumber == 2:
        return 'Keep going'
    elif ansNumber == 3:
        return 'You can work hard and succed'
    elif ansNumber == 4:
        return 'Hey handsome'
    elif ansNumber == 5:
        return 'Gonna be rich soon'
    elif ansNumber == 6:
        return 'Life is full of beautiful colors'
    elif ansNumber == 7:
        return 'You are gonna get someone really good'
    elif ansNumber == 8:
        return 'Work on your body and mind'
    elif ansNumber == 9:
        return 'Have confidence in yourself'

r = random.randint(1,9)
fortune = getAnswer(r)
print(fortune)
