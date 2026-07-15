import json
#创建Student类，包含name和age属性
class Student:
    def __init__(self, name, age):  
        self.name = name
        self.age = age
#编写introduce方法，打印自我介绍
    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
#创建两个Student对象，并调用introduce方法
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)
student1.introduce()
student2.introduce()
#将学生信息保存到students.json
students = [
    {"name": student1.name, "age": student1.age},
    {"name": student2.name, "age": student2.age}
]
with open("students.json", "w") as f:
    json.dump(students, f)
#再从students.json中读取学生信息，并打印出来
with open("students.json", "r") as f:
    loaded_students = json.load(f)
    for student in loaded_students:
        print(f"Name: {student['name']}, Age: {student['age']}")
