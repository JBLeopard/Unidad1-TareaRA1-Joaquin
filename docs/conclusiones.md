# 5. Reflexión sobre la infraestructura de seguridad de los lenguajes

Durante el desarrollo de esta tarea se han aplicado y analizado distintas medidas de seguridad relacionadas con el lenguaje Python y el entorno de ejecución.  

---

## Seguridad en Python

Python es un lenguaje que prioriza la facilidad de uso y la legibilidad, pero no incorpora de forma nativa mecanismos estrictos de aislamiento o control de recursos. Por este motivo, herramientas externas como Firejail o contenedores Docker resultan fundamentales para ejecutar aplicaciones Python de forma segura en entornos productivos.  

---

## Comparación con otros lenguajes

Otros lenguajes, como Java o C#, incorporan máquinas virtuales con mecanismos de seguridad más avanzados, como control de memoria, gestión de permisos o sandboxing interno. Sin embargo, incluso en estos casos, el uso de entornos controlados sigue siendo una buena práctica.

Esta tarea pone de manifiesto la importancia de combinar:
- Buenas prácticas de programación
- Pruebas automatizadas
- Ejecución en entornos aislados

Todo ello contribuye a una **puesta en producción más segura**, alineada con los principios de DevSecOps.
