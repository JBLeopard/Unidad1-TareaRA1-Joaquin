# 1. Creación del repositorio

Este documento describe el proceso realizado para la creación y configuración inicial del repositorio **PPS-Unidad0-Tarea-Joaquin**.

---

## Objetivo
Crear un repositorio público en GitHub con la estructura mínima necesaria para alojar la documentación de la actividad y preparar la automatización con GitHub Actions y la publicación en GitHub Pages.

---

## 1.1 Creación del repositorio en `GitHub`

Pasos realizados:  
	1. Acceder a [GitHub](https://github.com/) con la cuenta correspondiente.  
	2. Pulsar **New repository**.  
	3. Configurar:  
   - **Repository name:** `PPS-Unidad0-Tarea-Joaquin`  
   - **Visibility:** `Public`  
   - **Initialize with README:** `Si`  

![](./imagenes/repo.jpg)

---

## 1.2 Instalación `Git` en `Kali Linux`

- Instalamos Git.  
```bash
sudo apt install git
```
- Configuramos nombre y mail de GitHub, rama por defecto y editor.  
```bash
git config --global user.name JBLeopard
git config --global user.email xxxxxxxxxx@gmail.com
git config --global init.defaultBranch main
git config --global core.editor nano
```
- Para mostrar mensajes sin editor `git diff` o `git log`.  
```bash
git config --global core.pager ""
```
- Ajustamos las variables de Git.  
```bash
git config --global color.status auto
git config --global color.branch auto
git config --global color.interactive auto
git config --global color.diff auto
```
- Creamos una clave ssh en nuestro equipo y la añadimos a nuestra cuenta de github para el sincronismo con github.com.  
```bash
ssh-keygen -t ed25519 -C xxxxxxxxxx@gmail.com
# Iniciamos el agente en segundo plano
eval "$(ssh-agent -s)"
#Nos mostrará un mensaje como 
#Agent pid 59566
ssh-add ~/.ssh/id_ed25519
```
- Luego añadimos la clave generado por el siguiente comando a nuestra cuenta de github.com en apartado **Settings/SSH and GPG keys** y **Nueva clave SSH**.
```bash
cat ~/.ssh/id_ed25519.pub
```
![](./imagenes/ssh.jpg)

- Clonación del repositorio.  
```bash
git clone git@github.com:JBLeopard/PPS-Unidad0-Tarea-Joaquin.git
```
- Una vez clonado el repositorio a Kali en local, comenzamos la creación de ficheros y estructura del ejercicio que tendrá una estructura final como esta:  

```
PPS-Unidad0-Tarea-Joaquin/
├── docker-compose.yaml
├── docs
│   ├── conclusiones.md
│   ├── docker.md
│   ├── gitActions.md
│   ├── git.md
│   ├── gitPages.md
│   ├── imagenes
│   │   ├── contenedor.jpg
│   │   ├── gitpages.jpg
│   │   ├── logo.png
│   │   ├── repo.jpg
│   │   ├── seg.jpg
│   │   ├── ssh.jpg
│   │   ├── web.jpg
│   │   ├── wf.jpg
│   │   └── wflogs.jpg
│   ├── index.md
│   └── inspect_salida.json
├── .github
│   └── workflows
│       └── CreacionDocumentacion.yml
├── mkdocs.yml
└── README.md
```
- Comandos usados en Git.  

| Acción             | Comando                   |
| ------------------ | ------------------------- |
| Clonar repositorio | `git clone URL`           |
| Añadir cambios     | `git add .`               |
| Crear commit       | `git commit -m "mensaje"` |
| Subir cambios      | `git push origin main`    |

---
