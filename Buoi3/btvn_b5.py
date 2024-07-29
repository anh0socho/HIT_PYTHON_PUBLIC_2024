n = int(input("Nhap N:"))
lst=[]
for i in range(n):
    val = int(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(val)

liked_digits = {1, 3, 5, 7, 9}
liked_numbers = [i for i in lst if i % 10 in liked_digits]
liked_numbers.sort()

print(len(liked_numbers))
print(' '.join(map(str, liked_numbers)))