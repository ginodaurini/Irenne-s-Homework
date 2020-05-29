time = int(input("Введите время в секундах: "))
hour = time//3600
min = (time - hour*3600)//60
sec = time - (hour*3600 + min*60)
print(f"{hour} : {min} : {sec}")
