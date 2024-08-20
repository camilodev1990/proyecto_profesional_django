# Proyecto Profesional Django

Plantilla de proyecto lista para trabajar, organizada de manera profesional.

## Estructura del Proyecto

```plaintext
proyecto_profesional_django/
<<<<<<< HEAD
|
├── .env
├── .gitignore
├── manage.py
├── README.md
|
├── backend/
|   |
│   ├── asgi.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── __init__.py
|   |
│   └── settings/
|       |
│       ├── base.py
|       |
│       ├── dev.py --> configuracion para entorno desarrollo
|       |
│       ├── local.py --> configuracion para entorno local
|       |
│       ├── prod.py --> configuracion para entorno produccion
|       |
│       └── __init__.py
|
|
└── frontend/
    |
    ├── aplicaciones/ --> aqui van las aplicaciones
    │   
    ├── static/ --> aqui van los estaticos globales
    │   
    └── templates/ --> aqui van los templates globales
        

=======
├── .env
├── .gitignore
├── dev_db.sqlite3
├── manage.py
├── README.md
├── backend/
│   ├── asgi.py
│   ├── dev_db.sqlite3
│   ├── urls.py
│   ├── wsgi.py
│   ├── __init__.py
│   ├── settings/
│   │   ├── base.py
│   │   ├── dev.py
│   │   ├── local.py
│   │   ├── prod.py
│   │   └── __init__.py
│   └── __pycache__/
│       ├── base.cpython-312.pyc
│       ├── dev.cpython-312.pyc
│       ├── local.cpython-312.pyc
│       └── __init__.cpython-312.pyc
└── frontend/
    ├── aplicaciones/
    │   └── aqui_van_las_aplicaciones.txt
    ├── static/
    │   └── aqui_van_los_estaticos.txt
    └── templates/
        └── aqui_van_los_templates.txt

