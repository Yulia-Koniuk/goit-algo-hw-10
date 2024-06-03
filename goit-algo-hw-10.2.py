import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Метод Монте-Карло для оцінки площі під кривою
n_points = 1000000
x_points = np.random.uniform(a, b, n_points)
y_points = np.random.uniform(0, f(b), n_points)
points_under_curve = sum(y_points <= f(x_points))
ratio = points_under_curve / n_points
rectangle_area = (b - a) * f(b)
area_under_curve_mc = ratio * rectangle_area

# Перевірка: обчислення інтеграла за допомогою методу quad
result_quad, error_quad = spi.quad(f, a, b)

print("Обчислення значення інтеграла за допомогою методу Монте-Карло:", area_under_curve_mc)
print("Перевірка: обчислення інтеграла за допомогою quad:", result_quad)


"""
Обчислення значення інтеграла за допомогою методу Монте-Карло: 2.660104
Перевірка: обчислення інтеграла за допомогою quad: 2.666666666666667
"""