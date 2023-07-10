def logger(func_obg: 'callable') -> 'callable':
    def wrapper(*arg,**kwarg):
        if kwarg == {}:
            kwarg_func = func_obg.__kwdefaults__
        else:
            kwarg_func=kwarg
            for key,value in func_obg.__kwdefaults__.items():       
                if key not in kwarg:
                    kwarg_func[key]=value  
        kwargs=tuple((key+'='+str(value)) for key,value in kwarg_func.items())
        arguments=arg+kwargs
        try:
            result = func_obg(*arg,**kwarg)
        except Exception as exception:
            print(f'{func_obg.__name__}({arguments}) -> ')
            print(f'{exception.__class__.__name__}: {exception}')
        else:
            print(f'{func_obg.__name__} {arguments} -> {result}')
            return result
    return wrapper
    

@logger
def div_round(num1, num2, *, digits=0):
    return round(num1 / num2, digits)    

@logger
def div_sum(a1,a2,*arg,numb=2,numb2=0):
    a=[a1,a2,*arg]
    return sum(a)/numb if numb2 == 0 else sum(a)/numb2 
    
    