from re import split
import json

mass_of_for_calc_average_profit_of_firms = []
list_of_firm_and_profit = []
dict_of_firms_and_profit = dict()
dict_of_average_profit = dict()
with open('firms.txt', 'r', encoding='utf-8') as f, open("average_profit.json", 'w', encoding='utf-8') as fjs:
    quantity_of_str = len(f.readlines())
    f.seek(0)
    for _ in range(quantity_of_str):
        string_of_firm = f.readline()
        mass_str_of_firm = split('[ |.\n]', string_of_firm)
        profit_of_firm = float(mass_str_of_firm[2]) - float(mass_str_of_firm[3])
        if profit_of_firm > 0:
            mass_of_for_calc_average_profit_of_firms.append(profit_of_firm)
            dict_of_firms_and_profit[mass_str_of_firm[0]] = profit_of_firm
        else:
            dict_of_firms_and_profit[mass_str_of_firm[0]] = profit_of_firm

    average_profit = sum(mass_of_for_calc_average_profit_of_firms) / len(mass_of_for_calc_average_profit_of_firms)
    dict_of_average_profit['average_profit'] = average_profit
    list_of_firm_and_profit.append(dict_of_firms_and_profit)
    list_of_firm_and_profit.append(dict_of_average_profit)
    json.dump(list_of_firm_and_profit, fjs)
