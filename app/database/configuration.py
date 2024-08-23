from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine

# Conexion a la base de datos
# nombre de la base de datos

dataBaseName= "gestionbd"

#usuario de la base de datos
userName= "root"

#contraseña de la base de datos

userPassword= ""

#puerto de conexion a la base de datos
conexionPort = "3306"

#servidor conexion a la base
servidorPort = "localhost"

#creanddo la conexion
connectionToDataBase=f"mysql+mysqlconnector://{userName}:{userPassword}@{servidorPort}:{conexionPort}/{dataBaseName}"

engine = create_engine(connectionToDataBase)
sessionLocal=sessionmaker(autocomit=False, autoflush=False, bind=engine)