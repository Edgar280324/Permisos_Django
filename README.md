# Práctica: Permisos y Roles en Django

Proyecto realizado para la práctica de permisos en Django, basado en el flujo de django_permissions.
# Objetivo

Implementar control de acceso por permisos y roles usando:

- Permisos automáticos de Django (add, view, change, delete)
- Permisos personalizados en el modelo Article
- Grupos/roles: Lector, Escritor, Editor
- Vistas protegidas con @login_required y @permission_required
- Página 403 personalizada

# Requisitos

- Python 3.14+
- uv instalado

# Instalación y ejecución

## Clonar el repositorio

bash
git clone https://github.com/Edgar280324/Permisos_Django.git
cd Practicas_Desarrollo_web_avanzado

# Crear y activar entorno virtual
uv venv
. .\.venv\Scripts\Activate.ps1
uv sync

# Aplicar migraciones
python manage.py migrate

# Crear grupos y permisos
python manage.py setup_groups

# Ejecutar Servidor
python manage.py runserver
# Rutas principales
- Admin: http://127.0.0.1:8000/admin/
- Login: http://127.0.0.1:8000/
- Blog (artículos): http://127.0.0.1:8000/blog/articles/

# Roles y permisos
- Lector: puede ver artículos
- Escritor: puede ver, crear y editar
- Editor: puede ver, crear, editar, eliminar y publicar

# Usuarios de prueba se puede crear desde:
python manage.py shell

# Credenciales:
- lector1 / pass1234
- escritor1 / pass1234
- editor1 / pass1234




