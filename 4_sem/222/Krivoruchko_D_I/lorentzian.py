from typing import Callable
import numpy as np


def Lorentzian(f: float,
               f_0: float,
               A_max: float,
               gamma: float) -> float:
    """
    Функция Лоренца.

    Args:
        f (float): частота, на которой вычисляется значение.
        f_0 (float): резонансная частота.
        A_max (float): максимальная амплитуда.
        gamma (float): ширина резонанса.

    Returns:
        float: значение функции Лоренца на частоте f.
    """

    return A_max / (1 + (2 * (f - f_0) / gamma)**2)


def ApproximateResonanceCurve(f_0: float,
                              f_1: float,
                              f_2: float,
                              A_max: float = 1
                              ) -> tuple[Callable, float]:
    """
    Аппроксимирует резонансную кривую по трём точкам.

    Args:
        f0 (float): резонансная частота.
        f1 (float): частота слева от резонанса, где амплитуда A_max / sqrt(2).
        f2 (float): частота справа от резонанса, где амплитуда A_max / sqrt(2).
        A_max (float, optional): максимальная амплитуда. Defaults to 1.

    Returns:
        tuple[Callable, float]: функция, представляющую аппроксимированную резонансную кривую, 
                                ширина резонанса
    """

    gamma_factor = np.sqrt(np.sqrt(2) - 1)
    gamma_1 = 2 * abs(f_1 - f_0) / gamma_factor
    gamma_2 = 2 * abs(f_2 - f_0) / gamma_factor
    gamma = (gamma_1 + gamma_2) / 2

    def ResonanceCurve(f):
        return Lorentzian(f, f_0, A_max, gamma)

    return ResonanceCurve, gamma
