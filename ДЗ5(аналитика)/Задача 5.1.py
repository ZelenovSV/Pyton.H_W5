"""1.Создайте список из случайных чисел.
Найдите номер его последнего локального максимума
(локальный максимум — это элемент, который больше любого из своих соседей)."""
import random
n = int(input("Введите количество элементов: "))
list = [random.randint(0, 10) for item in range(n)]
print(list)
local_max=0
for i in range(0, len(list)-1):
    if list[i] > list[i-1] and list[i] > list[i+1]:
        local_max = list[i]
print(f"Локальный максимум: {local_max}")
print(f"Номер последнего локального максимума: {i-1}")
