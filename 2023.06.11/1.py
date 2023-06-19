adress = input()
if '@' in adress and '.' in adress.split('@')[1][2:]:
    print('да')
else:
    print('нет')
    
    
    # sgd@ya.ru
    # да
    
    # abcde@fghij
    # нет