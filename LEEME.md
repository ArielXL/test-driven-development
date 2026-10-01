# Código del Tema 8 — Pruebas de aceptación (CaféYa)

Proyecto de ingeniería de software · Tecmilenio · Sesión 8

## Preparar (una sola vez)

```bash
python -m pip install -r requirements.txt   # instala pytest
```

## Qué hay aquí

| Carpeta / archivo | Qué ilustra del material |
|---|---|
| `cafeya/` | El "sistema" de CaféYa: total del pedido, clientes, pasaje mensual |
| `tests/conftest.py` | **Pruebas fijas** (*test fixtures*): clientes y pedidos de prueba compartidos |
| `tests/test_clientes.py`, `tests/test_pedidos.py` | **Casos de prueba** de la Figura 2 (*Customer test*, *Order test*) |
| `tests/test_total_pedido.py` | **Pruebas unitarias** que nacieron con TDD |
| `tests/test_regresion.py` | **Prueba de regresión** (bug #17 que no debe volver) |
| `tests/test_aceptacion_*.py` | **Pruebas de aceptación**: escenarios Dado-Cuando-Entonces del Tema 7 hechos ejecutables |
| `pytest.ini` | **Suites** (marcas `unitaria`, `aceptacion`, `regresion`) y el **arnés** (pytest) |
| `demo_tdd/inicio` | Punto de partida de la demo en vivo de TDD |
| `demo_tdd/final` | Cómo queda la demo al terminar |
| `ejercicios/` | Ejercicios 1, 2 y 3 de la clase |

## Comandos útiles

```bash
python -m pytest                    # el arnés corre TODAS las pruebas y reporta
python -m pytest -m aceptacion      # solo la suite de aceptación
python -m pytest -m regresion       # solo la suite de regresión
python -m pytest demo_tdd/final     # la demo terminada
python -m pytest ejercicios/ej1_lee_el_rojo   # ¡este sale en rojo a propósito!
```
