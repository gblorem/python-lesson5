# -*- coding: utf-8 -*-

'''
7. Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки,
также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
'''

import json

json_object_list = {}
json_object = []

average_profit_list = []
average_profit = 0

with open('./solution_7.txt', 'r', encoding='utf-8') as file:
	for line in file:

		company_name = line.split()[0]
		type_of_ownership = line.split()[1]
		proceeds = line.split()[2]
		costs = line.split()[3]

		profit = int(proceeds) - int(costs)

		if profit > 0:
			json_object_list[company_name] = profit
			average_profit_list.append(profit)
		else:
			profit = 'losses'
			json_object_list[company_name] = profit

file.close()

for i in average_profit_list:
	average_profit += i

average_profit = average_profit / len(average_profit_list)

json_object.append(json_object_list)
json_object.append({'average_profit ' : '{:.2f}'.format(average_profit)})
print(json_object)

with open('./solution_7.json', 'w') as json_file:
	json.dump(json_object, json_file)