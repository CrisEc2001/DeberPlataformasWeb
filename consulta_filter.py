from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, Consultorio

Session = sessionmaker(bind=engine)
session = Session()


consultorios = session.query(Consultorio).filter(
    Consultorio.especialidad == "Cirugía"
).all()

print("Consultorios de Cirugía:")
for cons in consultorios:
    print(f"- {cons.nombre_numero} | Clínica: {cons.clinica.nombre_comercial}")

session.close()
