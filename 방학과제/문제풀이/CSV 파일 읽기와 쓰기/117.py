import csv
import random

result = []

try:
    file = open('C:/Users/dab06/Desktop/jongno-coding-study-2024/방학과제/문제풀이/CSV 파일 읽기와 쓰기/Score.csv', 'x')
    file.close()
except:
    file = open('C:/Users/dab06/Desktop/jongno-coding-study-2024/방학과제/문제풀이/CSV 파일 읽기와 쓰기/Score.csv', 'r')
    reader = csv.reader(file)

    for line in reader:
        result.append(line)

name = input('Your name: ')
repeat = 2
score = 0
for i in  range(repeat):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    buho = random.randint(1, 3)
    
    if buho == 1:
        if int(input(f'{num1} + {num2} ?: ')) == num1+num2:
            score += 50
    elif buho == 2:
        if int(input(f'{num1} - {num2} ?: ')) == num1-num2:
            score += 50
    elif buho == 3:
        if int(input(f'{num1} * {num2} ?: ')) == num1*num2:
            score += 50

file = open('C:/Users/dab06/Desktop/jongno-coding-study-2024/방학과제/문제풀이/CSV 파일 읽기와 쓰기/Score.csv', 'a')
for line in result:
    print(line)
    file.write(f'{', '.join(map(str, line))}\n')
file.write(f'{name}, {score}\n')
file.close()