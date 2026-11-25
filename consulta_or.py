from sqlalchemy import or_
from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, Consultorio

Session = sessionmaker(bind=engine)
session = Session()


consultorios = session.query(Consultorio).filter(
    or_(
        Consultorio.especialidad == "Dermatología",
        Consultorio.especialidad == "Cardiología"
    )
).all()

print("Consultorios de Dermatología o Cardiología:")
for cons in consultorios:
    print(f"- {cons.nombre_numero} ({cons.especialidad}) - {cons.clinica.nombre_comercial}")

session.close()
