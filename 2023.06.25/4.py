def repeat(func_obj: 'callable') -> 'callable':
    def wrapper(*args, **kwargs):
        for _ in range(10):
            result = func_obj(*args, **kwargs)
        return result
    return wrapper
    


# >>> def testing_function():
# ...     print('python')
# ...
# >>> testing_function = repeat(testing_function)
# >>>
# >>> testing_function()
# python
# python
# python
# python
# python
# python
# python
# python
# python
# python
