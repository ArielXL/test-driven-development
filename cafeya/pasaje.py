"""Precio del pasaje mensual de camión: el escenario del Tema 7, ahora ejecutable."""

PRECIOS_PASAJE_MENSUAL = {
    "Estudiante": 8,
    "Adulto mayor": 8,
    "Normal": 12,
}


def vender_pasaje_mensual(categoria):
    """Regresa el monto de la venta del pasaje mensual para una categoría de comprador."""
    if categoria not in PRECIOS_PASAJE_MENSUAL:
        raise ValueError(f"Categoría desconocida: {categoria}")
    return PRECIOS_PASAJE_MENSUAL[categoria]
