# ИСПОЛЬЗОВАТЬ: согласно PEP 8 комментарии размещаются над комментируемой строкой
# разметка шахматной доски по горизонтали
ranks = ('a','b','c','d','e','f','g','h')

# ПЕРЕИМЕНОВАТЬ: клетка поля — square, field; cage — клетка для животных
chess_cage_one = input('Введите первую клетку доски: ')
chess_cage_two = input('Введите вторую клетку доски: ')

# ИСПОЛЬЗОВАТЬ: для записи длинных выражений на нескольких строчках кода используются либо круглые скобки, либо обратный слэш, но не вместе — поскольку скобки здесь не только для переноса, но и для изменения приоритета операторов, то слэш вместо скобок вы использовать не можете
# ИСПОЛЬЗОВАТЬ: а соединяющие операторы согласно PEP 8 всегда лучше записывать в начале строчки кода
# multiply_g = (int(chess_cage_one[1])
#               - int(chess_cage_two[1])) % 2
# ИСПОЛЬЗОВАТЬ: но на самом деле здесь перенос вообще избыточен
multiply_g = (int(chess_cage_one[1]) - int(chess_cage_two[1])) % 2
# КОММЕНТАРИЙ: у вас хороший рабочий вариант, но просто напомню, что для любого символа можно получить его код (число) в таблице UTF-8 с помощью функции ord() — и это быстрее и компактнее, чем вычисления индексов
multiply_v = (ranks.index(chess_cage_one[0]) - ranks.index(chess_cage_two[0])) % 2

# ИСПОЛЬЗОВАТЬ: для записи длинных выражений на нескольких строчках кода лучше использовать круглые скобки, при этом соединяющие операторы должны находиться в начале соответствующих строчек
# if (
#        not multiply_g and not multiply_v
#     or multiply_g and multiply_v
# ):
# ИСПОЛЬЗОВАТЬ: но здесь перенос точно также избыточен
# ИСПРАВИТЬ: учитывая, что эти ваши переменные могут принимать значения только 0 и 1 — намного проще сравнить их между собой
if not multiply_g and not multiply_v or multiply_g and multiply_v:
    print('да')
else:
    print('нет')


# Введите первую клетку доски: a1
# Введите вторую клетку доски: b2
# да

# Введите первую клетку доски: h8
# Введите вторую клетку доски: f7
# нет


# КОММЕНТАРИЙ: этот ресурс поможет вам лучше придумывать имена переменным: https://context.reverso.net/перевод/русский-английский
#  никогда не забывайте про контекст, пример с клеткой довольно наглядный — переводите не по одному слову, а сразу словосочетаниями с контекстом


# ИТОГ: очень хорошо — 4/5
