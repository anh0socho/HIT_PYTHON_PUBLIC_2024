s = input("Nhap chuoi: ").strip()
my_dict = {}

for k in s:
    my_dict[k] = my_dict.get(k, s.count(k))
print(my_dict)