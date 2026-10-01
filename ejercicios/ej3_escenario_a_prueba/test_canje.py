"""Ejercicio 3 — "Del escenario a la prueba de aceptación" (individual).

Convierte este escenario (formato del Tema 7) en UNA prueba parametrizada:

    Dado que el cliente tiene <puntos> puntos
    Cuando canjea un café de 50 puntos
    Entonces el canje es <resultado>
        Y le quedan <restantes> puntos
    Ejemplos:
    | PUNTOS | RESULTADO  | RESTANTES |
    | 120    | aprobado   | 70        |
    | 50     | aprobado   | 0         |
    | 30     | rechazado  | 30        |

Pistas:
  - Cada fila de "Ejemplos" es una tupla en @pytest.mark.parametrize.
  - Deja comentarios # Dado / # Cuando / # Entonces dentro de la prueba.
  - Corre:  python -m pytest ejercicios/ej3_escenario_a_prueba -v
"""

import pytest  # noqa: F401

from canje import canjear_cafe  # noqa: F401

# Escribe tu prueba aquí.
