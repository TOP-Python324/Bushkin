# number = input('\t Введите трехзначное число : ')
# ПЕРЕИМЕНОВАТЬ: цифра числа — digit
# number1 = int(number)//100
# ИСПРАВИТЬ: не следует повторять одинаковые действия: вам не нужен объект str, возвращаемый функцией input(), вместо того, чтобы сохранять его в переменную number, следовало возвращаемое значение input() сразу преобразовать в объект int и уже этот объект сохранить в number — тогда бы и не пришлось здесь многократно преобразовывать в int
# number2 = (int(number)%100)//10
# number3 = (int(number)%100)%10
# ИСПРАВИТЬ: нужно справиться за один вызов print()
# ИСПРАВИТЬ: лишние символы пространства в выводе
# print(f'\n\t Сумма цифр = {number1+number2+number3}')
# print(f'\t Произведение цифр = {number1*number2*number3}')


#      Введите трехзначное число : 123
#       Сумма цифр = 6
#       Произведение цифр = 6

# ПЕРЕИМЕНОВАТЬ: число — number; цифра числа — digit (только не говорите, что в принципе не знаете разницу между цифрой и числом...)
digit = int(input('Введите трехзначное число: '))
digit1 = digit//100
digit2 = digit%100//10
digit3 = digit%100%10
print(f'Сумма цифр = {digit1+digit2+digit3}\n'
      f'Произведение цифр = {digit1*digit2*digit3}')


# Введите трехзначное число: 235
# Сумма цифр = 10
# Произведение цифр = 30


# ИТОГ: нужно лучше, доработать — 2/4
