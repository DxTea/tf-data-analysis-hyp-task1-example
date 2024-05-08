import pandas as pd
import numpy as np
from scipy.stats import norm

chat_id = 468441161 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Вычисляем доли
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt

    # Вычисляем общую долю успехов
    P = (x_success + y_success) / (x_cnt + y_cnt)

    # Вычисляем z-статистику
    z = (p1 - p2) / np.sqrt(P * (1 - P) * (1/x_cnt + 1/y_cnt))

    # Вычисляем p-value
    p_value = 2 * (1 - norm.cdf(abs(z)))

    # Отклоняем нулевую гипотезу, если p-value меньше уровня значимости
    return p_value < 0.1
