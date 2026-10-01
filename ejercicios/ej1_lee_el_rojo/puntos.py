"""Programa de lealtad de CaféYa.

Regla del Product Owner: el cliente gana 1 punto por cada $10 COMPLETOS
de compra. Ejemplos: $9.99 → 0 puntos · $47 → 4 puntos · $100 → 10 puntos.
"""


def calcular_puntos(total):
    return round(total / 10)
