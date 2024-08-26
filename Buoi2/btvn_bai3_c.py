a = int(input("Nhap a = "))
b = int(input("Nhap b = "))
c = int(input("Nhap c = "))
deta = 0
if a == 0 and c != 0 and b != 0:
    print("Phuong trinh la phuong trinh bac 1 voi nghiem x = ", -c/b)
else:
    deta = (b**2) - (4*a*c)
    if deta < 0:
        print("Phuong trinh bac 2 vo nghiem")
    elif deta == 0:
        print("Phuong trinh co nghiem kep voi x = ")
        print(-b/2*a)
    elif deta > 0:
        print("Phuong trinh co hai nghiem phan biet la")
        print("x1 = ", (-b + deta**(1/2))/ 2* a)
        print ("x2 = ",(-b - deta**(1/2))/ 2*a)