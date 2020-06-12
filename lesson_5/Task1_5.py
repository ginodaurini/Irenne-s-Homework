lazy_as_hell = open('damn.txt', 'w', encoding='utf-8')
z = input('Введите текст: \n')
while z:
    lazy_as_hell.writelines(z)
    z = input('Введите текст: \n')
    if not z:
        break

lazy_as_hell.close()
lazy_as_hell = open('damn.txt', 'r', encoding='utf-8')
content = lazy_as_hell.readlines()
print(content)
lazy_as_hell.close()