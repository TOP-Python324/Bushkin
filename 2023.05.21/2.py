# number = input('\n\t Введите целое число : ')
# ИСПРАВИТЬ: лишние символы пространства в выводе
# ИСПОЛЬЗОВАТЬ: длинные литералы удобно записывать на нескольких строчках кода следующим образом:
# print(f'\n\t Следующие за числом {number} число : {int(number)+1}\n'
      # ИСПРАВИТЬ: только что преобразовывали в int, а здесь повторяетесь — неоптимально
      # f'\t Для числа {number} предыдущее число : {int(number)-1}')
# КОММЕНТАРИЙ: в скобках записаны два строковых литерала, которые при вычислении объединяются в один с помощью неявной конкатенации — вне скобок потребуется явная конкатенация


#  Введите целое число : 33
#
#    Следующие за числом 33 число : 34
#    Для числа 33 предыдущее число : 32


# digit = int(input('Введите целое число: '))
# ИСПРАВИТЬ: лишние пробелы в выводе
# print(f'Следующие за числом {digit} число : {digit+1}\n'
      # f'Для числа {digit} предыдущее число : {digit-1}')


# Введите целое число :138
# Следующие за числом 138 число : 139
# Для числа 138 предыдущее число : 137


digit = int(input('Введите целое число:'))
print(f'Следующие за числом {digit} число :{digit+1}\n'
      f'Для числа {digit} предыдущее число :{digit-1}')


# Введите целое число:135
# КОММЕНТАРИЙ: разработчик, который должен работать с этой строкой, полученной от вас, написал, например, split(': ') — а у вас нет такой подстроки, потому что пробел стоит не там, где нужно
# Следующие за числом 135 число :136
# Для числа 135 предыдущее число :134


# КОММЕНТАРИЙ: внимание к деталям очень важно: невнимательный разработчик — несчастный разработчик


# ИТОГ: хорошо — 2/3
