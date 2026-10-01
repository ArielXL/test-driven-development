"""DEMO DE TDD — estado final (para consultar después de la clase).

Cada prueba corresponde a una vuelta del ciclo rojo → verde → refactor.
"""

import pytest

from total_final import calcular_total


# Vuelta 1 — rojo: ImportError. Verde: def calcular_total(items): return 0
def test_pedido_vacio_cuesta_cero():
    assert calcular_total([]) == 0


# Vuelta 2 — rojo: esperaba 45, obtuvo 0. Verde: return items[0][1] ... (¡trampa válida!)
def test_un_producto():
    assert calcular_total([("Latte", 45, 1)]) == 45


# Vuelta 3 — rojo: la "trampa" ya no alcanza. Verde: sumar precio * cantidad.
def test_varios_productos_con_cantidad():
    assert calcular_total([("Latte", 45, 2), ("Pan", 30, 1)]) == 120


# Vuelta 4 — rojo: TypeError (no acepta cupón). Verde: parámetro cupon.
# Refactor: se extrae _descuento() sin cambiar el comportamiento (las 4 siguen en verde).
def test_cupon_estudiante_descuenta_10_por_ciento():
    assert calcular_total([("Latte", 45, 2)], cupon="ESTUDIANTE") == pytest.approx(81)
