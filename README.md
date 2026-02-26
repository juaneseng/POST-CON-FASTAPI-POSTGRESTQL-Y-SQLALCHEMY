# POST con FastAPI + PostgreSQL + SQLAlchemy

Este repositorio representa mi primer proyecto conectando una API con una base de datos relacional.

La idea de este proyecto es explicar, con mis propias palabras, los conceptos más básicos para conectar una API con una base de datos y entender cómo funciona el flujo completo.

Aquí documento lo que voy aprendiendo mientras construyo backend paso a paso.

---

## 📦 Esquemas (Pydantic)

En esta parte definimos los datos que esperamos recibir desde el usuario.

Básicamente, aquí ponemos la estructura de los datos que van a llegar en las rutas, y luego los usamos en los endpoints.

Ejemplo:

* email
* password

Esto nos ayuda a validar lo que envía el cliente.

---

## 🧱 Modelos (SQLAlchemy ORM)

En esta carpeta definimos los modelos usando ORM (Object Relational Mapping).

La función del ORM es decirle a la base de datos qué tipo de datos va a recibir, pero usando clases de Python.

Por ejemplo:

* Creamos una clase que representa la tabla
* Definimos columnas como id, email, password, etc.

Cada modelo hereda de `Base`, que es la clase declarativa de SQLAlchemy.
Esta clase convierte una clase normal de Python en una tabla de base de datos.

También usamos el nuevo mapeo de SQLAlchemy (Mapped y mapped_column), que permite que el código sea más claro y cercano a Python.

---

## 🧩 Base declarativa

Aquí usamos:

```python
class Base(DeclarativeBase):
    pass
```

Esta base sirve para declarar que una clase será una tabla.
Es parte del nuevo estilo de SQLAlchemy ORM.

---

## ⚙️ Configuración

Aquí definimos una clase `Settings` que se encarga de leer las variables de entorno.

La idea es evitar poner datos sensibles directamente en el código.
Por ejemplo:

* usuario de base de datos
* contraseña
* host
* puerto

Todo eso se guarda en un archivo `.env`.

Luego usamos Pydantic Settings para cargar esas variables en una clase y poder usarlas en todo el proyecto.

Esto permite tener una configuración centralizada y más segura.

---

## 🔌 Conexión a la base de datos

Esta parte es muy importante, porque aquí se crea todo lo necesario para conectar la API con la base de datos.

Primero se crea la URL de conexión usando los datos del archivo de configuración:

```
postgresql://user:password@localhost/dbname
```

En mi caso uso PostgreSQL con el driver psycopg2.

Luego creamos el engine de SQLAlchemy:

```python
engine = create_engine(SQLALCHEMY_DATABASE_URL)
```

El engine es el encargado de manejar las conexiones y ejecutar consultas.
Sin el engine no hay conexión con la base de datos.

---

## 🧠 SessionLocal

SessionLocal es un generador de sesiones de base de datos.

Se usa para crear sesiones independientes por cada request.
Esto permite manejar transacciones de forma segura y evitar conflictos entre usuarios concurrentes.

```python
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
```

### autocommit=False

Hace que los cambios no se guarden automáticamente.
Así podemos confirmar manualmente las transacciones con commit.

### autoflush=False

Evita que SQLAlchemy envíe cambios a la base de datos antes de tiempo.
Esto ayuda a evitar errores y comportamientos inesperados.

### bind=engine

Conecta la sesión con el motor de base de datos.
Permite que la sesión pueda ejecutar consultas.

---

## 🔁 get_db()

Esta función se usa en los endpoints para obtener una sesión de base de datos.

Lo que hace es:

* Crear la sesión
* Usarla en el endpoint
* Cerrarla al final

Esto evita dejar conexiones abiertas y ayuda a liberar recursos.

---

## 🌐 Routers

Aquí creamos los endpoints de FastAPI.

Importamos:

* El modelo
* El esquema
* La función get_db

También usamos `APIRouter` para agrupar rutas relacionadas.

En el endpoint POST:

* Definimos la ruta (por ejemplo `/users/`)
* Indicamos que recibimos un esquema
* Inyectamos la sesión con Depends(get_db)

Dentro del endpoint:

1. Creamos el usuario usando el modelo
2. Lo agregamos a la sesión
3. Hacemos commit
4. Refrescamos el objeto
5. Lo retornamos

---

## 🚀 main.py

Finalmente, en main creamos la aplicación FastAPI.

También ejecutamos:

```python
Base.metadata.create_all(bind=engine)
```

Esto crea las tablas automáticamente usando el motor que ya definimos.

Es importante para que la base de datos tenga las tablas cuando inicia la aplicación.

Luego incluimos los routers y arrancamos la API.

---

## 🎯 Objetivo del proyecto

Este proyecto está enfocado en aprendizaje.

La idea es entender bien:

* Cómo conectar una API con una base de datos
* Cómo funcionan los modelos
* Cómo manejar sesiones
* Cómo hacer un POST real

Más adelante planeo usar esta base para:

* CRUD completo
* Autenticación
* JWT
* Mejor estructura
* Deploy

---

## 👨‍💻 Notas

Este repositorio no busca ser perfecto, sino mostrar mi progreso aprendiendo backend.
La idea es seguir mejorándolo con el tiempo y documentar el proceso.
