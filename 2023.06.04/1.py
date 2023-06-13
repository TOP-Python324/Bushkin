list_number = []
print('Вводите числа:')
while True:
    number = input()
    if int(number) % 7  ==  0:
        list_number.append(number)
    else: 
        break
print('Список чисел: ')
print(*list_number[::-1])

# Вводите числа:
# 7
# 14
# 21
# 7
# 63
# 13
# Список чисел:
# 63 7 21 14 7