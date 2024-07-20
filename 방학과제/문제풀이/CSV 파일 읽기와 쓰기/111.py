import csv

file = open('C:/Users/dab06/Desktop/jongno-coding-study-2024/방학과제/문제풀이/CSV 파일 읽기와 쓰기/Books.csv', 'w')

book_li = [
['To Kill A Mockingbird', 'Harper Lee', 1960], 
['A Brief History of Time', 'Stephen Hawking', 1988],
['The Great Gatsby', 'F. Scott Fitzgerald', 1985],
['The Man Who Mistook His Wife for a Hat', 'Oliver Sacks', 1985],
['Pride and Prejudice', 'jane Austen', 1813]]

for line in book_li:
    file.write(f"{', '.join(map(str, line))}\n")
file.close()