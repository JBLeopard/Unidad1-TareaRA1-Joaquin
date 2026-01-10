# 2. Ejecución y depuración del programa

En este apartado se describe el proceso de ejecución y depuración de la aplicación utilizando el IDE **Visual Studio Code**, así como los errores detectados durante la ejecución inicial.

---

## 2.1 Ejecución del programa

Durante la primera ejecución, el programa no funcionó correctamente debido a varios errores de implementación.

**Error mostrado en Visual Studio Code**  

![Error en ejecución](./imagenes/errormainapp.png)

---

## 2.2 Errores detectados en la ejecución

### Error 1: Llamada incorrecta a métodos

**Causa:**  
En el archivo `main_app.py` se realizaban llamadas a métodos inexistentes o con nombres incorrectos (por ejemplo `_hacer_lavado` en lugar de `hacerLavado`).

**Consecuencia:**  
El programa lanzaba excepciones al iniciar la ejecución.

**Solución aplicada:**  
He unificado los nombres de los métodos en toda la aplicación, utilizando exclusivamente el método público `hacerLavado()`.

---

### Error 2: Firma incorrecta de funciones

**Causa:**  
La función `ejecutarSimulacion()` no recibía correctamente todos los argumentos necesarios.

**Solución aplicada:**  
He modificado la función para aceptar explícitamente:
- La instancia del lavadero
- Las opciones de prelavado, secado y encerado

**Error corregido tras la modificación**  

![Error solucionado](./imagenes/errormainappsol.png)

---
A pesar de todas las demás pruebas realizadas con marcadores, no he encontrado mas fallos en el código.

---
