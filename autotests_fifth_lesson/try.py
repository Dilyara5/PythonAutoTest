# пример 1
a = 5
b = 2
try:
    result = a / b
    print(result)
except ZeroDivisionError:
    print("Делить на ноль нельзя!")


 # пример 2
try:
    num = int(input("Введите число: "))
    result = 10 / num
    print(result)
except ValueError:
    print("Не число!")
except ZeroDivisionError:
    print("На ноль делить нельзя!")


# пример 3
def get_value(d, key):
    try:
        return d[key]
    except KeyError:
        return "Ключа нет"
data = {"name": "Диляра", "age": 25}
print(get_value(data, "age"))
print(get_value(data, "city"))


# пример 4
a = 2
try:
    assert a == 2
    print("Проверка ок!")
except AssertionError:
    print("Проверка не ок!")