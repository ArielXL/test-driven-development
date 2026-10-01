"""PRUEBA DE ACEPTACIÓN de CaféYa (el escenario del Ejercicio 3 del Tema 7).

Historia: Como cliente de CaféYa, yo quiero pagar en la app,
          para recoger sin pasar por caja.

    Dado que el cliente tiene un pedido en el carrito
        Y que tiene un método de pago válido
    Cuando el cliente confirma el pago
    Entonces el sistema cobra el total
        Y genera el comprobante del pedido
"""

import pytest

from cafeya.pedido import calcular_total

pytestmark = pytest.mark.aceptacion


def confirmar_pago(carrito, metodo_pago_valido):
    """Simulación mínima del sistema de pago para la clase."""
    if not metodo_pago_valido:
        return {"cobrado": 0, "comprobante": None}
    total = calcular_total(carrito)
    return {"cobrado": total, "comprobante": f"CY-TICKET-{total}"}


def test_cliente_paga_en_la_app():
    # Dado que el cliente tiene un pedido en el carrito y un método de pago válido
    carrito = [("Latte", 45, 1), ("Pan", 30, 1)]
    # Cuando el cliente confirma el pago
    resultado = confirmar_pago(carrito, metodo_pago_valido=True)
    # Entonces el sistema cobra el total y genera el comprobante
    assert resultado["cobrado"] == 75
    assert resultado["comprobante"] is not None


def test_sin_metodo_de_pago_no_se_cobra():
    carrito = [("Latte", 45, 1)]
    resultado = confirmar_pago(carrito, metodo_pago_valido=False)
    assert resultado == {"cobrado": 0, "comprobante": None}
