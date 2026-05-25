# AI-Powered Anomaly-Based Intrusion Detection System (IDS)

> Built using Raspberry Pi 4, this project is a **plug-and-play, lightweight, and real-time IDS** designed for detecting and mitigating cyber-attacks such as DDoS, brute-force, and port scans. It features automated IP blocking, real-time system monitoring, and a live Flask-based dashboard.

---

## Table of Contents

- [📖 Project Summary](#-project-summary)
- [🎯 Target Audience](#-target-audience)
- [🛠️ Tech Stack](#️-tech-stack)
- [📐 System Architecture](#-system-architecture)
- [💡 Key Features](#-key-features)
- [🧠 Machine Learning Details](#-machine-learning-details)
- [📈 Live Dashboard](#-live-dashboard)
- [⚙️ Installation & Usage](#️-installation--usage)
- [🧪 Testing Tools](#-testing-tools)
- [📦 Product Launch Strategy](#-product-launch-strategy)
- [💥 Future Impact](#-future-impact)
- [❌ Known Limitations](#-known-limitations)
- [🏆 Why This Project Stands Out](#-why-this-project-stands-out)
- [👥 Team Members](#-team-members)
- [📞 Contact](#-contact)

---

## 📖 Project Summary

This AI-Powered IDS is a **cost-effective, real-time network defense tool** intended for homes, schools, and small organizations. It monitors incoming network data traffic, detects threats using trained ML models, auto-blocks malicious IPs via `iptables`, and displays everything on a clean Flask dashboard.

The system is **plugged in between the router and switch** for seamless traffic analysis, designed to work even in offline environments (ideal for remote and rural deployments).

---
## Target Audience

- 👨‍🏫 Educational Institutes and Labs  
- 🏠 Smart Homes and IoT Networks  
- 🏢 Small & Medium Enterprises (SMEs)  
- 🛡️ Defense and Government Organizations  
- 🧠 Research Labs and Cybersecurity Students

---

## 🛠️ Tech Stack

| Component       | Tool/Library                         |
|----------------|--------------------------------------|
| Device          | Raspberry Pi 4 (4 GB RAM)           |
| OS              | Raspberry Pi OS (Debian-based)      |
| Programming     | Python 3.11                         |
| ML Model        | XGBoost / Random Forest             |
| Data Source     | MQTT-Based Intrusion Dataset        |
| Dashboard       | Flask + HTML + Chart.js + AJAX      |
| Monitoring      | psutil, netstat                     |
| Security        | iptables, RSA                       |
| Alerts          | Twilio (SMS), smtplib (Email)       |
| Testing Tools   | hping3, hydra, netcat, Wireshark    |

---

## 📐 System Architecture
          [Internet]
               |
           [Router]
               |
   
   │ Raspberry Pi IDS   │
   │ - ML Prediction    │
   │ - Real-time Block  │
   │ - Dashboard View   │

               |
            [Switch]
               |
      [All Connected Devices]

      📍 Plug-and-play model: Just insert the Raspberry Pi between your **router and switch**, and the IDS starts passively monitoring and defending.

---

## 💡 Key Features

- ✅ Real-time detection of threats  
- 🔒 Auto-blocks IPs using `iptables`  
- 📊 Flask-based real-time dashboard  
- 🧠 AI Model trained on real-world intrusion dataset  
- 🚨 Sends SMS/Email alerts upon detection  
- 🔐 RSA signature verification for request authenticity  
- 🌐 Works fully offline (perfect for remote areas)

---

## 🧠 Machine Learning Details

- **Dataset Used**: MQTT-Based Intrusion Detection Dataset
- **Model**: XGBoost Classifier (with fallback Random Forest)
- **Top 10 Features Used**:
  - Duration
  - Bytes Sent
  - Packets
  - Source Port
  - Destination Port
  - Protocol
  - ACK Flags
  - Packet Size Variance
  - Flow Rate
  - Latency
- **Accuracy**: ~98.6% on test set
- **Prediction Time**: < 0.5 sec on Raspberry Pi 4

---

## 📈 Live Dashboard

The Flask web dashboard provides:

- Real-time CPU, RAM, and latency monitoring
- Attack detection logs
- Auto-blocked IP list
- Network traffic statistics
- Graphs powered by Chart.js

🔗 Access via: `http://<your-pi-ip>:5000`

![Dashboard Screenshot](https://via.placeholder.com/800x400?text=Live+Dashboard+Preview)

---

## ⚙️ Installation & Usage
---

## 🧪 Testing Tools

We simulated real-world attacks using widely recognized open-source tools to validate the effectiveness and responsiveness of our IDS system.

| Tool        | Use Case & Command Example                                                                 |
|-------------|---------------------------------------------------------------------------------------------|
| **hping3**  | Simulate DDoS or SYN Floods: `hping3 -S -p 80 --flood <target-IP>`                          |
| **hydra**   | SSH Brute Force: `hydra -l root -P passwords.txt ssh://<target-IP>`                         |
| **nmap**    | Scan network services: `nmap -sS -p 1-65535 -T4 <target-IP>`                                |
| **netcat**  | Open fake ports to test scanning response: `nc -lvp 9999`                                   |
| **Wireshark** | Monitor packet capture and IDS reaction in real time.                                    |
| **scapy**   | Custom packet crafting to test unknown or zero-day signatures.                             |

> All tests were conducted in a controlled environment using isolated virtual machines and routers.

---

## 📦 Product Launch Strategy

This project is designed to be **production-ready** with minimal setup, enabling even non-technical users to protect their networks.

### 🛒 Go-to-Market Plan:
- Package as a **pre-configured Raspberry Pi device** with everything preloaded.
- Create a **no-code dashboard setup** that boots up instantly on power-on.
- Provide a plug-and-play hardware solution to be placed **between router and switch**.

### 📘 Product Package Includes:
- Raspberry Pi with IDS pre-installed
- SD card pre-flashed with software and OS
- Access credentials for the dashboard
- Setup manual and quick start guide
- Alert configuration instructions for SMS/Email

### 🏁 Initial Launch Focus:
- 1,000+ Schools & Colleges across India
- MSMEs with limited cybersecurity infrastructure
- NGOs and Government offices in Tier-2/3 cities

---

## 💥 Future Impact

This system lays the groundwork for **decentralized, low-cost cybersecurity** in India. Here’s how it scales:

- 🌍 **Rural & Remote Protection**  
  No internet required – works offline. Ideal for defense installations, rural labs, or unmanned stations.

- 🏫 **Cybersecurity for Education**  
  Can serve as a training tool for students. Helps implement **"Cybersecurity Literacy"** at grassroots.

- 🌐 **Federated Threat Intelligence**  
  In future, multiple devices can form a **decentralized learning network**, sharing anonymized attack patterns.

- 🧠 **Adaptive Threat Response**  
  With future upgrades, we plan to incorporate **self-healing, reinforcement learning**, and **zero-trust architecture**.

---

## ❌ Known Limitations

While powerful, the current version of our IDS system has some limitations that are being actively worked on:

| Limitation                                 | Current Status / Reason                                |
|--------------------------------------------|----------------------------------------------------------|
| No Deep Packet Inspection (DPI)            | To keep the model light for Raspberry Pi                |
| No HTTPS Packet Decryption                 | Due to legal and ethical restrictions                   |
| IPv6 Not Fully Supported                   | Currently optimized for IPv4                            |
| Not Yet Dockerized                         | Will be packaged in Docker in a future release          |
| ML Model is Static                         | Does not yet auto-learn from new threats (WIP)          |
---

## 🏆 Why This Project Stands Out

| Feature                        | Benefit                                                                 |
|-------------------------------|--------------------------------------------------------------------------|
| 🎯 Edge AI Integration         | Smart detection directly on Raspberry Pi                                |
| 🔧 Plug-and-Play Setup         | Zero configuration needed post-boot                                     |
| 📊 Live Web Dashboard          | Monitor threats, resources, and logs in real time                       |
| 🧠 AI-Based Classification      | Uses trained ML models to accurately predict threats                    |
| 🔒 Automated IP Blocking       | Prevents damage by instantly blocking attack sources                    |
| 🚨 Real-Time Alerts            | Sends notification on threat detection                                     |
| 🌐 Offline Capability          | Fully functional even without internet access                           |
| 💸 Cost-effective & Scalable   | Ideal for widespread rural, defense, and SME deployment in India        |

---

## 👥 Team Members

| Name                   | Role                                | Contributions                                            |
|------------------------|-------------------------------------|----------------------------------------------------------|
| **Amit Kumar Behera**  | Project Lead, ML & IoT Developer    | Model training, firewall integration, system architect   |
| **Shashi Ranjan Kumar**| Frontend & Dashboard Developer      | Flask app, real-time chart integration                   |
| **Uttam Kumar**        | Dataset Preprocessing & Feature Selection | Cleaned and extracted top 10 features              |
|  **Santosh Kumar**     | Penetration Testing & QA            | hping3, hydra attack simulation, stress testing          |

---

## 📞 Contact

If you're interested in deploying or supporting this project:

- 📞 Phone 1: **+91-9431064363**
- 📞 Phone 2: **+91-7981971154**
- 🌐 GitHub: [github.com/amitkumarbehera](https://github.com/amitkumarbehera)
- 🧪 Project Demo: _Available upon request or during live hackathon presentation_

> _Let’s make cybersecurity accessible, intelligent, and affordable for every corner of India._

---
