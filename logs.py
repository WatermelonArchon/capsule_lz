import pandas as pd
import uuid #чего не сделаешь ради рандома🥀, цветок пришлось с тг копировать 
import os
from datetime import datetime

def logger(func):
    def wrapper(*args, **kwargs):
        data = { # записываем всякие штучки в строку
            'id': [str(uuid.uuid4())[:8]], # очень честно нагугленный способ рандомных коротких чисел, вроде даже работает
            'pc_username': [os.getlogin()], # слизано с практики
            'function_name': [func.__name__], # очевидно имя функции, тоже слизанное с практики
            'date': [datetime.now().strftime("%Y-%m-%d")], # почти слизано с практики
            'time': [datetime.now().strftime("%H:%M:%S")] # тоже самое
        }
        # датафрейм и файлик с адекватным названием
        df = pd.DataFrame(data)
        file_name = 'log.csv'
        # запись в слишком адекватный файлик
        # header и все что там дальше для шапки таблицы чтобы было
        df.to_csv(file_name, mode='a', index=False, header=not os.path.exists(file_name), encoding='utf-8')
        return func(*args, **kwargs)
    return wrapper

# @logger
# def cringe():
#     print('✨ ъуъуъуъуъуъуъуъуъуъуъуъуъуъ ✨')
# cringe()

# ну надо было на чем-то проверить
