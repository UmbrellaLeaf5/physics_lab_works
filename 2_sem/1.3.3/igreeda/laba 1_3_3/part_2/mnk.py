import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")

l = 0.4

L = np.array(list(map(float, input("Введите данные о расходе трубки Q:\n").split())))

P = np.array(list(map(float, input("Введите данные о изменении давления ΔP:\n").split())))
""" мои значения:

1: Трубка 1

-----


2: Трубка 2
---



3: Трубка 3

"""

mean_q = np.mean(L)
mean_p = np.mean(P)
mean_qq = np.mean(L * L)
mean_qp = np.mean(L * P)

print(f"Среднее значение L={mean_q}")
print(f"Среднее значение ΔP={mean_p}")
print(f"Среднее значение L^2={mean_qq}")
print(f"Среднее значение L*P={mean_qp}")


k = (mean_qp - mean_q*mean_p)/(mean_qq - mean_q*mean_q)
print(f"Коэффициент k={k}")

b = mean_p - k * mean_q
print(f"Коэффициент b={b}")

print(f"Уравнение МНК для данной трубки:\ny={round(k, 1)}x {round(b, 1)}")



_, axis = plt.subplots(figsize=(16, 9))
axis: plt.Axes = axis

axis.plot(L, k * L + b, color="blue")
axis.set_title(f"{round(k, 1)}x {round(b, 1)}", fontsize=17, fontweight="bold", c="dimgray")

_.savefig(f"{round(k, 1)}x {round(b, 1)}.png", bbox_inches="tight")
