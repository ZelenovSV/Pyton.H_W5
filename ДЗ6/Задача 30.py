"""Задача 30:  Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
 Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки."""
a1 = int(input("Введите первый элемент прогрессии:"))
n = int(input("Введите количество элементов: "))
d = int(input("Введите разность:"))
list = []
for i in range(1, n+1):
    ai = a1 + (i-1)*d
    list.append(ai)
print(f"Арифметическая прогрессия: {list}")