


# Parcial 2 - Tópicos de Ingeniería de Software

Este proyecto es una aplicación web desarrollada en **Python** usando **Flask**, que permite calcular el **factorial de un número** ingresado por URL, y mostrar el resultado con un diseño visual agradable.

---

## Estructura del proyecto

```
Parcial2_Topicos_Ingenieri_Software/
└───parcial2_app/
    │   app.py
    └───templates/
        └───factorial.html
```

---

## Instrucciones para ejecutar el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/Sebastian-jimenez30/Parcial2_Topicos_Ingenieri_Software.git
cd Parcial2_Topicos_Ingenieri_Software
```

---

### 2. Crear y activar un entorno virtual

```bash
python3 -m venv parcial2
source parcial2/bin/activate          # En Linux/macOS
# parcial2\Scripts\activate           # En Windows
```

---

### 3. Instalar dependencias

```bash
pip install flask
```

---

### 4. Ejecutar la aplicación

```bash
cd parcial2_app
python app.py
```

La aplicación se ejecutará por defecto en: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## ¿Cómo usar?

Ingresá en el navegador una URL como:

```
http://127.0.0.1:5000/factorial/6
```

Y verás el resultado del factorial de `6` renderizado con una interfaz HTML.

---

## Requisitos

- Python 3.7+
- Flask

---

## Autor

Anderson Sebastián Jiménez Mercado  
Proyecto para el parcial 2 de Tópicos de Ingeniería de Software.
