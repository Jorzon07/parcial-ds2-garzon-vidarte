use("MatriculApp");

db.dropDatabase();

db.createCollection("ticket");
db.createCollection("agente");
db.createCollection("defecto");

db.ticket.insertMany([
  { codigo: "T1", minuto_llegada: 0, minuto_atencion: 5, prioridad: "Alta" },
  { codigo: "T2", minuto_llegada: 3, minuto_atencion: 7, prioridad: "Alta" },
  { codigo: "T3", minuto_llegada: 6, minuto_atencion: 4, prioridad: "Media" },
  { codigo: "T4", minuto_llegada: 14, minuto_atencion: 8, prioridad: "Baja" },
  { codigo: "T5", minuto_llegada: 25, minuto_atencion: 6, prioridad: "Alta" },
  { codigo: "T6", minuto_llegada: 28, minuto_atencion: 5, prioridad: "Media" },
  { codigo: "T7", minuto_llegada: 40, minuto_atencion: 9, prioridad: "Baja" },
  { codigo: "T8", minuto_llegada: 52, minuto_atencion: 4, prioridad: "Alta" },
]);

db.agente.insertMany([
  { nombre: "Laura Cerquera", nivel: "Senior", ticket_por_hora: 10 },
  { nombre: "Andrés Perdomo", nivel: "Junior", ticket_por_hora: 6 },
]);

db.defecto.insertMany([
  { defectos: 28, semana: 1 },
  { defectos: 23, semana: 2 },
  { defectos: 22, semana: 3 },
  { defectos: 17, semana: 4 },
  { defectos: 16, semana: 5 },
  { defectos: 12, semana: 6 },
  { defectos: 12, semana: 7 },
  { defectos: 9, semana: 8 },
]);

db.ticket.find({ prioridad: "Alta" });
db.ticket.find({ minuto_atencion: { $gt: 6 } });
db.defecto.find({ defectos: { $lt: 15 } });

db.ticket.updateOne({ codigo: "T7" }, { $set: { prioridad: "Media" } });

db.ticket.insertOne({ codigo: "T_prueba", minuto_llegada: 90, minuto_atencion: 120, prioridad: "Baja" });
db.ticket.deleteOne({ codigo: "T_prueba" });
