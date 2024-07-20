a = 3
b = 4

print('{} + {} = {}'.format(a, b, a + b))
print(f'{a} - {b} = {a - b}')
print("a // b = ",a // b)
print('{} ** {} = {}'.format(a, b, a**b))
print(f'{a} % {b} = {a % b}')

if a > b: 
    print("a lon hon b")
elif a < b:
    print("a nho hon b")
else:
    print("a bang b")

print(a & b)
print(a | b)
print(a ^ b)

if ~a is b:
    print("bu 1 cua a bang b ")
elif ~a is not b:
    print("bu 1 cua a khac b")
print(a << a)
print(a >> a)