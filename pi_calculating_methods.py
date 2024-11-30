import math
import random


def nilakanth_method(n=9999):
    """
    Invented by Kerala School of Mathematics in India circa 1444-1545.
    """
    temp = 0

    for i in range(1, n):
        temp += (-1) ** (i + 1) * 4 / (2 * i * (2 * i + 1) * (2 * i + 2))
    return 3 + temp


def brounckers_method(n=999999):
    """
    Invented by William Brouncker in 1655.
    """
    temp = 2

    for i in range(n, 0, -2):
        temp = i**2 / (temp + 2)

    return 4 / (1 + temp)


def leibniz_method(n=9999):
    """
    Invented by Gottfried Wilhelm Leibniz in 1673.
    """
    temp = 0

    for i in range(n):
        temp += (-1) ** i / (2 * i + 1)
    return 4 * temp


def arcus_cosinus_method():
    """
    Based by Jean le Rond d'Alembert and Leonhard Euler work (1717-1783).
    """
    return 2 * math.acos(0)


def gauss_legendre_method(n=25):
    """
    Invented by Carl Friedrich Gauss in 1808.
    """
    a = 1
    b = 1 / math.sqrt(2)
    t = 1 / 4
    p = 1

    for _ in range(n):
        a_temp = a
        a = (a + b) / 2
        b = math.sqrt(a_temp * b)
        t = t - p * (a_temp - a) ** 2
        p *= 2

    return (a + b) ** 2 / (4 * t)


def monte_carlo_method(n=999999):
    """
    Invented by Stanisław Ulam and John von Neumann in 1946.
    """
    inside = 0

    for _ in range(n):
        x = random.random()
        y = random.random()
        if x * x + y * y <= 1:
            inside += 1

    return 4 * inside / n


print(f"Gauss Legendre Method = {gauss_legendre_method()}")
print(f"Brouncker Method = {brounckers_method()}")
print(f"Monte Carlo Method = {monte_carlo_method()}")
print(f"Leibniz Method = {leibniz_method()}")
print(f"Arcus cosinus method = {arcus_cosinus_method()}")
print(f"Nilakanth method = {nilakanth_method()}")
