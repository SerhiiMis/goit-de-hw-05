# 🛰 GoIT DE Homework 5 — Apache Kafka IoT Monitoring

## 📘 Task Overview

This project simulates a real-time IoT monitoring system using **Apache Kafka** and **Python**. It includes sensor data generation, stream processing, filtering, and alert handling.

---

## 🧱 Architecture

- **Sensor producer** → sends temperature and humidity data to Kafka.
- **Alert processor** → reads the data and sends alerts based on thresholds.
- **Alert listener** → reads alerts from alert topics and prints them.

---

## 🧩 Kafka Topics

Created via `create_topics.py`:

- `building_sensors_serhii_mishovych`
- `temperature_alerts_serhii_mishovych`
- `humidity_alerts_serhii_mishovych`

---

## 🚀 How to Run

> Requires Docker and WSL with Python

1. **Start Kafka**:
   ```bash
   docker compose up -d
   ```
2. **Create topics:**:
   ```bash
   python create_topics.py
   ```
3. **Simulate sensors (in multiple terminals):**:
   ```bash
   python sensor_producer.py
   ```
4. **Process alerts:**:
   ```bash
   python sensor_alert_processor.py
   ```
5. **Display alerts:**:
   ```bash
   python alert_listener.py
   ```

---
