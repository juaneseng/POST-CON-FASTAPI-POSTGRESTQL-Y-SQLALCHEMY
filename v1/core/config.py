from pydantic_settings import BaseSettings, SettingsConfigDict

"""
Aca definimos la clase Settings, que es la encargada de leer las variables de entorno, y almacenarlas en atributos de la clase. Esto es importante para tener una configuracion centralizada, y para evitar hardcodear las variables de entorno en el codigo.
"""


class Settings(BaseSettings):
    db_port: int
    db_host: str
    db_user: str
    db_password: str
    db_name: str

    model_config = SettingsConfigDict(
        from_attributes=True, env_file=".env", case_sensitive=False
    )


"""Con model_config le decimos a pydantic, que lea las variables de entorno, y las almacene en los atributos de la clase, ademas de decirle que no sea sensible a mayusculas y minusculas, para evitar problemas al escribir las variables de entorno."""


settings = Settings()

"""
Identamos settings para despues instanciarla en los demas archivos. esto se hace para no filtrar datos sensibles, Ya que los datos los tendremos en un archivo .env, que no se subira ni se compartira
"""

