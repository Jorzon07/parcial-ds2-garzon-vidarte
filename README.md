## Proyecto MatriculApp

### Integrantes

- Jorge Garzón
- Juan Vidarte

### Nombre de la base de datos: MatriculApp

#### Colecciones:

- **ticket**: codigo, minuto_llegada, minuto_atencion, prioridad.
- **agente**: nombre, nivel, ticket_por_hora
- **defecto**: defectos, semana


| ticket | tipo de dato |
| :---: | :---: |
| codigo | Se refiere al codigo del ticket (T1, T2, T...)
| minuto_llegada | El minuto en que llega el ticket (min) |
| minuto_atencion | El minuto en que se atiende el ticket (min) |
| prioridad | La prioridad del ticket (Alta, Media, Baja) |

| agente | tipo de dato |
| :---: | :---: |
| nombre | Se refiere al nombre del agente (Laura, Andrés) |
| nivel | El nivel del agente (junior, senior) |
| ticket_por_hora | El numero de tickets que atiende el agente por hora (tickets/hora) |

| defecto | tipo de dato |
| :---: | :---: |
| defectos | Se refiere al numero de defectos (defectos)|
| semana | La semana en que se registraron los defectos (w) |


## ¿Como se relacionan?


[ agente ] ──(nombre)──> [ ticket ] <──(semana)── [ defecto ]
<<<<<<< HEAD

## Opción escogida: A · Teoría de colas (`MesaDeAyuda`)

- `src/modelo.py`: clase `MesaDeAyuda(tickets, mu)` con `tasa_llegadas()`, `metricas_mm1(lam)`, `simular()` y `graficar()`.
- `src/main.py`: lee `ticket` y `agente` de MongoDB, crea el objeto y ejecuta los cálculos.
- μ = 10 tickets/hora, tomado del agente Senior (Laura Cerquera), porque el modelo M/M/1 tiene un solo servidor.
- λ se calcula con el tiempo promedio entre llegadas: 52 min / 7 intervalos ≈ 7.43 min → **λ ≈ 8.08 tickets/hora**.

### Cómo ejecutar

```bash
pip install -r requirements.txt
mongosh --file mongo/script_mongosh.js
python src/main.py
python -m pytest tests
```

### Resultados

| Métrica | Valor |
| :--- | :---: |
| λ | 8.08 tickets/hora |
| μ | 10 tickets/hora |
| ρ = λ/μ | 0.81 |
| Lq = ρ²/(1−ρ) | 3.39 tickets |
| Wq teórico = ρ/(μ−λ) | 0.42 h ≈ 25.2 min |
| Wq simulado (promedio) | 1.62 min |
| Wq con λ = 9.5 | 1.9 h = 114 min |

Esperas simuladas por ticket (Inicio = máx(Llegada, Fin anterior)): T1 0, T2 2, T3 6, T4 2, T5 0, T6 3, T7 0, T8 0 minutos.

![Espera por ticket](graficas/resultado.png)

## Interpretación

**¿Cuánto espera un usuario?** Según la teoría M/M/1, un usuario esperaría en cola unos **25 minutos** (0.42 h). Según la simulación con los datos reales, la espera promedio es de apenas **1.6 minutos**, y 4 de los 8 tickets no esperaron nada.

**¿Por qué difieren?**

1. **Muestra pequeña:** solo hay 8 tickets en menos de una hora; la fórmula describe el promedio de un sistema que lleva funcionando mucho tiempo (estado estable).
2. **El sistema arranca vacío:** la simulación empieza sin cola, mientras que el modelo supone que la cola ya se acumuló.
3. **Menos variabilidad que la supuesta:** M/M/1 asume llegadas y atenciones exponenciales (muy variables). En los datos, las atenciones están entre 4 y 9 minutos y las llegadas son bastante espaciadas, así que casi no se forman colas.
4. **ρ ≈ 0.81 es alto:** con esa ocupación, el modelo predice que basta una racha de llegadas seguidas para que la cola crezca mucho; eso no alcanzó a pasar en estos 8 tickets, pero sí se ve un inicio con T2–T4.

**¿Qué pasa si la demanda sube a 9.5 tickets/hora?** ρ = 0.95 y Wq = 0.95 / (10 − 9.5) = **1.9 horas (114 min)**, unas 4.5 veces más que con λ ≈ 8.08. Lq sube a ~18 tickets en cola. Como Wq crece con 1/(μ − λ), cerca de la capacidad del agente cualquier aumento pequeño de demanda dispara la espera; habría que sumar al agente Junior o reforzar la atención.

**Prueba:** con λ = 8 y μ = 10 se verifica que Wq = 0.8 / 2 = 0.4 horas (`tests/test_modelo.py`).
=======


