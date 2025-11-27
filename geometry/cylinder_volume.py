import math  # модуль math нужен для числа π


def cylinder_area(radius, height):
    """Считает площадь поверхности цилиндра и возвращает число."""  # описание функции
    if radius < 0 or height < 0:  # проверяем, что радиус и высота не отрицательные
        raise ValueError("Радиус и высота не могут быть отрицательными")  # сообщение об ошибке

    return 2 * math.pi * radius * (height + radius)  # формула S = 2πr(h + r)
