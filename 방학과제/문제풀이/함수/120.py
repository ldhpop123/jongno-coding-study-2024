import random

def select():
    print('1) Addition')
    print('2) Subtraction')
    option = int(input('Enter 1 or 2: '))

    if option == 1:
        Addition()
    elif option == 2:
        Subtraction()
    else:
        print('Incorrect option')

def Addition():
    result = 0
    for i in range(2):
        result += random.randint(5, 20)
    
    user_answer = int(input('answer?: '))
    prn(result, user_answer)

def Subtraction():
    num1 = random.randint(25, 50)
    num2 = random.randint(1, 25)
    user_answer = int(input('answer?: '))
    prn(num1+num2, user_answer)

def prn(result, user_answer):
    if result == user_answer:
        print('Correct')
    else:
        print('Incorrect, the answer is')
        print(f'answer: {result} user_answer {user_answer}')