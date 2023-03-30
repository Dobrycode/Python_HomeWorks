def select():
    print("Выбери действие:\n1 - импортировать файлы \n 2 - экспортировать \n 3- удалить данные\n 4 - изменить данные\n 0-выход\n")
    a = int(input())
    return a

def get_user():
    print("Введите новые данные: ")
    user = input("Введите имя, фамилию, номер телефона (через пробел): ")
    return user

def select_find():
    return int(input("Введите 1 - если хотите вывести весь список, \n 2 - для поиска по ключевым словам \n"))

def ask():
    return input("Введите данные пользователя для поиска: ")

def delete_data():
    data_str = input("Введите данные для удаления строки: ")
    return data_str

    
