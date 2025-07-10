def hello(name):
    return "Привет, " + name + "!"


hello_name = hello("Иван")
print(hello_name)


def get_list(list):
    for elem in list:
        print(elem)


get_list(["яблоко", "банан", "груша"])
