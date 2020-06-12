import json
profit = {}
pr = {}
prof = 0
average_profit = 0
i = 0
with open('text_7.txt', 'r', encoding='utf-8') as file:
    for line in file:
        name, firm, gain, damage = line.split()
        profit[name] = int(gain) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        average_profit = prof / i
        print(f'Прибыль средняя - {average_profit:.2f}')
    else:
        print(f'Все плохо!')
    pr = {'средняя прибыль': round(average_profit)}
    profit.update(pr)
    print(f'Прибыль каждой компании: {profit}')

with open('text_77.json', 'w', encoding='utf-8') as write_js:
    json.dump(profit, write_js, ensure_ascii=False)

    js_str = json.dumps(profit, ensure_ascii=False)
    print(f'json: \n ' f' {js_str}')
