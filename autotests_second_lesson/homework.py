# Пример с арифметическими операциями
mango_calories = 60
passion_fruit_calories = 70
smoothie_calories = mango_calories + passion_fruit_calories
print(f"Калорийность смузи : {smoothie_calories}")

# Примеры с условными конструкциями
if smoothie_calories > 200:
    print("Калорийный")
else:
    print("Диетический")

food_name = "Рыба"
fish_calories = 150
potato_calories = 80

if food_name == "Рыба":
    print(f"Калорийность рыбы : {fish_calories}")
elif food_name == "Картошка":
    print(f"Калорийность картошки : {potato_calories}")
else:
    print("Неизвестно")
