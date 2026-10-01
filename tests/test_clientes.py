"""CASO DE PRUEBA "Customer test" de la Figura 2  →  assertCustNumFormatValid()."""

import pytest

from cafeya.clientes import numero_cliente_valido

pytestmark = pytest.mark.unitaria


def test_formato_numero_cliente_valido():
    assert numero_cliente_valido("CY-0042")


@pytest.mark.parametrize("numero", ["0042", "CY-42", "cy-0042", "", None])
def test_formato_numero_cliente_invalido(numero):
    assert not numero_cliente_valido(numero)
