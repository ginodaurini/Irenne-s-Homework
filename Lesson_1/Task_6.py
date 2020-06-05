z = int(input("кол-во км в первый день: "))
max = int(input("цель в км: "))
day = 1
distance = z
while distance < max:
    z = z + z*0.1
    day = day + 1
    distance = distance + z

print(f"а что сюда писать я не знаю :)")

