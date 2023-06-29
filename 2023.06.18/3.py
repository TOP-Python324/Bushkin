def numbers_strip(list_number: list, n: int = 1,*, copy: bool = False) -> list:
    """ Возвращает исходный измененный обьект списка или измененную копию """
    while n > 0:
        n -= 1
        list_number.remove(min(list_number))
        list_number.remove(max(list_number))
    if copy:
        return  list_number.copy()      
    return list_number

# >>> list_number = [1,2,3,4,5,6,7]
# >>> list_number_stripped = numbers_strip(list_number)
# >>> list_number_stripped
# [2, 3, 4, 5, 6]
# >>> list_number is list_number_stripped
# True

# >>> list_number = [1,2,3,4,5,6,7]
# >>> list_number_stripped = numbers_strip(list_number, 3, copy=True)
# >>> list_number_stripped
# [4]
# >>> list_number is list_number_stripped
# False