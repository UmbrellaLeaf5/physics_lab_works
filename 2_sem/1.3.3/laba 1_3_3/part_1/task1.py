import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")

l = 0.4

Q = np.array(list(map(int, input("Введите данные о расходе трубки Q:\n").split())))

P = np.array(list(map(int, input("Введите данные о изменении давления ΔP:\n").split())))
""" мои значения:

1: Трубка 1
67 62 56 46 40 33 20
916 884 790 655 545 419 245
0.5 0.5 0.5 0.5 0.5 0.5 0.5 
7.5 8.11 8.86 10.76 12.36 15.29 25.52
116 112 100 83 69 53 31

r_трубки = 0.002
-----


2: Трубка 2
117 109 104 94 75 51 30
710 592 419 324 261 182 95
V: 0.5 0.5 0.5 0.5 0.5 0.5 0.5
Δt: 4.27 4.55 4.8 5.34 6.65 9.73 16.6
Δh: 90 75 53 41 33 23 12

r_трубки = 0.003


---
3: Трубка 3
Q: 162 144 131 145 120 106 47
ΔP: 371 316 213 292 150 126 47
V: 0.5 0.5 0.5 0.5 0.5 0.5 0.5
Δt: 3.09 3.46 3.81 3.44 4.16 4.72 10.61
Δh: 47 40 27 37 19 16 6

r_трубки = 0.004
"""



mean_q = np.mean(Q)
mean_p = np.mean(P)
mean_qq = np.mean(Q*Q)
mean_qp = np.mean(Q*P)

print(f"Среднее значение Q={mean_q}")
print(f"Среднее значение ΔP={mean_p}")
print(f"Среднее значение Q^2={mean_qq}")
print(f"Среднее значение Q*P={mean_qp}")


k = (mean_qp - mean_q*mean_p)/(mean_qq - mean_q*mean_q)
print(f"Коэффициент k={k}")

b = mean_p - k * mean_q
print(f"Коэффициент b={b}")

print(f"Уравнение МНК для данной трубки:\ny={round(k, 1)}x {round(b, 1)}")


r = float(input("Введите значение радиуса трубки r в м"))
etta = np.pi * (r**4) * 1_000_00 * P[-1] / (8 * l * Q[-1])
print(f"{etta * (10 ** 5)} * 10^(-5)")

Re = (Q[-1] * 2 * 1200)/(np.pi * 2*r*k * 1000)
print(f"Рейнольдс: Re={Re}")

"""-----------------"""
"""Погрешности"""


dv = 0.02
dt = 0.2
dh = 0.001
V = np.array(list(map(float, input("Введите значения V:\n").split())))
t = np.array(list(map(float, input("Введите значения Δt:\n").split())))
h = np.array(list(map(float, input("Введите значения Δh:\n").split())))

mean_V = np.mean(V)
mean_t = np.mean(t)
mean_h = np.mean(h)

dq = mean_q * np.sqrt( (dv/mean_V)**2 + (dt/mean_t)**2 )
print(f"ΔQ={dq}")

dn = etta * np.sqrt( (dh/mean_h)**2 + (dq/mean_q)**2 )
print(f"Δetta = {dn}")

dRe = Re * np.sqrt( (dq/mean_q)**2 + (dn/etta)**2 )
print(f"ΔRe={dRe}")


_, axis = plt.subplots(figsize=(16, 9))
axis: plt.Axes = axis

axis.plot(Q, k*Q + b, color="blue")
# axis.set_xlim(abscissa.min(), abscissa.max());
axis.set_title(f"{round(k, 1)}x {round(b, 1)}", fontsize=17, fontweight="bold", c="dimgray")

_.savefig(f"{round(k, 1)}x {round(b, 1)}.png", bbox_inches="tight")
