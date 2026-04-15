# 📊 Project 1: Monitoring & Alerting System

## 🚀 Overview

This project implements a complete monitoring and alerting system using Prometheus, Node Exporter, Grafana, and Alertmanager with webhook integration.

---

## 🛠️ Tech Stack

* Prometheus
* Grafana
* Node Exporter
* Alertmanager
* Flask (Webhook Receiver)
* Docker

---

## ⚙️ Features

* Monitors Flask application health
* Collects system metrics (CPU, Memory)
* Triggers alert when application goes down
* Sends alert to webhook (Flask server)
* Displays metrics in Grafana dashboard

---

## 🔔 Alerting Logic

* Alert Name: AppDown
* Condition: up == 0
* Duration: 10 seconds

---

## 🔄 Workflow

App Down → Prometheus → Alertmanager → Webhook → Terminal Output

---

## 📸 Output

* Alert firing in Prometheus
* Alert received in Alertmanager
* Webhook prints:

```
ALERT RECEIVED:
{...JSON...}
```

---

## 🧠 Challenges Solved

* Docker ↔ WSL networking issues
* Alertmanager configuration issues
* Webhook integration debugging

---

## ✅ Result

Successfully implemented end-to-end monitoring and alerting system.

---

## 👨‍💻 Author

Charan Teja
