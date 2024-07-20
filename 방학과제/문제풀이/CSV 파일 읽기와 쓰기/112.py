import csv

file = open('C:/Users/dab06/Desktop/jongno-coding-study-2024/방학과제/문제풀이/CSV 파일 읽기와 쓰기/Books.csv', 'a')

name = input('name: ')
author = input('author: ')
year = input('year: ')

file.write(f'{name}, {author}, {year}\n')
file.close()

file = open('C:/Users/dab06/Desktop/jongno-coding-study-2024/방학과제/문제풀이/CSV 파일 읽기와 쓰기/Books.csv', 'r')
reader = csv.reader(file)
for line in reader:
    print(', '.join(map(str, line)))
