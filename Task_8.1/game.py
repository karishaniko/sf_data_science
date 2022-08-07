"""Игра угадай число.
Компьютер сам загадывает и угадывает число
Угадать необходимо менее, чем за 20 попыток
"""

import numpy as np
def random_predict(number:int=np.random.randint(1, 101)) -> int:
    """Рандомно угадываем число
    Args:
        number (int, optional): Загаданное число. По умолчанию рандомно загадывается компьютером в диапазоне 1-100.
    Returns:
        int: Число попыток
    """
    count = 0
    limit_min = 0
    limit_max = 100
    predict_number = np.random.randint(1, 101) # предполагаемое число
    while True:
        count += 1
        if predict_number > number:
            limit_max = predict_number - 1
            predict_number = (limit_max + limit_min) // 2
        elif predict_number < number:
            limit_min = predict_number + 1
            predict_number = (limit_max + limit_min) // 2
        else:
            print(f'Это было число = {number}')
            break  # выход из цикла, если угадали
    return count

