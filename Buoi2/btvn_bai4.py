n = int(input("Nhap n = "))
a = 0
b = 1
print(a, end=' ')
print(b, end=' ')
for val in range(0, n - 2):
    c = a + b
    a = b
    b = c
    print(c, end=' ')