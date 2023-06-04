sum = 0
print('Введите последовательно три числа:')
digit1 = float(input())
digit2 = float(input())
digit3 = float(input())
if digit1 > 0 :
    sum += digit1
if digit2 > 0 :
    sum += digit2
if digit3 > 0 :
    sum += digit3
print(f'Сумма положительных чисел:\n{sum}')

# Введите последовательно три числа:
# 13
# -5.5
# 9.7
# Сумма положительных чисел:
# 22.7