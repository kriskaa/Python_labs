numbers_fib = [0, 1]
n = 8

for i in range(2, n):
    numbers_fib.append(numbers_fib[-1] + numbers_fib[-2])

print("Перші", n, "чисел ряду Фібоначчі:")
print(numbers_fib)
sum_fib = sum(numbers_fib)
print("Сума перших", n, "чисел ряду Фібоначчі:", sum_fib)
