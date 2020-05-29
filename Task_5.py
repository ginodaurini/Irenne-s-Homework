rev = int(input("укажите выручку Вашей компании: "))
costs = int(input("укажите издержки Вашей компании: "))

if rev > costs:
    print("Ваша компания - Отец!")
    print("Ваша рентабельность: ")
    print(rev/costs)

elif rev < costs:
    print("Батенька, Вы - олух!")

emp = int(input("Кол-во сотрудников в Вашей компании: "))
print((rev-costs)/emp)

