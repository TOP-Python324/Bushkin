# fibo_seguence = [1,1]
# value_seguence = int(input('Введите количество элементов: '))
# if value_seguence == 1:
    # fibo_seguence = [1]
# else:
    # for i in range(value_seguence - 2):
        # fibo_seguence.append(fibo_seguence[i] + fibo_seguence[i+1])
# print(*fibo_seguence)



fibo_seguence = [1,1]
value_seguence = int(input('Введите количество элементов: '))
if value_seguence == 1:
    fibo_seguence = [1]
else:
    fibo_seguence_t = ( (fibo_seguence[i] + fibo_seguence[i+1])
                      for i in range(int(value_seguence) - 2)
    )
    fibo_seguence += fibo_seguence_t
    
print(*fibo_seguence)

# Введите количество элементов: 1
# 1 

# Введите количество элементов: 17
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597