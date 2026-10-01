"""Clientes de CaféYa. Sirve para ilustrar los componentes de TDD (Figura 2)."""

import re

_FORMATO_CLIENTE = re.compile(r"^CY-\d{4}$")  # p. ej. CY-0042


def numero_cliente_valido(numero):
    """True si el número de cliente tiene el formato CY-#### ."""
    return bool(_FORMATO_CLIENTE.match(numero or ""))


def pedido_tiene_cliente_valido(pedido, clientes_registrados):
    """True si el pedido pertenece a un cliente registrado y con formato válido."""
    numero = pedido.get("cliente")
    return numero_cliente_valido(numero) and numero in clientes_registrados
