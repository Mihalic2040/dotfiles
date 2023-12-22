
# Завдання 1

n = input("Уведінь число n:>> ")
n = int(n)
# 1.1
my_list = [13, n + 9, 11, n + 1, 18]
removed_element = my_list.pop(0)
max_element = max(my_list)

# 1.2
cities = ["Херсон", "Житомир", "Ужгород", "Харків"]
cities.insert(1, "Луцьк")
cities.sort()

# 1.3
my_list_2 = [n + 8, 2, n + 2, 6]
my_list_2[0] = 12
sorted_list_2 = sorted(my_list_2)

# 1.4
scientists_list = ["В. Глушков", "вчений України"]
scientists_list[0] = "В. Глушков — великий"
string_scientists = ' '.join(scientists_list)

# 1.5
list1 = ["Мова", "Pascal"]
list2 = ["— це мова", "процедурного програмування"]
merged_list = list1 + list2
string_merged = ' '.join(merged_list)

# 1.6
my_list_3 = [5, n + 3, 8, 12, n + 1]
sum_greater_than_n_plus_4 = sum(element for element in my_list_3 if element > n + 4)

# Виведення результатів
print("1.1: Виделений елемент =", removed_element, ", Максимальний елемент =", max_element)
print("1.2: Міста =", cities)
print("1.3: Сортований і оновлений =", sorted_list_2)
print("1.4: Список на рядок =", string_scientists)
print("1.5: Зєднання списків =", string_merged)
print("1.6: Сума елементів > n + 4 =", sum_greater_than_n_plus_4)

