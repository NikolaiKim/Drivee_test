# Yakutsk
import math

# Функция для вычисления расстояния между двумя точками на плоскости (координаты)
def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Функция для поиска ближайших заказов к маршруту водителя
def find_closest_orders(driver_route, orders):
    point_a, point_b = driver_route
    closest_orders = []

    for order in orders:
        order_a, order_b = order
        distance_to_a = calculate_distance(point_a, order_a)
        distance_to_b = calculate_distance(point_b, order_b)

        # Проверяем, если заказ ближе к начальной точке маршрута водителя и к конечной точке маршрута
        # или ближе к конечной точке маршрута водителя и к начальной точке маршрута
        if (distance_to_a + distance_to_b) < (calculate_distance(point_a, point_b) + 0.1):
            closest_orders.append(order)

    return closest_orders

# Пример входных данных
driver_route = [(1, 1), (5, 5)]
orders = [((2, 2), (4, 4)), ((3, 3), (6, 6)), ((6, 6), (7, 7))]

# Поиск ближайших заказов
closest_orders = find_closest_orders(driver_route, orders)

if closest_orders:
    print("Ближайшие заказы к маршруту водителя:")
    for order in closest_orders:
        print(f"От {order[0]} до {order[1]}")
else:
    print("Нет ближайших заказов к маршруту водителя.")