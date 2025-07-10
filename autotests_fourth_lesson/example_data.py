# список list
numbers = [1, 2, 3, 4, 5]
print(numbers[0])
print(numbers[-1])
print(numbers.index(2))
numbers.append(6)
numbers.insert(5, 6)
print(numbers)

# кортежи (tuple)
coordinate = (10.0, 20.0, 20.0)
print(coordinate[1])
coordinate.count(20.0)
coordinate.index(20.0)

# множества (set)
unic_num = {1, 2, 3, 4, 3}
print(unic_num)
unic_num.remove(1)
print(unic_num)

# словарь (dict)
person = {
    "name": "Диляра",
    "age": 25,
    "city": "Казань"
}
print(person)
print(person.keys())
print(person.values())
print(person.items())
print(person.get("name"))
person.update({"age": 26})
print(person)
person["status"] = "alive"
print(person)

if "city" in person:
    print("Город", person["city"])
for key, value in person.items():
    print(f"{key}: {value}")


def print_data(num, coor, unic_id, pers_info):
    print("Числа")
    for i, num in enumerate(num):
        print(f"{i + 1}, {num}")
    print("Координаты")
    print(f"X: {coor[0]}, Y: {coor[1]}")
    print("Уникальные айди")
    for uid in unic_id:
        print(f"{uid}")
        print("Информация о человеке")


for key, value in person.items():
    print(f"{key}: {value}")

print_data(
        [10, 20, 30],
        (55.3, 45.3),
    {101, 102, 203},
        {"name": "Диляра", "age": "25"}
    )
