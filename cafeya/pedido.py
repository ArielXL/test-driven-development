"""Reglas de cobro de CaféYa (Ana, Beto y Carla).

Este es el código que queda al TERMINAR la demo de TDD de la clase:
cada línea existe porque primero hubo una prueba que la pidió.
"""

CUPONES = {"ESTUDIANTE": 0.10}  # 10 % de descuento


def calcular_total(items, cupon=None):
    """Regresa el total a cobrar de un pedido.

    items: lista de tuplas (producto, precio_unitario, cantidad)
    cupon: texto opcional; hoy solo existe "ESTUDIANTE" (10 %).
    """
    subtotal = sum(precio * cantidad for _, precio, cantidad in items)
    return round(subtotal * (1 - _descuento(cupon)), 2)


def _descuento(cupon):
    if cupon is None:
        return 0
    # Bug #17 (corregido): "estudiante" en minúsculas no aplicaba descuento.
    return CUPONES.get(cupon.strip().upper(), 0)
