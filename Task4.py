# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

s = int(input("Введите количество журавликов: "))
while s % 6 != 0:
    print("Введите другое число, это не подходит(")
    s = int(input("Введите количество журавликов: "))
Pete = s // 6 
Serg = Pete
Kate = (Serg + Pete) * 2
print(f"Катя сделала {Kate} журавликов")
print(f"Сережа и Петя сделали по {Pete} ")
