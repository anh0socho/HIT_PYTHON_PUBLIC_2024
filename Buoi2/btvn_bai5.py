n = int(input("Nhap n = "))
for val in range(1, n + 1):
    x = val
    y = 0
    d = 0

    while val > 0:
        val //= 10
        y +=1
    val = x

    while val > 0:
        t = val % 10
        d = d + t**y
        val //= 10
    if d == x:
        print(x)
    