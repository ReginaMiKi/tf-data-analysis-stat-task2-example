import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 730773348 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    loc = x.mean()
    mean = np.mean(x**2)
    return loc - mean/scipy.stats.chi2.ppf(1-alpha/2, df=1) / 0.39, \
           loc - mean/scipy.stats.chi2.ppf(alpha/2, df=1) / 0.39
