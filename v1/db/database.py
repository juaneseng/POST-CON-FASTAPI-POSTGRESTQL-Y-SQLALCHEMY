from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from v1.core.config import settings

"""
Esta carpeta es super importanbte... aca es donde se crea el motor, y los administradores de sesion para conectar nuestra api con la base de datos

Primero, se crea la URL de conexiÃ³n a la base de datos utilizando los parÃ¡metros definidos en el archivo de configuraciÃ³n.
	postgresql://user:password@localhost/dbname
En este caso, como estoy usando posgrest es este nombre, y el driver es psycopg2, que es el recomendado para postgresql.
para otros motores de sql seria diferetne. 
"""
SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{settings.db_user}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}"
"""
Luego se crea el motor de SQLAlchemy utilizando la URL de conexiÃ³n. El motor es responsable de gestionar las conexiones a la base de datos y ejecutar las consultas.
Si no esta el create engine, no se puede conectar a la base de datos, y no se pueden ejecutar las consultas.
"""

engine = create_engine(SQLALCHEMY_DATABASE_URL)

"""
 SessionLocal es un generador de sesiones de base de datos.
 Se utiliza para crear nuevas sesiones independientes por cada request.
 Esto permite manejar transacciones de forma segura y evitar conflictos entre usuarios concurrentes.
"""
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
"""
Autocommit, sirve par que los cambios no se guarden automaticamente, y necesiten se confirmados manualmente, esto es importante para evitar errores, y para tener un control mas preciso sobre las transacciones.

Autoflush, sirve para evitar que se envien cambios a la base de datos antes de tiempo, esto es importante para evitar errores, y para tener un control mas preciso sobre las transacciones. Evita que SQLAlchemy haga consultas sin que te des cuenta.

Bind, sirve para conectar el motor a la sesiÃ³n, esto es importante para que la sesiÃ³n pueda ejecutar consultas en la base de datos.
"""


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


"""
GET_DB ES LA FUNCION que pondremos en endpoints, para obtener una sesiÃ³n de base de datos, y poder ejecutar consultas en la base de datos.

Aca, ya creamos la sesion, para ser usada en los endpints, y luego la cerramos, para evitar problemas de conexiones abiertas, y para liberar recursos.

"""

