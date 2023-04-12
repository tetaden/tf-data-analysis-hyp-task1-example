import pandas as pd
import numpy as np
from scipy.stats import norm

chat_id = 415542660 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    conv_ctr = x_success / x_cnt
    conv_test = y_success / y_cnt
    
    se = np.sqrt(conv_ctr * (1 - conv_ctr) / x_cnt + conv_test * (1 - conv_test) / y_cnt)
    
    z_stat = (conv_test - conv_ctr) / se 
    
    p_crit = norm.ppf(1 - 0.07)
    
    reject_null = z_stat > p_crit
    
    return reject_null # Ваш ответ, True или False

