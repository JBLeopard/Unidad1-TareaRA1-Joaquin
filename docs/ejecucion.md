# 2. Ejecuta el programa mediante las opciones de Ejecución y Depuración del IDE.
🔴 ERROR REAL 1 (IMPORTANTE)
Falta un argumento al llamar a la función
📍 Dónde ocurre

Archivo: main_app.py
Última llamada a ejecutarSimulacion

ejecutarSimulacion(lavadero_global, prelavado=True, secado_mano=False)

🔴 Qué muestra Visual Studio Code al ejecutar / depurar

En la consola aparece algo como:

TypeError: ejecutarSimulacion() missing 1 required positional argument: 'encerado'


VS Code:

Detiene la ejecución

Marca la línea en rojo

Indica el archivo y la línea exacta

🧠 Causa del error

La función está definida así:

def ejecutarSimulacion(lavadero, prelavado, secado_mano, encerado):


Pero se está llamando solo con 3 argumentos, cuando necesita 4.

✅ Solución aplicada

Añadir el argumento que falta:

ejecutarSimulacion(
    lavadero_global,
    prelavado=True,
    secado_mano=False,
    encerado=False
)


👉 Este error SÍ es obligatorio documentarlo en el Apartado 2.

Apartado 2 – Ejecución y depuración en Visual Studio Code

Al ejecutar la aplicación desde Visual Studio Code, el IDE mostró un error de ejecución de tipo TypeError, indicando que a la función ejecutarSimulacion le faltaba un argumento obligatorio (encerado). El error se mostraba en la consola, señalando el archivo main_app.py y la línea exacta donde se producía el fallo, deteniendo la ejecución del programa.

La causa del error era una llamada incorrecta a la función, ya que estaba definida con cuatro parámetros, pero se estaba invocando únicamente con tres. Para solucionarlo, se añadió el parámetro que faltaba en la llamada a la función.

Además, Visual Studio Code mostraba varios avisos generados por la extensión SonarLint relacionados con convenciones de nombres, complejidad del código y buenas prácticas. Estos avisos no impedían la ejecución del programa y no se consideraron errores de ejecución, por lo que no fue necesario corregirlos en este apartado.

Tras corregir el error de ejecución, el programa pudo ejecutarse y depurarse correctamente desde el IDE.
