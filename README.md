<div align="center">

# 📚 Librería Papelucho


![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.0-092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Status](https://img.shields.io/badge/Status-En%20Desarrollo-orange?style=for-the-badge)

Proyecto desarrollado con **Django** y **PostgreSQL** que modela una pequeña biblioteca dedicada a los libros de *Papelucho*, el icónico personaje de la literatura infantil chilena creado por Marcela Paz.


> Desarrollado en el marco de la **Actividad Práctica N°4 – Módulo 7 (Gestión de Migraciones en Django)**.

</div>



---

## 📖 Descripción

**Librería Papelucho** es una aplicación backend que permite gestionar información bibliográfica utilizando el **ORM de Django** y el sistema de migraciones para el control del esquema de base de datos.

El sistema actualmente permite:

* Registrar libros
* Gestionar información básica (título, autor, ISBN)
* Aplicar y versionar cambios en la base de datos mediante migraciones
* Ejecutar operaciones CRUD utilizando Django ORM

El desarrollo completo de la actividad práctica, incluyendo explicación teórica, comandos ejecutados y evidencias gráficas, se encuentra documentado en el archivo:

```
migraciones.md
```

---

## 🛠 Tecnologías utilizadas

* Python 3
* Django
* PostgreSQL
* Django ORM
* Git & GitHub

---

## 🚀 Cómo ejecutar el proyecto

1. Clonar el repositorio
2. Crear y activar entorno virtual
3. Instalar dependencias

```bash
pip install -r requirements.txt
```

4. Ejecutar migraciones

```bash
python manage.py migrate
```

5. Iniciar el servidor

```bash
python manage.py runserver
```

---

## 🔮 Proyección futura

Aunque actualmente cumple con los objetivos académicos de la actividad, el proyecto tiene potencial para evolucionar hacia:

* Implementación de autenticación y control de usuarios
* Interfaz frontend completa
* Sistema de préstamos
* Panel administrativo personalizado
* API REST

---

## 🎯 Objetivo Académico

Demostrar la correcta implementación del sistema de migraciones de Django y la sincronización entre modelos y base de datos.

---

Proyecto académico desarrollado con fines educativos y con potencial de crecimiento hacia una aplicación completa de gestión bibliográfica.



