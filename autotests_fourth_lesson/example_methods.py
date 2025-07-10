def demo(*args, **kwargs):
    print(args)
    print(kwargs)


demo(1, 2, 3, a=4, b=5)


def add(a: int, b: int) -> int:
    return a + b


add_res = add(1, 2)
print(add_res)

assert add(1, 2) == 3


def temperature_locator(temperature):
    if temperature > 30:
        print("Жарко")
    elif temperature > 20:
        print("Тепло")
    else:
        print("Нормально")
temperature_locator(20)

