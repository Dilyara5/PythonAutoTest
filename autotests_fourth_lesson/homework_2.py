# ЗАДАНИЕ № 1 (список - list)
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(numbers)

# вывод первых 5 чисел
print(numbers[:5])

# вывод 5ого элемента
print(numbers[5])

# изменение 5ого элемента на другое число
numbers[5] = 51
print(numbers)

# добавление нового числа в конец списка
numbers.insert(10, 110)
print(numbers)

# --------------------------------------------------------------------

# ЗАДАНИЕ № 2 (кортеж - tuple)
weather = ("Солнечно", "Пасмурно", "Дождливо")
print(weather)
print(weather[1])

# Изменить элемент кортежа невозможно:
# weather[2] = "Ясно"
# print(weather)

# Создать новый кортеж, добавляя новый элемент
new_element = ("Морозно",)
new_weather = weather + new_element
print(new_weather)

# --------------------------------------------------------------------

# ЗАДАНИЕ № 3 (множества - set)
set_1 = {1, 2, 3}
set_2 = {3, 4, 5}

# Вывод общих элементов в 2х множествах
print(set_1.intersection(set_2))

# Объединение 2х ммножеств
print(set_1.union(set_2))

# Удаление числа из 2ого множества
set_2.remove(4)
print(set_2)

# --------------------------------------------------------------------

# ЗАДАНИЕ № 4 (словарь - dict)
cat = {
    "Имя": "Ева",
    "Цвет": "серый",
    "Порода": "Шотландская",
}

print(cat)

# Вывод значения по ключу "Имя"
print(cat.get("Имя"))

# Добавить новую пару
cat["Возраст"] = "3"
print(cat)

# Удалить ключ X
del cat["Возраст"]
print(cat)

# --------------------------------------------------------------------

# ЗАДАНИЕ № 5 (метод для списка)

def sort_positive_num(numbers):
    positive_numbers = []
    for num in numbers:
        if num > 0:
            positive_numbers.append(num)

    return positive_numbers


numbers = [1, -2, 3, -4, 5]
new_positive_numbers = sort_positive_num(numbers)
print(new_positive_numbers)


# --------------------------------------------------------------------

# ЗАДАНИЕ № 6 (метод для словаря)

def print_updated_age(person, years_to_add):
    person_age = person.get("age")
    new_person_age = person_age + years_to_add
    print(new_person_age)

person_dilyara = {
    "name": "Диляра",
    "age": 25,
    "city": "Казань"
}

print_updated_age(person_dilyara, 5)



