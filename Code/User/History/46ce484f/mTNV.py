# Завдання 4
# 4.1
array_2d_1 = [['команда', 'файл', 'біт'], ['смартфон', 'миша', 'байт']]
element_1_0 = array_2d_1[0][0]
element_1_1 = array_2d_1[1][1]
print("4.1: Елемент [0][0]:", element_1_0, ", Елемент [1][1]:", element_1_1)

# 4.2
array_2d_2 = [[5, 3, 12], [13, n, n], [21, 6, 8]]
total_sum = sum(sum(row) for row in array_2d_2)
print("4.2: Загальна сума чисел масиву:", total_sum)

# 4.3
array_2d_3 = [[34, n + 5, 23, 19], [18, 19, 37, 51], [77, 20, 35, 55]]
min_elements_per_row = [min(row) for row in array_2d_3]
print("4.3: Мінімальний елемент у кожному рядку:", min_elements_per_row)

# 4.4
array_2d_4 = [[77, 32, 23, 3], [44, 21, 23, 9], [80, n + 3, n, 4]]
row_sums = [sum(row) for row in array_2d_4]
min_sum_row_index = row_sums.index(min(row_sums))
print("4.4: Рядок із мінімальною сумою чисел:", array_2d_4[min_sum_row_index])
