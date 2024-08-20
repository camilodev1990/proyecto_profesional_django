# Proyecto Profesional Django

Plantilla de proyecto lista para trabajar, organizada de manera profesional.

## Estructura del Proyecto

```plaintext

proyecto_profesional_django/
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
        
