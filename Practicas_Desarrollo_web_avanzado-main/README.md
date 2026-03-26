# Practica: Permisos y Roles en Django

Proyecto realizado para la practica de permisos en Django, basado en el flujo de `django_permissions`.

## Objetivo

Implementar control de acceso por permisos y roles usando:

- Permisos automaticos de Django (`add`, `view`, `change`, `delete`)
- Permisos personalizados en el modelo `Article`
- Grupos/roles: `Lector`, `Escritor`, `Editor`
- Vistas protegidas con `@login_required` y `@permission_required`
- Pagina `403` personalizada

## Requisitos

- Python 3.14+
- `uv` instalado

## Instalacion y ejecucion

1. Clonar el repositorio

```bash
git clone https://github.com/Marghook/Practicas_Desarrollo_web_avanzado.git
cd Practicas_Desarrollo_web_avanzado
```

2. Crear/activar entorno virtual y sincronizar dependencias

```powershell
uv venv
. .\.venv\Scripts\Activate.ps1
uv sync
```

3. Aplicar migraciones

```bash
python manage.py migrate
```

4. Crear grupos y permisos

```bash
python manage.py setup_groups
```

5. Ejecutar servidor

```bash
python manage.py runserver
```

## Rutas principales

- Admin: `http://127.0.0.1:8000/admin/`
- Login: `http://127.0.0.1:8000/`
- Blog (articulos): `http://127.0.0.1:8000/blog/articles/`

## Roles y permisos esperados

- `Lector`: puede ver articulos
- `Escritor`: puede ver, crear y editar
- `Editor`: puede ver, crear, editar, eliminar y publicar

## Archivos clave de la practica

- `blog/models.py`
- `blog/views.py`
- `blog/forms.py`
- `blog/urls.py`
- `blog/management/commands/setup_groups.py`
- `blog/templates/blog/article_list.html`
- `blog/templates/blog/article_form.html`
- `blog/templates/blog/article_confirm_delete.html`
- `templates/403.html`

## Usuarios de prueba (ejemplo)

Se pueden crear desde `python manage.py shell`:

- `lector1 / pass1234`
- `escritor1 / pass1234`
- `editor1 / pass1234`

## Nota

Este proyecto usa SQLite (`db.sqlite3`) para desarrollo local.
