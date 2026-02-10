## 🛠️Eliminamos el SPOF en sistema de pedidos con arquitectura basada en eventos

# Problema
La empresa X enfrenta un cuello de botella arquitectónico en su servicio de gestión de pedidos, el cual permanece alojado on-premises dentro de una aplicación monolítica, mientras otros subprocesos ya operan en la nube. Esta dependencia genera un SPOF (Single Point of Failure), que bajo cargas elevadas de tráfico o picos de solicitudes concurrentes supera la capacidad de la infraestructura local, provocando indisponibilidad del servicio e impacto directo en los ingresos por ventas. La migración de este módulo busca eliminar esta limitación.

# Criterios para la reestructuración de la arquitectura del subproceso::

Tolerancia a fallos
Escalabilidad
Monitorización y alertas
Optimización de costos

Sistema de microservicios que procesa pedidos en tiempo real utilizando servicios AWS completamente administrados. 
Procesa **100,000+ pedidos/mes** con un **costo promedio de $3.32 USD/mes**.

## 🏗️ Arquitectura

![Arquitectura del Sistema](diagrams/architecture.png)

API Gateway → Recibe solicitudes HTTP POST

SQS (Queue) → Buffer de mensajes asíncrono

Lambda (Processor) → Procesa pedidos y escribe en DynamoDB

DynamoDB Stream → Captura cambios en tiempo real

Lambda (Publisher) → Publica eventos en SNS

SNS Topic → Distribuye notificaciones a múltiples servicios
