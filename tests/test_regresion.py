"""PRUEBAS DE REGRESIÓN.

"Ayudan a identificar que ninguna funcionalidad anterior del sistema haya
sido afectada al agregar una nueva."

Bug #17 (reportado por Carla en el sprint 3): si el cliente escribía el
cupón en minúsculas ("estudiante") NO se aplicaba el descuento.
Se corrigió y se dejó esta prueba para que el defecto no regrese nunca,
aunque alguien reescriba _descuento() en el futuro.
"""

import pytest

from cafeya.pedido import calcular_total

pytestmark = pytest.mark.regresion


@pytest.mark.parametrize("cupon", ["estudiante", "Estudiante", "  ESTUDIANTE  "])
def test_bug17_cupon_sin_importar_mayusculas_ni_espacios(cupon):
    assert calcular_total([("Latte", 45, 2)], cupon=cupon) == pytest.approx(81)
