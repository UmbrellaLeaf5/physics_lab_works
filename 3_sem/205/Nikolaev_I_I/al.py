from experemental_data import wood, aluminium, stalinium
import numpy as np

# Снаружи поля нет, только внутри катушки смотрим
print(np.mean((aluminium / wood)[:21]) * 100, " %") 