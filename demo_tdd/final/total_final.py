"""Código que quedó al final de la demo (después del refactor)."""

CUPONES = {"ESTUDIANTE": 0.10}


def calcular_total(items, cupon=None):
    subtotal = sum(precio * cantidad for _, precio, cantidad in items)
    return round(subtotal * (1 - _descuento(cupon)), 2)


def _descuento(cupon):
    return CUPONES.get(cupon, 0) if cupon else 0
