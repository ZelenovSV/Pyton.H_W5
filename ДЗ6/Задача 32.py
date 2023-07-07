"""Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)"""
import random
n = int(input("Введите количество элементов: "))
a = int(input("Введите нижнюю границу интервала: "))
b = int(input("Введите верхнюю границу интервала: "))
list = [random.randint(0, 10) for item in range(n)]
print(list)
list1 = []
for i in range(len(list)):
    if list[i]>=a and list[i]<=b:
        list1.append(i)
print(list1)