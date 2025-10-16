import numpy as np
W_1 = 600
d_1 = 0.0085
nu = 50
nu_0 = 4 * np.pi * (10 ** (-7))
R_average = 3.8e-2  # 3.8 см → 0.038 м
L = 20e-2  # 22 см → 0.22 м




def get_B(E: np.array) -> np.array:
    res = 2 * E / (d_1 * d_1 * np.pi * np.pi * nu * W_1)
    # print((2 / (d_1 * d_1 * np.pi * np.pi * nu * W_1)) ** (-1))
    return res

def get_theoretical_B(x: np.array) -> np.array:
    I = 1  # Ампер
    N = 3000

    # Переведем x в метры, если он в см
    x_m = x * 1e-2

    B = nu_0 * I * N / (2 * L) * (
        x_m / np.sqrt(x_m**2 + R_average**2) -
        (x_m - L) / np.sqrt(R_average**2 + (x_m - L)**2)
    )
    return B



def get_Relative_delta(B: np.array) -> np.array:
    return B*0.03

mu0 = 4 * np.pi * 1e-7


def B_formula(x_m: np.ndarray, I: float, N: float, L: float, R: float) -> np.ndarray:
    """Осевая теоретическая формула B(x). x_m, L, R в метрах."""
    term = x_m / np.sqrt(x_m**2 + R**2) - (x_m - L) / np.sqrt((x_m - L)**2 + R**2)
    return mu0 * I * N / (2.0 * L) * term


def get_delta_B(
    x_cm: np.ndarray,
    I: float = 1.0,
    N: float = 3000.0,
    L_m: float = 0.20,
    R_m: float = 0.038,
    dI: float = 0.1,
    dN: float = 1.0,
    dL: float = 1e-3,
    dR: float = 1e-4,
    dx: float = 1e-3,
    rel_model_uncert: float = 0.03
) -> np.ndarray:
    """
    Возвращает абсолютную погрешность dB(x) для каждого x (x_cm — в сантиметрах).
    Параметры:
      - I, N, L_m, R_m: номинальные параметры (L_m и R_m в метрах)
      - dI, dN, dL, dR, dx: абсолютные погрешности соответствующих параметров (в тех же единицах: A, витки, м, м, м)
      - rel_model_uncert: дополнительная относительная погрешность модели (по умолчанию 3%)
    Возвращает: dB (массив той же формы, что x_cm) — абсолютные погрешности в Тл.
    """
    # перевод x в метры
    x_m = np.asarray(x_cm) * 1e-2

    # номинальное B
    B0 = B_formula(x_m, I, N, L_m, R_m)

    # вычисляем вклад от каждого параметра численно (прямыми приращениями)
    # dB_I
    B_I_plus = B_formula(x_m, I + dI, N, L_m, R_m)
    dB_I = np.abs(B_I_plus - B0)

    # dB_N
    B_N_plus = B_formula(x_m, I, N + dN, L_m, R_m)
    dB_N = np.abs(B_N_plus - B0)

    # dB_L (L участвует в prefactor и в (x-L) -> меняем L на L + dL)
    B_L_plus = B_formula(x_m, I, N, L_m + dL, R_m)
    dB_L = np.abs(B_L_plus - B0)

    # dB_R
    B_R_plus = B_formula(x_m, I, N, L_m, R_m + dR)
    dB_R = np.abs(B_R_plus - B0)

    # dB_x (позиционная неопределённость): смещаем x на +dx
    B_x_plus = B_formula(x_m + dx, I, N, L_m, R_m)
    dB_x = np.abs(B_x_plus - B0)

    # модельная относительная погрешность (например, 3% от B)
    dB_model = np.abs(B0) * rel_model_uncert

    # объединяем квадратично
    dB_total = np.sqrt(dB_I**2 + dB_N**2 + dB_L**2 + dB_R**2 + dB_x**2 + dB_model**2)

    return dB_total
