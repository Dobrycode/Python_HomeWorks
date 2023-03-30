#1. Запрос у пользователя - импорт/экспорт
# 2. запись данных
# 3. чтение данных
# 4. Поиск

import func_ask
import func2
while True:
    result = func_ask.select()
    if result == 1:
        user = func_ask.get_user()
        func2.write_data(user)
    elif result == 2:
        res = func_ask.select_find()
        if res == 1:
            print(func2.read_data())
        else: 
            user = func2.read_data()
            name = func_ask.ask()
            func2.find_user(user, name)
    elif result == 3:
        worker = func_ask.ask()
        user_lst, full_lst =func2.select_user(worker)
        num_line = func2.select_str()
        func2.delete_data_person(full_lst, user_lst, num_line)

    elif result == 4:
        worker = func_ask.ask()
        user_lst, full_lst =func2.select_user(worker)
        num_line = func2.select_str()
        user = func_ask.get_user()
        func2.change_data_person(full_lst, user_lst, num_line, user)

    elif result == 0:
        print("До встречи!")
        break
