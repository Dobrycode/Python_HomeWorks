# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
# 1 2 3 4 5
#   3
# >  1

lst = []
n = int(input("Введите количество элементов в массиве: "))
x = int(input(f'Введите число от 1 до {n}: '))
count = 0
for i in range(1, n+1):
    lst.append(i)
    if i == x:
        count +=1
print(lst)
print(f'Число {x} встречается в массиве {count} раз')