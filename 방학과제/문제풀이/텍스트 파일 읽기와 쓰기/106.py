file = open('C:/Users/dab06/Desktop/jongno-coding-study-2024/방학과제/문제풀이/텍스트 파일 읽기와 쓰기/Names.txt', 'w')
for i in ['느비예트', '푸리나', '라이덴', '클로린드', '콜롬비나']:
    file.write(f'{i}\n')
file.close()