text = "Python - мощный язык"
print(text)
print(text[0:3])
print(text[-10])
print(len(text))

print(text.lower())
print(text.upper())
print(text.capitalize())
print(text.title())

bad_text = "      Привет мир!   ! "
print(bad_text)
print(bad_text.strip())
print(bad_text.lstrip())
print(bad_text.rstrip())

new_text = text.replace("мощный", "гибкий")
print(new_text)

words = text.split()
print(words)

name = "Диляра"
age = 25
city = "Казань"

# старый способ через %
print("Имя: %s, Возраст : %d, Город: %s" % (name, age, city))

# format
print("Имя: {}, Возраст : {}, Город: {}".format(name, age, city))
print("Имя: {a}, Возраст : {b}, Город: {c}".format(a=name, b=age, c=city))

# современная f строка
print(f"Имя: {name}, Возраст: {age}, Город: {city}")
