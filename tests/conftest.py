"""PRUEBAS FIJAS (test fixtures) — Figura 2 del material.

"Objetos compartidos entre diferentes casos de prueba que especifican
condiciones previas y posteriores a una prueba."
Aquí: un conjunto de clientes y pedidos de prueba (Fixture: set of test
orders and customers). Cualquier prueba que pida `clientes` o `pedidos`
por nombre los recibe listos.
"""

import pytest


@pytest.fixture
def clientes():
    # Condición previa: estos clientes existen en el sistema.
    return {"CY-0001", "CY-0042"}


@pytest.fixture
def pedidos():
    return {
        "de_ana": {"cliente": "CY-0001", "items": [("Latte", 45, 1)]},
        "sin_registro": {"cliente": "CY-9999", "items": [("Americano", 35, 1)]},
        "mal_formato": {"cliente": "0042", "items": [("Moka", 55, 2)]},
    }


@pytest.fixture
def pedido_temporal(tmp_path):
    # Condición previa: se crea un archivo de pedido...
    archivo = tmp_path / "pedido.txt"
    archivo.write_text("Latte,45,1")
    yield archivo
    # ...y condición POSTERIOR: pytest limpia al terminar (todo lo que va
    # después del yield corre al final de la prueba).
    archivo.unlink(missing_ok=True)
