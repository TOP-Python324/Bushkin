ranks = ('a','b','c','d','e','f','g','h') # разметка шахмматной доски по горизонтали
chess_cage_one = input('Введите первую клетку доски: ')
chess_cage_two = input('Введите вторую клетку доски: ')
multiply_g = (int(chess_cage_one[1]) - \
              int(chess_cage_two[1]))%2
multiply_v = (ranks.index(chess_cage_one[0]) - \
              ranks.index(chess_cage_two[0]))%2
if not multiply_g and not multiply_v or \
       multiply_g and multiply_v :
    print('да')
else:
    print('нет')
    
# Введите первую клетку доски: a1
# Введите вторую клетку доски: b2
# да

# Введите первую клетку доски: h8
# Введите вторую клетку доски: f7
# нет