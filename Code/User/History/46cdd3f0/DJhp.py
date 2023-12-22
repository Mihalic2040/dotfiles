import random

# Завдання 3
# 3.1
array_strings = ['звук', 'колонка', 'кодування', 'модель']
print("3.1: Масив рядків:", array_strings)

# 3.2
n = int(input("Введіть значення n: "))
array_integers = [21, n + 10, 53, 17, n + 15]
print("3.2: Масив цілих чисел:", array_integers)

# 3.3
array_random = [random.randint(4, 10) for _ in range(10)]
print("3.3: Масив випадкових чисел:", array_random)

# 3.4
arithmetic_progression = [n + 4 * i for i in range(5)]
print("3.4: Масив арифметичної прогресії:", arithmetic_progression)

# 3.5
array_random_sum = [random.randint(2, 6) for _ in range(7)]
sum_of_elements = sum(array_random_sum)
print("3.5: Масив випадкових чисел та їх сума:", array_random_sum, ", Сума:", sum_of_elements)

# 3.6
n_geo = float(input("Введіть значення n для геометричної прогресії: "))
geo_progression = [n_geo * 2**i for i in range(6)]
average_geo_progression = sum(geo_progression) / len(geo_progression)
print("3.6: Геометрична прогресія та її середнє значення:", geo_progression, ", Середнє значення:", average_geo_progression)
