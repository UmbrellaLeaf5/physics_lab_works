import numpy as np
import matplotlib.pyplot as plt
from experemental_data import wood, stalinium, aluminium
from Phys_func import get_B, get_theoretical_B, get_Relative_delta, get_delta_B


E1 = wood * 1e-3
E2 = aluminium * 1e-3
E3 = stalinium * 1e-3

# B1 = E1/10.69618
# B2 = E2/10.69618
# B3 = E3/10.69618

# Создаем массив индексов x
x = np.arange(len(E1))

# Строим графики
plt.figure(figsize=(12, 8))

# Наши эксперементальные точки
delta = get_Relative_delta(get_B(E1))

plt.scatter(x, get_B(E1), color='b', marker="o", label="Эксперементальные точки: Дерево")
plt.errorbar(
    x, get_B(E1),
    yerr=delta,
    fmt='none',           # Не добавляем точки, только "усы"
    ecolor='b',           # Цвет усов совпадает с линией
    elinewidth=1,         # Толщина линии погрешности
    capsize=3,            # Маленькие "шляпки" сверху и снизу
    alpha=0.6             # Прозрачность
)


plt.scatter(x, get_B(E2), color='r', marker="o", label="Эксперементальные точки: Алюминий")
plt.errorbar(
    x, get_B(E2),
    yerr=delta,
    fmt='none',           # Не добавляем точки, только "усы"
    ecolor='r',           # Цвет усов совпадает с линией
    elinewidth=1,         # Толщина линии погрешности
    capsize=3,            # Маленькие "шляпки" сверху и снизу
    alpha=0.6             # Прозрачность
)



plt.scatter(x, get_B(E3), color='g', marker="o", label="Эксперементальные точки: Сталь")
plt.errorbar(
    x, get_B(E3),
    yerr=delta,
    fmt='none',           # Не добавляем точки, только "усы"
    ecolor='g',           # Цвет усов совпадает с линией
    elinewidth=1,         # Толщина линии погрешности
    capsize=3,            # Маленькие "шляпки" сверху и снизу
    alpha=0.6             # Прозрачность
)

B_wood_Theor = get_theoretical_B(x)
print(B_wood_Theor*1000)

# тут вместо B_i нужно будет вставить теоретические данные
plt.plot(x, B_wood_Theor, 'b-', label='Теоритическая кривая B(x) для Дерева', linewidth=2)
delta = get_delta_B(x)
plt.fill_between(
    x,
    B_wood_Theor - delta,
    B_wood_Theor + delta,
    color='b',
    alpha=0.15,
    label='Погрешность теоретических данных'
)

plt.ylim(0, None)
plt.xlim(0, 34)
plt.xlabel('x, см')
plt.ylabel('B(x), мТл')
plt.title('Графики B1(x), B2(x), B3(x)')
plt.legend()
# plt.grid(True, alpha=0.3)

# Включаем более частую сетку
plt.minorticks_on()
plt.grid(which='major', color='gray', linestyle='-', linewidth=0.5, alpha=0.5)
plt.grid(which='minor', color='gray', linestyle=':', linewidth=0.3, alpha=0.3)



plt.savefig("graphs/graph.pdf")     # в PDF
plt.savefig("graphs/graph.svg")     # векторный формат SVG
plt.savefig("graphs/graph.png", dpi=300, bbox_inches='tight')
plt.show()
