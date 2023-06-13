amount = 0
number = int(input('Введите натуральное число: '))
list_divisors = list(range(1,number +1))
for count in list_divisors:
    if number%count == 0:
        divisor = number//count
        if divisor != count:
            amount = amount + count + divisor
            list_divisors.remove(divisor) 
        else:
            amount += count        
print(f'Сумма делителей: {amount}')

# Введите натуральное число: 9
# Сумма делителей: 13