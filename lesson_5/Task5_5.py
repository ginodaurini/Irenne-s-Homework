def summary():
    try:
        with open('text_5.txt', 'w+', encoding='utf-8') as file_sum:
            line = input('Введите цифры через пробел: \n')
            file_sum.writelines(line)
            x = line.split()
            print(sum(map(int, x)))
    except IOError:
        print('Error!')
    except ValueError:
        print('Error! Ошибка ввода-вывода.')
summary()
