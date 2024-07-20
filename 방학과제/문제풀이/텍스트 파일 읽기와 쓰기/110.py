file = open('C:/Users/dab06/Desktop/jongno-coding-study-2024/방학과제/문제풀이/텍스트 파일 읽기와 쓰기/Names.txt', 'r')
name_li = []

for name in file.read().split('\n'):
    name_li.append(name)
    print(name)
del name_li[-1]

target_name = input('Delete name: ')
name_li.remove(target_name)

file = open('C:/Users/dab06/Desktop/jongno-coding-study-2024/방학과제/문제풀이/텍스트 파일 읽기와 쓰기/Names2.txt', 'w')

for name in name_li:
    file.write(f'{name}\n')
file.close()
