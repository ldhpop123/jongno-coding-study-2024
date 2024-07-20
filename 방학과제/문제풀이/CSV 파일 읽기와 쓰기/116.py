import csv

file = open('C:/Users/dab06/Desktop/jongno-coding-study-2024/방학과제/문제풀이/CSV 파일 읽기와 쓰기/Books.csv', 'r')
reader = csv.reader(file)
book_li = []

for num, info in enumerate(reader):
    print(num, info)
    book_li.append(info)

delete_index = int(input('삭제하실 행을 선택해주세요: '))
del book_li[delete_index]

for num, info in enumerate(book_li):
    print(num, info)

fix_index = int(input('수정하실 행을 선택해주세요: '))
target_li = [i.strip() for i in input('쉼표로 끊어 입력해주세요: ').split(',')]
book_li[fix_index] = target_li

file = open('C:/Users/dab06/Desktop/jongno-coding-study-2024/방학과제/문제풀이/CSV 파일 읽기와 쓰기/Books.csv', 'w')
for book_info in book_li:
    file.write(f"{','.join(map(str, book_info))}\n")
file.close()