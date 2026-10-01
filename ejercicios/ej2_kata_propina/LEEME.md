# Ejercicio 2 — "Rojo primero": kata de la propina (en equipo)

**Historia.** Como cliente de CaféYa, yo quiero agregar propina al pagar, para
agradecer al barista.

**Reglas que dio el Product Owner:**
1. La propina es un **porcentaje del subtotal**.
2. Solo se permiten **0 %, 10 %, 15 % y 20 %**.
3. Cualquier otro porcentaje se rechaza (`ValueError`).
4. El resultado se redondea a **2 decimales**.

**Cómo trabajar (TDD en pares, como pide el material):**
- Una persona escribe la prueba y la otra el código; cambien de rol en cada vuelta.
- En cada vuelta: **escribe 1 prueba → córrela y confirma que FALLA → escribe el mínimo
  código → córrela en VERDE → refactoriza si hace falta.**
- Anoten en una tabla cada vuelta: *prueba escrita · por qué falló · qué cambiaron*.

**Archivos:** crea `test_propina.py` (las pruebas) y `propina.py` (la función
`calcular_propina(subtotal, porcentaje)`) en esta carpeta.

```
python -m pytest ejercicios/ej2_kata_propina -v
```

**Meta mínima:** 4 pruebas en verde (una por regla). **Extra:** una tabla de ejemplos con
`@pytest.mark.parametrize` y una prueba de que 25 % es rechazado con `pytest.raises`.
