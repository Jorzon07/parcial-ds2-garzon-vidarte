import numpy as np
import matplotlib
from pathlib import Path

matplotlib.use("Agg")
import matplotlib.pyplot as plt

MINUTOS_POR_HORA = 60


class MesaDeAyuda:
    def __init__(self, tickets, mu):
        self.tickets = sorted(tickets, key=lambda ticket: ticket["minuto_llegada"])
        self.mu = mu

    def tasa_llegadas(self):
        minutos_llegada = [ticket["minuto_llegada"] for ticket in self.tickets]
        minutos_entre_llegadas = np.diff(minutos_llegada).mean()
        return float(MINUTOS_POR_HORA / minutos_entre_llegadas)

    def metricas_mm1(self, lam):
        if lam >= self.mu:
            raise ValueError(f"Sistema inestable: λ={lam} debe ser menor que μ={self.mu}")

        rho = lam / self.mu
        return {
            "rho": rho,
            "Lq": rho**2 / (1 - rho),
            "Wq": rho / (self.mu - lam),
        }

    def simular(self):
        esperas_minutos = []
        fin_atencion_anterior = 0
        for ticket in self.tickets:
            inicio_atencion = max(ticket["minuto_llegada"], fin_atencion_anterior)
            esperas_minutos.append(inicio_atencion - ticket["minuto_llegada"])
            fin_atencion_anterior = inicio_atencion + ticket["minuto_atencion"]
        return esperas_minutos

    def espera_promedio(self):
        return float(np.mean(self.simular()))

    def graficar(self, ruta_salida=None):
        if ruta_salida is None:
            ruta_salida = Path(__file__).resolve().parents[1] / "graficas" / "resultado.png"
        ruta_salida = Path(ruta_salida)
        ruta_salida.parent.mkdir(parents=True, exist_ok=True)

        codigos = [ticket["codigo"] for ticket in self.tickets]
        esperas_minutos = self.simular()
        espera_promedio = np.mean(esperas_minutos)

        fig, ax = plt.subplots(figsize=(9, 5))
        ax.bar(codigos, esperas_minutos, color="#4C72B0")
        ax.axhline(espera_promedio, color="#DD8452", linestyle="--",
                   label=f"Promedio simulado: {espera_promedio:.2f} min")
        ax.set_title("Espera en cola por ticket (simulación)")
        ax.set_xlabel("Ticket")
        ax.set_ylabel("Espera (minutos)")
        ax.legend()
        fig.tight_layout()
        fig.savefig(ruta_salida, dpi=150)
        plt.close(fig)
