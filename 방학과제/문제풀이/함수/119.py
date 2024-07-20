import random

def comp():
    low = int(input('Low number: '))
    high = int(input('High number: '))
    comp_num = random.randint(low, high)
    answer(comp_num)

def answer(comp_num):
    print('I am thinking of a number...')
    result = int(input('Enter num: '))
    yes_or_no(comp_num, result)

def yes_or_no(comp_num, result):
    if comp_num == result:
        print('Correct, you win')
    else:
        answer(comp_num)

comp()