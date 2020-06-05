x = int(input("Введите целое положительное число: "))
max = x%10
x = x//10
while x > 0:
    if x%10 > max:
        max = x%10
    x = x//10
print(max)