import csv

file = open('C:/Users/dab06/Desktop/jongno-coding-study-2024/방학과제/문제풀이/CSV 파일 읽기와 쓰기/Books.csv', 'a')
repeat = int(input('How many repeat?: '))

for i in range(repeat):
    name = input('name: ')
    author = input('author: ')
    year = input('year: ')
    file.write(f'{name}, {author}, {year}\n')
file.close()

file = open('C:/Users/dab06/Desktop/jongno-coding-study-2024/방학과제/문제풀이/CSV 파일 읽기와 쓰기/Books.csv', 'r')
reader = csv.reader(file)
target_author = input('Enter author: ')
result = []

for line in reader:
    if target_author in line:
        result.append(line)

if len(result) == 0:
    print('Not Found')
else:
    for Book_info in result:
        print(', '.join(map(str, Book_info)))