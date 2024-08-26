n = int(input("Nhap n: "))
sum = 0
for val in range(1, 2 * n + 2):
    if val % 2 == 0:
        sum = sum - val
    else:
        sum = sum + val
print(sum)