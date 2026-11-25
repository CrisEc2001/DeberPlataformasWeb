from datetime import date
from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, Clinica, Consultorio, Veterinario, HistoriaClinica

Session = sessionmaker(bind=engine)
session = Session()

# Clinicas 
c1 = Clinica(
    nombre_comercial="VetVida Norte",
    direccion="Av. 6 de Diciembre y Eloy Alfaro, Quito",
    veterinario_responsable="Dr. Carlos Mendoza"
)
c2 = Clinica(
    nombre_comercial="Clínica Animal del Puerto",
    direccion="Av. Francisco de Orellana Km 4, Guayaquil",
    veterinario_responsable="Dra. Valeria Ortiz"
)
c3 = Clinica(
    nombre_comercial="San Roque Veterinaria",
    direccion="Av. Remigio Crespo 4-25, Cuenca",
    veterinario_responsable="Dr. Diego Salazar"
)

session.add_all([c1, c2, c3])

# Consultorios 
cons1 = Consultorio(nombre_numero="Consultorio 101", especialidad="Medicina General", clinica=c1)
cons2 = Consultorio(nombre_numero="Consultorio 102", especialidad="Cirugía", clinica=c1)
cons3 = Consultorio(nombre_numero="Consultorio A1", especialidad="Dermatología", clinica=c2)
cons4 = Consultorio(nombre_numero="Consultorio A2", especialidad="Medicina General", clinica=c2)
cons5 = Consultorio(nombre_numero="Consultorio 1", especialidad="Cirugía", clinica=c3)
cons6 = Consultorio(nombre_numero="Consultorio 2", especialidad="Cardiología", clinica=c3)

session.add_all([cons1, cons2, cons3, cons4, cons5, cons6])

# Veterinarios 
v1 = Veterinario(
    nombres="Carlos",
    apellidos="Mendoza",
    correo="cmendoza@vetvida.ec",
    numero_licencia="VET-EC-1042",
    consultorio=cons1
)
v2 = Veterinario(
    nombres="Andrea",
    apellidos="Paredes",
    correo="aparedes@vetvida.ec",
    numero_licencia="VET-EC-1185",
    consultorio=cons1
)
v3 = Veterinario(
    nombres="Luis",
    apellidos="Cevallos",
    correo="lcevallos@vetvida.ec",
    numero_licencia="VET-EC-1290",
    consultorio=cons2
)
v4 = Veterinario(
    nombres="Valeria",
    apellidos="Ortiz",
    correo="vortiz@animalpuerto.ec",
    numero_licencia="VET-EC-2031",
    consultorio=cons3
)
v5 = Veterinario(
    nombres="Mateo",
    apellidos="Jaramillo",
    correo="mjaramillo@animalpuerto.ec",
    numero_licencia="VET-EC-2144",
    consultorio=cons4
)
v6 = Veterinario(
    nombres="Diego",
    apellidos="Salazar",
    correo="dsalazar@sanroquevet.ec",
    numero_licencia="VET-EC-3018",
    consultorio=cons5
)
v7 = Veterinario(
    nombres="Gabriela",
    apellidos="Lozano",
    correo="glozano@sanroquevet.ec",
    numero_licencia="VET-EC-3192",
    consultorio=cons6
)

session.add_all([v1, v2, v3, v4, v5, v6, v7])

# Historias clinicas 
historias = [
    HistoriaClinica(
        fecha_atencion=date(2026, 10, 14),
        diagnostico="Gastroenteritis leve",
        tratamiento="Dieta blanda por 5 días y probióticos cada 12 horas",
        nombre_mascota="Max",
        veterinario=v1
    ),
    HistoriaClinica(
        fecha_atencion=date(2026, 10, 22),
        diagnostico="Control de vacunación anual",
        tratamiento="Aplicación de vacuna séxtuple y desparasitación oral",
        nombre_mascota="Luna",
        veterinario=v1
    ),
    HistoriaClinica(
        fecha_atencion=date(2026, 11, 2),
        diagnostico="Otitis externa bacteriana",
        tratamiento="Limpieza ótica diaria y gotas antibióticas por 7 días",
        nombre_mascota="Toby",
        veterinario=v2
    ),
    HistoriaClinica(
        fecha_atencion=date(2026, 11, 5),
        diagnostico="Fractura cerrada de radio",
        tratamiento="Reducción quirúrgica con placa y reposo por 4 semanas",
        nombre_mascota="Rocky",
        veterinario=v3
    ),
    HistoriaClinica(
        fecha_atencion=date(2026, 11, 11),
        diagnostico="Esterilización programada",
        tratamiento="Ovariohisterectomía, collar isabelino y analgésicos por 4 días",
        nombre_mascota="Kira",
        veterinario=v3
    ),
    HistoriaClinica(
        fecha_atencion=date(2026, 11, 3),
        diagnostico="Dermatitis alérgica por pulgas",
        tratamiento="Antiparasitario mensual y baño medicado con clorhexidina",
        nombre_mascota="Milo",
        veterinario=v4
    ),
    HistoriaClinica(
        fecha_atencion=date(2026, 11, 9),
        diagnostico="Pioderma superficial",
        tratamiento="Cefalexina cada 12 horas por 14 días",
        nombre_mascota="Nala",
        veterinario=v4
    ),
    HistoriaClinica(
        fecha_atencion=date(2026, 11, 14),
        diagnostico="Rinotraqueitis felina",
        tratamiento="Nebulizaciones y suplemento de L-lisina por 10 días",
        nombre_mascota="Michi",
        veterinario=v5
    ),
    HistoriaClinica(
        fecha_atencion=date(2026, 11, 18),
        diagnostico="Deshidratación moderada",
        tratamiento="Fluidoterapia subcutánea y observación 24 horas",
        nombre_mascota="Bruno",
        veterinario=v5
    ),
    HistoriaClinica(
        fecha_atencion=date(2026, 11, 7),
        diagnostico="Extracción de cuerpo extraño gástrico",
        tratamiento="Gastrotomía, antibiótico parenteral y dieta líquida",
        nombre_mascota="Simba",
        veterinario=v6
    ),
    HistoriaClinica(
        fecha_atencion=date(2026, 11, 16),
        diagnostico="Soplo cardíaco grado II",
        tratamiento="Ecocardiograma de control y seguimiento cada 6 meses",
        nombre_mascota="Coco",
        veterinario=v7
    ),
]

session.add_all(historias)
session.commit()
session.close()

print("Datos ingresados correctamente.")
