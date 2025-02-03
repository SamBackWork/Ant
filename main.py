# -*- coding: utf-8 -*-
from collections import deque


# Функция для вычисления суммы цифр числа
def sum_of_digits(n):
    return sum(int(d) for d in str(abs(n)))  # Преобразуем число в строку и суммируем его цифры


# Функция для проверки, доступна ли клетка
def is_accessible(x, y):
    return sum_of_digits(x) + sum_of_digits(y) <= 25  # Проверяем, чтобы сумма цифр координат была <= 25


# Основная функция для подсчета доступных клеток
def count_accessible_cells(start_x, start_y):
    visited = set()  # Множество для хранения посещенных клеток
    queue = deque()  # Очередь для обхода в ширину (BFS)
    queue.append((start_x, start_y))  # Добавляем начальную клетку в очередь
    visited.add((start_x, start_y))  # Отмечаем начальную клетку как посещенную

    # Возможные направления движения: вверх, вниз, влево, вправо
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Пока очередь не пуста, продолжаем обход
    while queue:
        x, y = queue.popleft()  # Извлекаем текущую клетку из очереди

        # Проверяем все возможные направления
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy  # Вычисляем новую координату

            # Если новая клетка не посещена и доступна, добавляем её в очередь и отмечаем как посещенную
            if (new_x, new_y) not in visited and is_accessible(new_x, new_y):
                visited.add((new_x, new_y))
                queue.append((new_x, new_y))

    # Возвращаем количество доступных клеток
    return len(visited)


# Начальные координаты муравья
start_x, start_y = 1000, 1000

# Выводим количество доступных клеток
print(count_accessible_cells(start_x, start_y))
