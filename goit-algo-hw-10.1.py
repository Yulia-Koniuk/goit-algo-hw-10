import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize_Drink_Production", pulp.LpMaximize)

# Визначення змінних
x1 = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')  # Кількість "Лимонаду"
x2 = pulp.LpVariable('FruitJuice', lowBound=0, cat='Continuous')  # Кількість "Фруктового соку"

# Цільова функція - максимізація загальної кількості напоїв
model += x1 + x2, "TotalDrinks"

# Обмеження на ресурси
model += 2 * x1 + 1 * x2 <= 100, "WaterConstraint"  # Обмеження на воду
model += 1 * x1 <= 50, "SugarConstraint"  # Обмеження на цукор
model += 1 * x1 <= 30, "LemonJuiceConstraint"  # Обмеження на лимонний сік
model += 2 * x2 <= 40, "FruitPureeConstraint"  # Обмеження на фруктове пюре

# Розв'язання моделі
model.solve()

# Вивід результатів
print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Optimal amount of Lemonade: {pulp.value(x1)}")
print(f"Optimal amount of Fruit Juice: {pulp.value(x2)}")
print(f"Total drinks produced: {pulp.value(model.objective)}")


"""
Status: Optimal
Optimal amount of Lemonade: 30.0
Optimal amount of Fruit Juice: 20.0
Total drinks produced: 50.0
"""
