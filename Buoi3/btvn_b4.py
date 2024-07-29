ho_ten = input("Nhap ho va ten: ")
a = list(ho_ten)
b = []
for i in range(len(a)):
    if not(a[i] == ' ' and (a[i - 1] == " " or i == 0)):
        b.append(a[i])
ho_ten = "".join(b)
ho_ten = ho_ten.title()
print("---> ", ho_ten)
