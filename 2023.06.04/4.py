n = int(input('Введите число разрядности: '))
count = 0
j = 1
for number in range(int('1'+'0'*(n-1))+1,int('1'+'0'*n)):
    while True:
        j = j + 1
        if (number%j == 0) and (number > j):
            j = 1
            break  
        if (number%j == 0) and (number == j ):
            count += 1
            j =  1         
            break       
print(f'Простых чисел в {n}-х разрядных\n'
      f'числах: {count}')
  

# Введите число разрядности: 3
# Простых чисел в 3-х разрядных
# числах: 143  
            
           