def select():
    try:
        option = int(input('Make a selection 1, 2 or 3: '))
        if option == 1:
            create_file()
        elif option == 2:
            Display_file()
        elif option == 3:
            Add_item()
        else:
            print('Incorrect option')
            select()
    except:
        print('Incorrect option')
        select()

def create_file():
    file = open('C:/Users/dab06/Desktop/jongno-coding-study-2024/방학과제/문제풀이/텍스트 파일 읽기와 쓰기/Subject.txt', 'w')
    file.close()

def Display_file():
    try:
        file = open('C:/Users/dab06/Desktop/jongno-coding-study-2024/방학과제/문제풀이/텍스트 파일 읽기와 쓰기/Subject.txt', 'r')
        print(file.read())
    except:
        print('file Not Found')
    

def Add_item():
    file = open('C:/Users/dab06/Desktop/jongno-coding-study-2024/방학과제/문제풀이/텍스트 파일 읽기와 쓰기/Subject.txt', 'a')
    file.write(f'{input('New subject name: ')}')
    file.close

select()