# 🎨 GitHub Contribution Graph Pain

¡Convierte tu gráfica de contribuciones de GitHub en un lienzo de pixel art!

Este proyecto contiene un script en Python que automatiza la creación de commits en fechas específicas del pasado. Al leer un archivo de diseño (`pattern.json`), el script "viaja en el tiempo" y genera la actividad necesaria para dibujar patrones, texto o logos en tu perfil de GitHub.

> **⚠️ Aviso:** Este proyecto es con fines educativos y de diversión. Se recomienda usarlo en un repositorio nuevo y vacío, no en proyectos profesionales activos.

## 🚀 Características

* **Dibujo Personalizado:** Carga cualquier diseño desde un archivo JSON.
* **Intensidad de Color:** Genera automáticamente 5 commits por "pixel" para asegurar que el punto verde se vea intenso.
* **Viaje en el Tiempo:** Modifica las variables de entorno `GIT_AUTHOR_DATE` y `GIT_COMMITTER_DATE` para colocar commits en el pasado.
* **Animaciones CLI:** Incluye una interfaz de línea de comandos con barras de carga y banners ASCII.
* **Automatización Total:** Solo necesitas ejecutar el script, ingresar el año y el código se encarga de hacer los commits y el push.

## 🛠️ Requisitos Previos

Asegúrate de tener instalado lo siguiente en tu sistema:

* [Python 3.x](https://www.python.org/downloads/)
* [Git](https://www.google.com/search?q=https://git-scm.com/downloads)
* Una cuenta de GitHub y acceso configurado (SSH o Token) para hacer push sin contraseña cada vez.

## 📦 Instalación y Uso

### 1. Clona este repositorio

```bash
git clone https://github.com/tu-usuario/nombre-del-repo.git
cd nombre-del-repo

```

### 2. Prepara tu patrón (`pattern.json`)

El archivo `pattern.json` define tu dibujo. Es una matriz de **7 filas** (los días de la semana, de Domingo a Sábado) y aproximadamente **52 columnas** (las semanas del año).

* Espacio `" "` = Día vacío (sin contribución).
* Cualquier otro carácter (ej. `"3"`) = Día con contribución (Pixel activo).

Ejemplo de estructura:

```json
[
  "       ",
  "  XXX  ",
  " X   X ",
  " X   X ",
  " X   X ",
  "  XXX  ",
  "       "
]

```

### 3. Ejecuta el script

Corre el script principal con Python:

```bash
python script.py

```

### 4. Sigue las instrucciones

El script mostrará una animación de carga y te pedirá que ingreses el año donde quieres dibujar el patrón:

```text
👉 Enter year to draw pattern 📆 ➤ 2023

```

El script calculará las fechas exactas basándose en el primer domingo del año elegido, generará los commits en el archivo `info.txt` y hará el `git push` automáticamente al finalizar.

## 🧠 ¿Cómo funciona?

El script `script.py` realiza los siguientes pasos:

1. **Carga el Patrón:** Lee la matriz desde `pattern.json`.
2. **Calcula Fechas:** Localiza el primer domingo del año ingresado para alinear la gráfica correctamente.
3. **Itera:** Recorre cada celda de la matriz.
4. **Genera Commits:** Si encuentra un carácter, calcula la fecha correspondiente y genera 5 commits vacíos modificando la fecha de autoría de Git.
5. **Sincroniza:** Al terminar, ejecuta `git push` para enviar los cambios a GitHub.

