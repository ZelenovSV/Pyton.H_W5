"""2.Создайте список из случайных чисел. 
Найдите максимальное количество его одинаковых элементов."""
import random
n = int(input("Введите количество элементов: "))
list = [random.randint(0, 10) for item in range(n)]
print(list)
count_dict={}
for num in list:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1
max_count = max(count_dict.values())
print(f"Максимальное количество одинаковых элементов: {max_count}")