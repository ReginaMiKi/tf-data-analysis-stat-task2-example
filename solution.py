import pandas as pd
import numpy as np

from scipy.stats import chi2


chat_id = 730773348 # Ваш chat ID, не меняйте название переменной

def solution(p: (0, 1), x: np.ndarray) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    loc = x.mean()
    mean = np.mean(x**2)
    return loc - mean / chi2.ppf(1-alpha/2, df=1) / 0.39, \
           loc - mean / chi2.ppf(alpha/2, df=1) / 0.39
