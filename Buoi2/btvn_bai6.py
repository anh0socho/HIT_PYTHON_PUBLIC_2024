n = int(input("Nhap n = "))

for a in range(1, n + 1):
    sum = 0
    for b in range(1, a):
        if a % b == 0:
            sum = sum + b
    if sum == a:
        print(a)