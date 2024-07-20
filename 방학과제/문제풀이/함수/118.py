num = 0

def inp():
    save(int(input('Enter num: ')))

def save(result):
    global num
    num = result
    count()

def count():
    for i in range(1, num + 1):
        print(i, end= ' ')

inp()