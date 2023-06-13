
numbers=[ int(char)  for char in input('Введите номер билета: ')]
if sum(numbers[0:3]) == sum(numbers[3:]):
    print('Да')
else:     
    print('Нет')
    
# Введите номер билета: 123122
# Нет
# Введите номер билета: 121121
# Да