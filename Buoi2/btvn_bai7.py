n = int(input("Nhap n: "))

for a in range(1, n + 1):
    sum = 0
    for b in range(1, a):
        if a % b == 0:
            sum += b
    
    for c in range(a + 1, n + 1):
        z = 0
        for d in range(1, c):
            if c % d == 0:
                z +=d
                if sum == c and z == a:
                    print (a, c, end=' ')
    