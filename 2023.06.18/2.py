def taxi_cost(length: int,waiting: int =0) -> int | None:
    """ Вычисление стоимости поездки """
    if length < 0 or waiting < 0:
        return None
    cost = 80 + length/150*6 + waiting*3 if length > 0 else 160 + waiting*3
    return round(cost)
    
    
# >>> taxi_cost(1500)
# 140
# >>> taxi_cost(2560)
# 182
# >>> taxi_cost(0, 5)
# 175
# >>> taxi_cost(42130, 8)
# 1789
# >>> print(taxi_cost(-300))
# None
# >>>