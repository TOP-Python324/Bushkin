ranks = 'abcdefgh'
files = '12345678'
chess_cage_one = input('Введите первую клетку доски: ')
chess_cage_two = input('Введите вторую клетку доски: ')
king_point_v = int(chess_cage_one[1]) - 1
king_point_g = ranks.index(chess_cage_one[0])
king_point_vcor , king_point_gcor = king_point_v , king_point_g
if  king_point_v == 0 :
    king_point_vcor = 1
if  king_point_g == 0 :
    king_point_gcor  = 1
if  chess_cage_two[0] in ranks[king_point_gcor -1 : king_point_g +2 ]  and \
    chess_cage_two[1] in files[king_point_vcor -1 : king_point_v +2 ] :
    print('да')
else:
    print('нет') 
    
# Введите первую клетку доски: a1
# Введите вторую клетку доски: b2
# да

# Введите первую клетку доски: h8
# Введите вторую клетку доски: g6
# нет