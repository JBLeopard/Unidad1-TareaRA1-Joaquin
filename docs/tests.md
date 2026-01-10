# 3. Pruebas unitarias y corrección del código de la aplicación

En este apartado se documenta de forma detallada el proceso completo de **ejecución de pruebas unitarias**, **detección de errores**, **análisis de fallos** y **corrección del código** de la aplicación del lavadero.

Este apartado es clave dentro de la asignatura *Puesta en Producción Segura*, ya que demuestra el uso de pruebas automáticas como mecanismo de control de calidad y detección temprana de errores antes del despliegue de una aplicación.

---

## 3.1 Entorno de pruebas

Las pruebas se han realizado en el siguiente entorno:

- Sistema operativo: **Kali Linux**
- Lenguaje: **Python 3**
- Framework de testing: **unittest**
- Entorno virtual: `.venv`
- Editor / IDE: **Visual Studio Code**
- Terminal: Bash

📄 Archivo de pruebas unitarias:  
[`tests/test_lavadero_unittest.py`](./tests/test_lavadero_unittest.py)

📄 Archivo de la aplicación corregido:  
[`lavadero.py`](./lavadero.py)

---

## 3.2 Ejecución de las pruebas unitarias

Las pruebas se ejecutaron desde terminal utilizando el descubrimiento automático de tests:

```bash
PYTHONPATH=. python3 -m unittest discover -s tests -p "*.py" -v  
```
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
