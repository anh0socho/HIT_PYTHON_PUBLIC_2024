#khai bao tuple
# t0 = tuple()

# t1 = ()

# t2 = ("hello", 1, 2, ["abc", 4, 5])

# t3 = "ciao", [1,2,3], "bonjour"

# print(f"t0={t0}\t({type(t0)})")
# print(f"t0={t1}\t({type(t1)})")
# print(f"t0={t2}\t({type(t2)})")
# print(f"t0={t3}\t({type(t3)})")

# print("t2[1] = ", t2[1])
# print("t3[1][2] = ", t3[1][2])

# t2[3][0] = "bella"
# print(t2)

# t2 = list(t2)
# t2[0] = "ciao"
# t2 = tuple(t2)
# print(t2)



#khai bao set in

#set rong
# s = {1, 2, 3,5,4,5,3}
# print(s)

# s1 = {1,2,3}
#sap xep thu tu luon!!

# set.add(23)
# print(s)

# set.update(34,68,99)
# print(s)

# s.add(9)
# print(s)
# s.remove(2)
# print(s)

# s.clear()
# print(s)

# s.pop()
# print(s)

# s.discard(5)
# print(s)

# superset n subset
# print(s1.issubset(s))
# print(s.issuperset(s1))

# a = {1,2,3}
# b = {3,4,5}

# s = a.union(b)
# print(s)

# s = a ^ b
# print(s)

# s = a - b
# print(s)

# s = a | b
# print(s)

# s = a & b
# print(s)



#
# string = "Hoc lap trinh Python cung HIT"

# result =[]
# # for char in string:
# #     if char == " ":
# #         continue
# #     result.append(char)
# # result = tuple(result)
# # print(result)

# for index in range(len(string)):
#     if string[index] == " ":
#         continue
#     result.append(string[index])
# print(result)

# result = (char for char in string if char != " ")
# result = tuple(result)
# print(result)

# print("O occurent =", result.count("o"))

# danh_sach = [6,5,8,9,3,1,0]
# danh_sach.sort()
# n = len(danh_sach)
# print(danh_sach[n-2])








