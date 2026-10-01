"""CASO DE PRUEBA "Order test" de la Figura 2  →  assertHasValidCustomer().

Fíjate: estas pruebas no crean sus datos; los PIDEN por nombre
(`clientes`, `pedidos`) y pytest les entrega la prueba fija de conftest.py.
"""

import pytest

from cafeya.clientes import pedido_tiene_cliente_valido

pytestmark = pytest.mark.unitaria


def test_pedido_tiene_cliente_valido(pedidos, clientes):
    assert pedido_tiene_cliente_valido(pedidos["de_ana"], clientes)


def test_pedido_de_cliente_no_registrado(pedidos, clientes):
    assert not pedido_tiene_cliente_valido(pedidos["sin_registro"], clientes)


def test_pedido_con_numero_mal_formado(pedidos, clientes):
    assert not pedido_tiene_cliente_valido(pedidos["mal_formato"], clientes)


def test_lee_pedido_de_archivo(pedido_temporal):
    producto, precio, cantidad = pedido_temporal.read_text().split(",")
    assert (producto, int(precio), int(cantidad)) == ("Latte", 45, 1)
