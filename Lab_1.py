a = int(input("Введіть а: "))

while (a < 0):
    a = int(input("Значення 'а' має бути більше 0. Введіть а: "))

b = int(input("Введіть b: "))
while (b < 0):
    b = int(input("Значення 'b' має бути більше 0.Введіть b: "))

if a < b:
    result = a/b-3
    print("a < b")

elif a == b:
    result = -5
    print("a == b")

else:
    result = ((a*a-b)/b)
    print("a > b")

print("result = ", format(result, '.2f'))
