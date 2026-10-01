"""PRUEBA DE ACEPTACIÓN: el escenario del Tema 7, ahora ejecutable.

    Dado que un comprador sea un <categoría de comprador>
        Y que el comprador seleccione un pasaje mensual
    Cuando el comprador pague
    Entonces ocurrirá una venta por la cantidad de <precio>
    Ejemplos:
    | CATEGORIA    | PRECIO |
    | Estudiante   | $8     |
    | Adulto mayor | $8     |
    | Normal       | $12    |

La tabla de "Ejemplos" se convierte, fila por fila, en @pytest.mark.parametrize:
el cliente puede leer la tabla y el equipo la puede ejecutar.
"""

import pytest

from cafeya.pasaje import vender_pasaje_mensual

pytestmark = pytest.mark.aceptacion


@pytest.mark.parametrize(
    "categoria, precio",
    [
        ("Estudiante", 8),
        ("Adulto mayor", 8),
        ("Normal", 12),
    ],
)
def test_venta_de_pasaje_mensual(categoria, precio):
    # Dado que un comprador sea <categoria> y seleccione un pasaje mensual
    comprador = categoria
    # Cuando el comprador pague
    venta = vender_pasaje_mensual(comprador)
    # Entonces ocurrirá una venta por la cantidad de <precio>
    assert venta == precio
