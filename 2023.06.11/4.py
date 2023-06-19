code_dict_reverse = {}
while True:
    key_value = input()
    if key_value!='':
        code_dict_reverse[(key_value).split(' ')[1]] = (key_value).split(' ')[0]
    else:
        break
value = input()
if value in code_dict_reverse:
    print(code_dict_reverse[value])
else:
    print('! value error !')


# 1004 ER_CANT_CREATE_FILE
# 1005 ER_CANT_CREATE_TABLE
# 1006 ER_CANT_CREATE_DB
# 1007 ER_DB_CREATE_EXISTS
# 1008 ER_DB_DROP_EXISTS1010 ER_DB_DROP_RMDIR

# ER_CANT_CREATE_TABLE
# 1005


# 1004 ER_CANT_CREATE_FILE
# 1005 ER_CANT_CREATE_TABLE
# 1006 ER_CANT_CREATE_DB

# ER_DB_DROP_EXISTS1010 ER_DB_DROP_RMDIR
# ! value error !