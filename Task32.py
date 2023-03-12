# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

list1 =[random.randint(-20,20) for i in range(int(input("Введите размер массива ")))]
print(list1)
list2 = []
borderMin = int(input("Введите минимальное число в диапазоне: "))
borderMax = int(input("Введите максимальное число в диапазоне: "))
for i in range(len(list1)):
    if list1[i] <= borderMax and list1[i] >= borderMin:
        list2.append(list1[i])
print(sorted(list2))

