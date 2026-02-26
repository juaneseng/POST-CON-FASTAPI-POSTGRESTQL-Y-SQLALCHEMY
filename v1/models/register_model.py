from datetime import datetime

from v1.db.base import Base
from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column

"""

En este archivo, usualmente definimos los modelos con el ORM (Object-Relational Mapping) de preferencia, cuya funcion es mostrarle a la base de datos, que tipo de datos va esperar.

"""


class mUser(Base):
    """
    Esta clase representa la tabla 'user' en la base de datos.
    Almacena informaciÃ³n bÃ¡sica de los usuarios del sistema.

    Hereda de Base, que es la clase declarativa de SQLAlchemy
    que convierte esta clase Python en una tabla de base de datos.
    """

    __tablename__ = "login_user"
    # Aca hacemos el mapeo de datos, para explicarle a la base de datos, que tipo de datos va, enn la nueva version de sqlalchemy, se utiliza este tipo de mapeado, que mejora la eficiencia al leer codigo, por que me lee con dattos de python
    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(100), nullable=False)

    last_name: Mapped[str] = mapped_column(String(100), nullable=False)

    email: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)

    password: Mapped[str] = mapped_column(String(255), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

