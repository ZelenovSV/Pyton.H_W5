"""3.Создайте список из случайных чисел. Найдите второй максимум.
a = [1, 2, 3] # Первый максимум == 3, второй == 2"""
import random
n = int(input("Введите количество элементов: "))
list = [random.randint(0, 10) for item in range(n)]
print(list)
local_max1=list[0]
for i in list:
    if i > local_max1:
        local_max1 = i
        list.remove(local_max1)
local_max2 = list[0]
for i in list:
    if i > local_max2:
        local_max2 = i 
print(f"Второй максимум: {local_max2}")