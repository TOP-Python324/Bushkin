number = input('\t Введите трехзначное число : ')
number1 = int(number)//100
number2 = (int(number)%100)//10
number3 = (int(number)%100)%10
print(f'\n\t Сумма цифр = {number1+number2+number3}')
print(f'\t Произведение цифр = {number1*number2*number3}')
  #      Введите трехзначное число : 123
  #       Сумма цифр = 6
  #       Произведение цифр = 6