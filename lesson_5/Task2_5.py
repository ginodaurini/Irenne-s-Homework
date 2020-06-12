file_2 = open('text_2.txt', 'r', encoding='utf-8')
content = file_2.read()
print(f'Содержимое файла: \n{content}')
file_2 = open('text_2.txt', 'r', encoding='utf-8')
content = file_2.readlines()
print(f'Количество строк в файле - {len(content)}')
file_2 = open('text_2.txt', 'r', encoding='utf-8')
line = 0
for i in file_2:
    line += 1

    flag = 0
    word = 0
    for j in i:
        if j != ' ' and flag == 0:
            word += 1
            flag = 1
        elif j == ' ':
            flag = 0

    print(f'Cтрока: {i}', word, 'слов.')

file_2.close()