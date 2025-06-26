name = "Диляра"
age = 25
height = 1.66
human = True

name_2: str = "Диляра"
age_2: int = 25
height_2: float = 1.66
human_2: bool = True

print(f"Имя: {name}, возраст: {age}")
print (type(name))

a = 5
b = 10
# Арифметика
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)

# Сравнение
print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)

# Логические операторы

x = True
y = False

print(x and y)
print(x or y)
print(not x)
print(not y)

"""
Условные конструкции IF, ELIF, ELSE
"""

temperature = 25

if temperature > 30:
    print("АД")
elif temperature > 20:
    print("Жарко")
elif temperature > 15:
    print("Сойдет")
else:
    print("Норм")


status = "Студент" if age < 25 else "Работающий"
print(status)






