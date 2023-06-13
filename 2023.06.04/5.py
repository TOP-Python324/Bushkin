symbol_cost = 0.30
text = input('Ведите текст телеграммы : \n')
list_leng = [len(word) for word in text.split()]
list_cost = str(format(sum(list_leng)*symbol_cost,'.2f')).split(".")
print(f'Стоимость отправки телеграммы: \n'
      f'{list_cost[0]} руб. {list_cost[1]} коп.')

# Ведите текст телеграммы :
# прошлом веке для отправки коротких текстовых сообщений люди использовали телеграммы
# Стоимость отправки телеграммы:
# 22 руб. 20 коп.