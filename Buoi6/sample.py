#function

# def name(arguments) :
#     statement
#     ...
#     return value

# tham so la dung trong viet ham
# doi so la gia tri truyen vao ham

# ngon ngu python xac dinh than ham bang cach thut le vao trong
# return tat ca cac kieu du lieu

# tao function

# def hello():
#     print("Ai so thi di ve. Phong cach. Phong cach!!")
# hello()

# def infor(name, age):
#     print(name, "co so tuoi la:", age)
# infor("nam anh", "19")

# def hello(name:str, age:int) -> str:
#     return f"Hello {name}, you are {age} years old"
# print(hello("nam anh", 19))

# def Tong(l:list) -> int:
#     sum = 0
#     for i in l:
#         if i % 2 != 0:
#             sum = sum + i
#     return("Tong cac so le la: ", sum)

# cac_so = [1,2,3,4,5]
# print(Tong(cac_so))

# -------------------------------

# def hello(name:str, age:int) -> str:
#     return f"Hello {name}, you are {age} years old"
# print(hello(age=19, name="Nam Anh"))
# them tu khoa age va name la thanh doi so tu khoa

# return value
# def func(a,b):
#     return a + b
# func(3,4)
# print(func(3,4))

# -------------------------------

# def tong(*args) -> int:
#     print(args)
#     return sum(args)

# a, b, c, d, e, f, g = 1, 2, 3, 4, 5, 6, 7
# result = tong(a, b, c, d, e, f, g)
# print(result)
# * thi thanh tuple

# def sinhvien(**kwargs) -> int:
#     print(kwargs)

# result = sinhvien(name = "nam anh", age = 19, address = "Ha noi")
# print(result)
# ** thi thanh dictionary

def tong(a, b, *args):
    print(args)
    print(a)
    print(b)

tong(1,2,3,4,5,6)
