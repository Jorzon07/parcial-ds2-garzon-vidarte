## Proyecto MatriculApp

### Nombre de la base de datos: MatriculApp

#### Colecciones:

- **ticket**: codigo, minuto_llegada, minuto_atencion, prioridad.
- **agente**: nombre, nivel, ticket_por_hora
- **defectos**: defectos, semana


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

| defectos | tipo de dato |
| :---: | :---: |
| defectos | Se refiere al numero de defectos (defectos)|
| semana | La semana en que se registraron los defectos (w) |


## ¿Como se relacionan?


[ agente ] ──(nombre)──> [ ticket ] <──(semana)── [ defectos ]

