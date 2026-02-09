## 📋 Descripción

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
