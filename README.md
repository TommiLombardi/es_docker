# Flask App con PostgreSQL su Docker

Semplice applicazione Flask che interagisce con un database PostgreSQL, entrambi containerizzati con Docker.

## Pre-requisiti

- Docker
- Docker Compose

## Installazione e avvio

1. **Clona il repository**:
   ```bash
   git clone https://github.com/TommiLombardi/es_docker.git
   ```
1. **Docker Compose**

   ```bash
   docker-compose up -d --build
   ```
1. **Controllo del funzionamento**
   
   visita *http://localhost:5000* per vedere l'applicazione in funzione

## Pulizia

Per fermare e rimuovere i container e i volumi definiti nel file *docker-compose.yml*
```bash
   docker-compose down -v
```
