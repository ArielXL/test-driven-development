"""Pruebas unitarias que NACIERON en la demo de TDD (rojo → verde → refactor).

Cada prueba se escribió ANTES que el código que la hace pasar.
"""

import pytest

from cafeya.pedido import calcular_total

pytestmark = pytest.mark.unitaria


def test_pedido_vacio_cuesta_cero():
    assert calcular_total([]) == 0


def test_un_producto():
    assert calcular_total([("Latte", 45, 1)]) == 45


def test_varios_productos_con_cantidad():
    assert calcular_total([("Latte", 45, 2), ("Pan", 30, 1)]) == 120


def test_cupon_estudiante_descuenta_10_por_ciento():
    assert calcular_total([("Latte", 45, 2)], cupon="ESTUDIANTE") == pytest.approx(81)


def test_cupon_inexistente_no_descuenta():
    assert calcular_total([("Latte", 45, 1)], cupon="GRATIS") == 45
