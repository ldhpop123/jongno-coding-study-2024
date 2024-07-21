def select():
    print('1) Add')
    print('2) Fix')
    print('3) Delete')
    print('4) View')
    print('5) Quit')

    try:
        option = int(input('Enter option number: '))
        if option == 1:
            Add()
        elif option == 2:
            Fix()
        elif option == 3:
            Delete()
        elif option == 4:
            View()
        elif option == 5:
            pass
        else:
            print('Incorrect option')
    except:
        print('Incorrect option')

def Add():
    name = input('Enter name: ')
    name_li.append(name)
    select()

def Option_view():
    for num, name in enumerate(name_li):
        print(f'{num+1}. {name}')

def View():
    for num, name in enumerate(name_li):
        print(f'{num+1}. {name}')
    select()

def Fix():
    Option_view()
    index = int(input('index_number: '))
    name_li[index-1] = input('fix name: ')
    select()

def Delete():
    Option_view()
    index = int(input('index_number: '))
    del name_li[index-1]
    select()

name_li = []

select()