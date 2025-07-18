def print_words(name: object) -> None:
    words_count = len(name)
    print(f"В слове {name} кол-во букв: {words_count}")

print_words("Диляра")

list_names = ["Ильназ", "Диаз", "Ришат"]

for name in list_names:
    print_words(name)


#  пример 2
def find_max_num(numbers):
    max_num = 0
    for num in numbers:
        if num > max_num:
            max_num = num
    print(max_num)


numbers = [1, 4, -1, 19]
find_max_num(numbers)

# пример 3
def find_concrete_num(list_of_numbers, num_for_compare):
    for num in list_of_numbers:
        if num == num_for_compare:
            print(f"Список содержит число: {num}")
        else:
            print(f"Нет")

list_of_numbers = [1, 5, 15, 25, 30]
find_concrete_num(list_of_numbers, 5)

