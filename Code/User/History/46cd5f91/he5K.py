# Завдання 2
# 2.1
prices = {"інформатика": 45, "географія": 53, "історія": 40, "хімія": 47}

min_price = min(prices.values())
max_price = max(prices.values())
chemistry_price = prices.get("хімія", 0)

print("2.1: Мінімальна ціна:", min_price)
print("     Максимальна ціна:", max_price)
print("     Ціна посібника з хімії:", chemistry_price)

# 2.2
trains = {23: "Львів", 7: "Одеса", 15: "Харків"}
trains[37] = "Херсон"
trains[29] = "Полтава"
del trains[15]

print("2.2: Оновлений словник потягів:", trains)
