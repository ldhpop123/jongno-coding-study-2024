file = open('C:/Users/dab06/Desktop/jongno-coding-study-2024/방학과제/문제풀이/텍스트 파일 읽기와 쓰기/Numbers.txt', 'w')
num = [1, 2, 3, 4, 5]
result = ','.join(map(str, num))
file.write(result)
file.close()