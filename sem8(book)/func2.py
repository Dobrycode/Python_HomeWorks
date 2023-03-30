def write_data(user):
    with open("data.txt", "a", encoding = "UTF-8") as file:
        file.write(user + "\n")


def read_data():
    with open("data.txt", "r", encoding = "UTF-8") as file:
        all_text = file.readlines()
        res = [i.strip() for i in all_text]
        return res

def find_user(lst, str):
    for value in lst:
        if str in value:
            print(value)

def select_user(worker):
    user_lst=[]
    with open("data.txt", "r", encoding = "UTF-8") as f:
        full_lst = f.readlines()
        for line in full_lst:
            if worker in line:
                user_lst.append(line)
    print(*user_lst)
    return user_lst, full_lst

def select_str():
    answer = int(input("введи номер строчки: "))
    return answer

def change_data_person(full_lst, user_lst, num_line, user):
    with open("data.txt", "w", encoding = "UTF-8") as f:
        for line in full_lst:
            if user_lst[num_line - 1] != line:
                f.write(line)
            else:
                f.write(user)

def delete_data_person(full_lst, user_lst, num_line):
    with open("data.txt", "w", encoding = "UTF-8") as f:
        for line in full_lst:
            if user_lst[num_line - 1] != line:
                f.write(line)
            else:
                continue

