import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from modelo import MesaDeAyuda

TICKETS_MATRICULAPP = [
    {"codigo": "T1", "minuto_llegada": 0, "minuto_atencion": 5},
    {"codigo": "T2", "minuto_llegada": 3, "minuto_atencion": 7},
    {"codigo": "T3", "minuto_llegada": 6, "minuto_atencion": 4},
    {"codigo": "T4", "minuto_llegada": 14, "minuto_atencion": 8},
    {"codigo": "T5", "minuto_llegada": 25, "minuto_atencion": 6},
    {"codigo": "T6", "minuto_llegada": 28, "minuto_atencion": 5},
    {"codigo": "T7", "minuto_llegada": 40, "minuto_atencion": 9},
    {"codigo": "T8", "minuto_llegada": 52, "minuto_atencion": 4},
]


def test_wq_mm1_con_lambda_8_y_mu_10():
    mesa = MesaDeAyuda(TICKETS_MATRICULAPP, mu=10)

    metricas = mesa.metricas_mm1(8)

    assert abs(metricas["Wq"] - 0.4) < 1e-9


def test_simulacion_espera_hasta_que_termina_el_ticket_anterior():
    mesa = MesaDeAyuda(TICKETS_MATRICULAPP, mu=10)

    assert mesa.simular() == [0, 2, 6, 2, 0, 3, 0, 0]


if __name__ == "__main__":
    test_wq_mm1_con_lambda_8_y_mu_10()
    test_simulacion_espera_hasta_que_termina_el_ticket_anterior()
    print("Pruebas OK")
