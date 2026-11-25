from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, Clinica

Session = sessionmaker(bind=engine)
session = Session()


clinicas = session.query(Clinica).all()

for c in clinicas:
    total_historias = 0
    for cons in c.consultorios:
        for vet in cons.veterinarios:
            total_historias += len(vet.historias_clinicas)

    print(f"Clínica: {c.nombre_comercial}")
    print(f"  Dirección: {c.direccion}")
    print(f"  Responsable: {c.veterinario_responsable}")
    print(f"  Número de historias clínicas asociadas: {total_historias}")
    print("-" * 45)

session.close()
