for num in range(10):
    if num == 2:
        continue
    if num == 4:
        pass
    if num == 7:
        break
print(num)

fruits = ['apple', 'banana', 'orange']
for fruit in fruits:
    if fruit == 'banana':
        continue
    print(fruit)

count = 0
while count < 3:
    print(count)
    count += 1

while True:
        answer = input("Продолжить? (да/нет): ")
        if answer.lower() == "нет":
            break


"""ЦЕЛИ ЦИКЛОВ"""
# 1. Перебор
for fruit in fruits:
    print(fruit)
# Строчный
    for char in "Python":
        print(char)

# 2. Повторы
for _ in range(2):
    print("Привет!")
# Счётчик
for i in range(1, 11):
    print(f"{i}, привет")

# 3. Обработка ввода
age = input("Сколько тебе лет? ")
while not age.isdigit():
    age = input("Сколько тебе лет? ")

# 4. Автоматизации
numbers = [1, 4, 7, 10]
for num in numbers:
    if num % 2 == 0:
    print(num)
# Подсчет
total = 0
for num in numbers:
    total += num
    print(total)