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
lst = input(f'Введите через пробел список чисел длиной {n} элементов: ').split()
while len(lst) != n:
   lst = input(f'Вы ввели неверно! Введите через пробел список чисел длиной {n} элементов: ').split()
x = int(input(f'Введите число, которое необходимо найти в списке: '))
count = 0
for i in range(n):
    if int(lst[i]) == x:
        count +=1
print(lst)
print(f'Число {x} встречается в массиве {count} раз')