class PersonMan:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print(f"Привет {self.name}, тебе {self.age} лет")

man = PersonMan("Иван", 18)
man.hello()

class Student(PersonMan):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university
    def study(self):
        print(f" {self.name} учится в {self.university} и ему {self.age} лет")

student = Student("Петр", 20, "МГУ")
student.hello()
student.study()
