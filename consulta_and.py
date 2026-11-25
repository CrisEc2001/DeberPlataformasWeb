from datetime import date
from sqlalchemy import and_
from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, HistoriaClinica

Session = sessionmaker(bind=engine)
session = Session()


historias = session.query(HistoriaClinica).filter(
    and_(
        HistoriaClinica.fecha_atencion >= date(2026, 11, 1),
        HistoriaClinica.fecha_atencion <= date(2026, 11, 15)
    )
).all()

print("Historias clínicas entre el 1 y el 15 de noviembre de 2026:")
for h in historias:
    print(f"- {h.fecha_atencion} | {h.nombre_mascota}: {h.diagnostico}")

session.close()
