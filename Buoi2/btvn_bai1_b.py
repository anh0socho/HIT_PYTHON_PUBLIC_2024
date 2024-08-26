n = int(input("Nhap so nguyen duong n: "))
sum  = 0
for val in range(1, n+1):
    if n % val == 0:
        sum = sum + val
print(sum)