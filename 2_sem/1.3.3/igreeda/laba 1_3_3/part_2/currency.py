import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")

l = 0.4

L = np.array(list(map(int, input("Введите данные о расходе трубки Q:\n").split())))

P = np.array(list(map(int, input("Введите данные о изменении давления ΔP:\n").split())))

mean_q = np.mean(L)
mean_p = np.mean(P)
mean_qq = np.mean(L * L)
mean_pp = np.mean(P * P)
mean_qp = np.mean(L * P)



k = (mean_qp - mean_q*mean_p)/(mean_qq - mean_q*mean_q)


dk = (1 / (np.sqrt(6))) * np.sqrt(  (  (mean_pp - mean_p*mean_p)/(mean_qq - mean_q*mean_q)   )   - k*k)
print(f"delta K = {dk}")

db = dk * np.sqrt(  mean_qq - mean_q*mean_q   )
print(f"delta b = {db}")