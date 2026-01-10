# 3. Pruebas unitarias y corrección del código

Este apartado es clave en la práctica, ya que permite detectar errores que no son visibles durante la ejecución normal del programa.

Se han desarrollado pruebas unitarias con **Unittest** para verificar que la aplicación cumple exactamente con todos los requisitos del enunciado.

---

## 3.1 Framework de pruebas

Se ha utilizado **Unittest**, incluido en la biblioteca estándar de Python.

📄 Archivo de pruebas:  
👉 [tests/test_lavadero_unittest.py](../tests/test_lavadero_unittest.py)

---

## 3.2 Tipos de pruebas realizadas

### ✅ Test 1 – Estado inicial
Comprueba que al crear un lavadero:
- Fase = 0 (Inactivo)
- No está ocupado
- Ingresos = 0 €
- Todas las opciones a `False`

---

### ✅ Tests 2 y 3 – Reglas de negocio
Verifican que:
- No se puede encerar sin secado a mano (`ValueError`)
- No se puede iniciar un lavado si el lavadero está ocupado (`RuntimeError`)

---

### ✅ Tests 4 a 8 – Cálculo de ingresos
Comprueban que los ingresos coinciden exactamente con los valores del enunciado:

| Opción | Ingresos |
|------|---------|
| Prelavado | 6,50 € |
| Secado a mano | 6,00 € |
| Secado + encerado | 7,20 € |
| Prelavado + secado | 7,50 € |
| Lavado completo | 8,70 € |

---

### ✅ Tests 9 a 14 – Flujo de fases
Comprueban que el lavadero pasa por las fases correctas según las opciones seleccionadas.

Ejemplo:
```python
[0, 1, 3, 4, 5, 6, 0]
