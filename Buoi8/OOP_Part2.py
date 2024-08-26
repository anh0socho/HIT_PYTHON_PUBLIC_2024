# Bai6.1
class HinhChuNhat: 
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
    def Perimeter(self):
        return (self.chieu_dai + self.chieu_rong)*2
    def Area(self):
        return self.chieu_dai * self.chieu_rong
    def Display(self):
        print("Chieu dai cua Hinh chu nhat la: ", self.chieu_dai)
        print("Chieu rong cua Hinh chu nhat la: ", self.chieu_rong)
        print("Chu vi cua hinh chu nhat la: ", self.Perimeter())
        print("Dien tich cua hinh chu nhat la: ", self.Area())

a = int(input("Nhap chieu dai cua hinh chu nhat: "))
b = int(input("Nhap chieu rong cua hinh chu nhat: "))
h1 = HinhChuNhat(a, b)
c = h1.Display()
print(c)