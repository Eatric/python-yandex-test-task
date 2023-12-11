from app.delivery_enums import Dimensions, ServiceWorkload
from app.delivery_constants import FRAGILE_ADDITIONAL_COST, MIN_DELIVERY_COST


def calculate_delivery_cost(distance, dimension, is_fragile, service_workload):
    # Метод расчета добавочной стоимости в зависимости от расстояния
    def calculate_distance_cost(distance_):
        if distance_ > 30:
            return 300
        elif distance_ > 10:
            return 200
        elif distance_ > 2:
            return 100
        return 50

    current_cost = 0

    if not isinstance(distance, float) and not isinstance(distance, int):
        raise TypeError("Argument distance should be float/int type.")

    if not isinstance(dimension, Dimensions):
        raise TypeError("Argument dimension should be Dimensions(Enum) type.")

    if not isinstance(is_fragile, bool):
        raise TypeError("Argument is_fragile should be bool type.")

    if not isinstance(service_workload, ServiceWorkload):
        raise TypeError("Argument service_workload should be ServiceWorkload(Enum) type.")

    if distance > 30 and is_fragile:
        raise ValueError("You cannot deliver fragile items over a distance of more than 30 kilometers.")

    if distance <= 0:
        raise ValueError("Argument distance cannot be lower or equal zero.")

    # Добавление стоимости в зависимости от расстояния
    current_cost += calculate_distance_cost(distance)

    # Добавление стоимости в зависимости от размера посылки
    current_cost += dimension.value

    # Добавление стоимости, если хрупкий товар
    if is_fragile:
        current_cost += FRAGILE_ADDITIONAL_COST

    # Увеличение стоимости, в зависимости от нагрузки на сервис
    current_cost = current_cost * service_workload.value

    # Если стоимость доставки меньше минимальной, возвращаем минимальное
    if current_cost < MIN_DELIVERY_COST:
        return MIN_DELIVERY_COST

    return current_cost
