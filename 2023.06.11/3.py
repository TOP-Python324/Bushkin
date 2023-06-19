list_number_one = [ int(number) for number in (input('Введите числа: \n')).split() ]
list_number_two = [ int(number_two) for number_two in (input('Введите числа: \n')).split() ]
leng_list_one = len(list_number_one)
leng_list_two = len(list_number_two)
while True:
    for count in range(0,leng_list_one - leng_list_two + 1):
        if list_number_one[count:count + leng_list_two] == list_number_two:
            print('да')
            break
        if count == leng_list_one - leng_list_two:
            print('нет')
    break
   
   # Введите числа:
   # 1 2 3 4 5 6
   # Введите числа:
   # 6 5 4
   # нет
   
   
   # Введите числа:
   # 1 2 3 4 5 6 7
   # Введите числа:
   # 5 6 7
   # да