"""4.Создайте список из случайных чисел. Найдите количество различных элементов в нем."""
import random
n = int(input("Введите количество элементов: "))
list = [random.randint(0, 10) for item in range(n)]
print(list)
unique_list = []
for i in list:
    if i not in unique_list:
        unique_list.append(i)
print(f"Количество различных элементов: {len(unique_list)}")