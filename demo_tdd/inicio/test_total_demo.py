"""DEMO EN VIVO DE TDD — punto de partida (archivo casi vacío a propósito).

Historia: Como cliente de CaféYa, yo quiero ver el total de mi pedido,
          para saber cuánto voy a pagar.

Guion (Figura 3 del material):
  1. Add a test   → escribe UNA prueba aquí abajo.
  2. Run the test → debe FALLAR (rojo). Si pasa, la prueba no sirve.
  3. Make a little change → el MÍNIMO código en total_demo.py.
  4. Run the test → verde. Refactoriza si hace falta. Repite.

Corre desde la carpeta codigo_tema8:
    python -m pytest demo_tdd/inicio -v
"""

from total_demo import calcular_total  # noqa: F401  (todavía no existe → primer ROJO)


# Paso 1: escribe aquí tu primera prueba, por ejemplo:
# def test_pedido_vacio_cuesta_cero():
#     assert calcular_total([]) == 0
