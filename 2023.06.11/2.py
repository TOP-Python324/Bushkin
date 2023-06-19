list_fruits = []
while True:
    fruit = input('Введите фрукт: ')
    if fruit:
        list_fruits.append(fruit)
    else:
        break
leng_fruits = len(list_fruits)
str_fruits = list_fruits[0]
for i in range(1,leng_fruits ):
    if i == (leng_fruits - 1):
        list_fruits[i] = ' и ' + list_fruits[i] 
    else:
        list_fruits[i] = ', ' + list_fruits[i] 
    str_fruits += (list_fruits[i])
print(str_fruits)

# Введите фрукт: яблоко
# Введите фрукт: груша
# Введите фрукт: айва
# Введите фрукт: слива
# Введите фрукт:
# яблоко, груша, айва и слива

# Введите фрукт: яблоко
# Введите фрукт: груша
# Введите фрукт:
# яблоко и груша

# Введите фрукт: яблоко
# Введите фрукт:
# яблоко