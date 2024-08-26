# # # OOP with Python -- Lap trinh huong doi tuong
# # # la mot phuong phap lap trinh dua tren khai niem "doi tuong"

# # # 1. class - thuoc tinh va phuong thuc
# # # class Person:
# # #  

# # #     # dinh nghia thuoc tinh khoi tao
# # #     def __init__(self, name: str, age: int) -> None:
# # #         self.name = name
# # #         self.age = age
# #         # phuong thuc
# # #     def sleep(self):
# # #         print(self.name + "is working")

# # # student = Person("Nam Anh", 19)
# # # student.sleep

# # # Instance and Class Variable

# # class Teacher:
# #     basic_salary = 3
# #     def __init__(self, name, age, coeffsalary):
# #         self.name = name
# #         self.age = age
# #         self.coeffsalary = coeffsalary
# #         self.__chieucao = 1.75
# #     def getChieucao(self):
# #         return self.__chieucao
# #     def getSalary(self):
# #         return self.coeffsalary * Teacher.basic_salary
    
# # t1 = Teacher("Hoang", 20, 4)
# # t2 = Teacher("Kien", 24, 7)
# # t3 = Teacher("Phong", 29, 12)
# # t4 = input()
# # tuoi = input()
# # t4 = Teacher(t4, tuoi, 1)
# # # print(t4.name, t4.age, "luong: ", t4.getSalary())
# # print (t1.getChieucao())

# # # _ la protected dung dc cho cac class con cua class me
# # # __ la private thi chi dung duoc tron class duoc khai bao
# # # khong co _ nao thi la public dung duoc cho ca truy cap ben ngoai

# class Person:
#     def __init__(self):
#         self.name = "Nam Anh"
#         self._age = 19
#         self.__chieucao = 1.75

# class Student(Person):
#     def __init__(self):
#         super
#     def get(self):
#         self.name
#         self._age
#         self.__chieucao

# n1 = Student()
# print(n1)

# -------------------------------------------------------------

