import csv

file = open('C:/Users/dab06/Desktop/jongno-coding-study-2024/방학과제/문제풀이/CSV 파일 읽기와 쓰기/Books.csv', 'r')
reader = csv.reader(file)

for num, info in enumerate(reader):
    print(num, info)
