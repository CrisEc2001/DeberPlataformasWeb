from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, HistoriaClinica

Session = sessionmaker(bind=engine)
session = Session()


historias = session.query(HistoriaClinica).order_by(
    HistoriaClinica.fecha_atencion.desc()
).all()

print("Historias clínicas ordenadas por fecha:")
for h in historias:
    vet = h.veterinario
    print(f"- {h.fecha_atencion} | Mascota: {h.nombre_mascota} | {h.diagnostico} (Dr/a. {vet.nombres} {vet.apellidos})")

session.close()
