file_str = input()
files_str = file_str.split("; ")
file_count = {file:file_str.count(file) for file in files_str}  
for file in file_count:
    for i in range(0,file_count[file]):
        if i == 0:
            print(file)
        else:
            y = file.split('.')
            if len(y) == 3:
                y = [y[0], y[1]+'.'+y[2]]
            print(f'{y[0]}_{i+1}.{y[1]}')
  
# 1.py; 1.py; src.tar.gz; aux.h; main.cpp; functions.h; main.cpp; 1.py; main.cpp; src.tar.gz
# 1.py
# 1_2.py
# 1_3.py
# src.tar.gz
# src_2.tar.gz
# aux.h
# main.cpp
# main_2.cpp
# main_3.cpp
# functions.h  