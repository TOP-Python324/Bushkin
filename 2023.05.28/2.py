numerator = int(input('Введите целое число(делимое):'))
denominator = int(input('Введите целое число(делитель):'))
remains = numerator % denominator

if remains == 0:
    print(f'{numerator} делится на {denominator} нацело\n'
          f'часное:{numerator // denominator}')
# СДЕЛАТЬ: лучше написать код так, чтобы не прописывать генерацию очень похожего литерала второй раз и вообще не использовать блок else — подумайте, как это можно сделать
else:
    print(f'{numerator} не делится на {denominator} нацело\n'
          f'неполное частное: {numerator // denominator}\n'
          f'остаток: {remains}')


# Введите целое число(делимое):16
# Введите целое число(делитель):4
# 16 делится на 4 нацело
# часное:4    

# Введите целое число(делимое):15
# Введите целое число(делитель):2
# 15 не делится на 2 нацело
# неполное частное: 7
# остаток: 1


# ИТОГ: хорошо, но можно лучше — 3/4
