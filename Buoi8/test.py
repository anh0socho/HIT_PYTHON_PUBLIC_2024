# Bai 3
# class Vehicle:
#     def __init__(self, make):
#         self.make = make
#     def description(self):
#         return self.make


# class Car(Vehicle):
#     def __init__(self, model):
#         super().__init__(self)
#         self.model = model
#     def description(self):
#         return self.model

# class ElectricCar(Car):
#     def __init__(self, battery_size):
#         super().__init__(self)
#         self.battery_size = battery_size
#     def description(self):
#         return self.battery_size
    
# brand = Vehicle("Toyota")
# car = Car("Camry")
# battery = ElectricCar("100Wh")
# print(brand.description())
# print(car.description())
# print(battery.description())
# ________________________________________________________________


# bai 4
# class Tam_thuc_bac_hai:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def khoi_tao(self):
#         self.a = input()
#         self.b = input()
#         self.c = input()
#     def __str__(self):
#         print( self.a,".x2 +",self.b, "b + ", self.c,"c")
#     def getstr(self):
#         self.__str__()
#     # def tinh_toan(self):


# he_so = Tam_thuc_bac_hai(3,4,5)
# a = he_so.khoi_tao()
# b = he_so.getstr()
# print(b)
# ________________________________________________________________


