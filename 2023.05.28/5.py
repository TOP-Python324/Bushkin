chess_cage_one = input('Введите первую клетку доски: ')
chess_cage_two = input('Введите вторую клетку доски: ')
if chess_cage_one[0] == chess_cage_two[0]  or \
   chess_cage_one[1] == chess_cage_two[1] :
    print('да')
else:
    print('нет')
    
# Введите первую клетку доски: a3
# Введите вторую клетку доски: f3
# да

# Введите первую клетку доски: d2
# Введите вторую клетку доски: f4
# нет