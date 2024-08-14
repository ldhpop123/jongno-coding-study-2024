import csv

def select():
    print('1) Add to file')
    print('2) View all records')
    print('3) Quit program')

    try:
        option = int(input('Enter the number of your selection: '))
        
        if option == 1:
            Addition()
        elif option == 2:
            View_records()
        elif option == 3:
            pass
        else:
            print('Incorrect option')
            select()
    except:
        print('Incorrect option')
        select()

def Addition():
    file = open('C:/Users/dab06/Desktop/jongno-coding-study-2024/방학과제/문제풀이/함수/Salaries.csv', 'w')
    
    for i in range(int(input('repeat: '))):
        name = input('name: ')
        salary = int(input('salary: '))
        file.write(f'{name}, {salary}\n')
    file.close()
    select()

def View_records():
    file = open('C:/Users/dab06/Desktop/jongno-coding-study-2024/방학과제/문제풀이/함수/Salaries.csv', 'r')
    reader = csv.reader(file)

    for line in reader:
        name, salary = line
        print(f'name: {name.strip()} salary: {salary.strip()}')
    select()

select()