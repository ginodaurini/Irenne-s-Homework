with open('text_3.txt', 'r', encoding='utf-8') as workers:
    sal = []
    bum = []
    workers_list = workers.read().split('\n')
    for i in workers_list:
        i = i.split()
        if float(i[1]) < 20000:
           bum.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20.000: {bum}\nCредний оклад: {sum(map(float, sal)) / len(sal)}')
