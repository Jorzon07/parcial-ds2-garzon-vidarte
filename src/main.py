import os
from pathlib import Path

from pymongo import MongoClient

from modelo import MesaDeAyuda, MINUTOS_POR_HORA

LAMBDA_ALTA_DEMANDA = 9.5
RUTA_GRAFICA = Path(__file__).resolve().parents[1] / "graficas" / "resultado.png"


def leer_tickets(db):
    return list(db["ticket"].find({}, {"_id": 0}))


def leer_mu(db):
    agente_senior = db["agente"].find_one({"nivel": "Senior"})
    return agente_senior["ticket_por_hora"]


def main():
    cliente = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017"))
    db = cliente[os.getenv("MONGO_DB", "MatriculApp")]

    mesa = MesaDeAyuda(leer_tickets(db), leer_mu(db))

    lam = mesa.tasa_llegadas()
    metricas = mesa.metricas_mm1(lam)
    esperas_minutos = mesa.simular()
    espera_simulada = sum(esperas_minutos) / len(esperas_minutos)
    metricas_alta_demanda = mesa.metricas_mm1(LAMBDA_ALTA_DEMANDA)

    print(f"λ = {lam:.2f} tickets/hora | μ = {mesa.mu} tickets/hora")
    print(f"ρ = {metricas['rho']:.3f} | Lq = {metricas['Lq']:.2f} tickets")
    print(f"Wq teórico  = {metricas['Wq']:.3f} h ({metricas['Wq'] * MINUTOS_POR_HORA:.1f} min)")
    print(f"Wq simulado = {espera_simulada:.2f} min | esperas: {esperas_minutos}")
    print(f"Wq con λ = {LAMBDA_ALTA_DEMANDA}: {metricas_alta_demanda['Wq']:.2f} h "
          f"({metricas_alta_demanda['Wq'] * MINUTOS_POR_HORA:.0f} min)")

    mesa.graficar(RUTA_GRAFICA)
    print(f"Gráfica guardada en {RUTA_GRAFICA}")


if __name__ == "__main__":
    main()
