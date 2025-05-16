import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.kernel_ridge import KernelRidge
from sklearn.svm import SVR
from sklearn.ensemble import GradientBoostingRegressor
import random

# 1. Генерируем исходную функцию (нелинейную)
def f(x):
    return np.sin(x) + 0.5 * np.sqrt(x)

# 2. Генерируем данные с шумом
np.random.seed(42)
random.seed(42)
x_min, x_max = 0.1, 10
x = np.linspace(x_min, x_max, 100)
y = f(x) + np.array([random.uniform(-0.3, 0.3) for _ in range(100)])

# Преобразуем x в двумерный массив для sklearn
X = x.reshape(-1, 1)

# 3. Инициализация моделей
models = {
    "Kernel Ridge": KernelRidge(alpha=1.0, kernel='rbf', gamma=0.1),
    "SVR": SVR(kernel='rbf', C=100, gamma=0.1, epsilon=0.1),
    "Gradient Boosting": GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3)
}

# 4. Обучение моделей и предсказание
results = {}
for name, model in models.items():
    model.fit(X, y)
    y_pred = model.predict(X)
    mse = mean_squared_error(y, y_pred)
    results[name] = {"model": model, "y_pred": y_pred, "mse": mse}

# 5. Визуализация
plt.figure(figsize=(18, 5))
for i, (name, result) in enumerate(results.items()):
    plt.subplot(1, 3, i+1)
    plt.scatter(x, y, color='blue', label='Исходные точки', s=10)
    plt.plot(x, f(x), color='green', label='Исходная функция')
    plt.plot(x, result["y_pred"], color='red', label=f'Предсказание ({name})')
    plt.title(f'{name}\nMSE: {result["mse"]:.4f}')
    plt.legend()
    plt.grid(True)

plt.tight_layout()
plt.show()

# 6. Выводы
print("Среднеквадратичные ошибки (MSE):")
for name, result in results.items():
    print(f"{name}: {result['mse']:.4f}")