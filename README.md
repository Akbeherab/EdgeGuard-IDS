markdown
<div align="center">

<!-- Animated Cyber Header -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=280&section=header&text=EdgeGuard%20IDS&fontSize=60&fontColor=00f0ff&animation=fadeIn&fontAlignY=35&desc=AI-Driven%20Intrusion%20Detection%20%7C%20Real-Time%20Cyberattack%20Mitigation%20%7C%20Edge%20Computing&descSize=15&descAlignY=58&descColor=c9d1d9" />

<!-- Award Badges -->
<p>
  <img src="https://img.shields.io/badge/🏆_BEST_PAPER_AWARD-IEEE_AIMLA_2026-00f0ff?style=for-the-badge&labelColor=0d1117" />
  <img src="https://img.shields.io/badge/🥇_HACKATHON_WINNER-Cybersecurity_CTF_2024-ff00ff?style=for-the-badge&labelColor=0d1117" />
  <img src="https://img.shields.io/badge/📜_IEEE_Indexed-10.1109/AIMLA67915.2026.11522334-00f0ff?style=for-the-badge&logo=ieee&logoColor=00f0ff&labelColor=0d1117" />
</p>

<!-- Tech Stack Badges -->
<p>
  <img src="https://img.shields.io/badge/Edge_AI-Raspberry%20Pi%204-00f0ff?style=for-the-badge&logo=raspberrypi&logoColor=00f0ff&labelColor=0d1117" />
  <img src="https://img.shields.io/badge/ML-XGBoost%20%7C%20Random%20Forest-ff00ff?style=for-the-badge&logo=python&logoColor=ff00ff&labelColor=0d1117" />
  <img src="https://img.shields.io/badge/Security-iptables%20%7C%20RSA-00f0ff?style=for-the-badge&logo=linux&logoColor=00f0ff&labelColor=0d1117" />
  <img src="https://img.shields.io/badge/Wireless-LoRa%20SX1262-ff00ff?style=for-the-badge&logo=arduino&logoColor=ff00ff&labelColor=0d1117" />
  <img src="https://img.shields.io/badge/Dashboard-Flask%20%7C%20Chart.js-00f0ff?style=for-the-badge&logo=flask&logoColor=00f0ff&labelColor=0d1117" />
</p>

<!-- Status Badges -->
<p>
  <img src="https://img.shields.io/badge/Python-3.11-00f0ff?style=flat-square&logo=python&logoColor=00f0ff&labelColor=0d1117" />
  <img src="https://img.shields.io/badge/Accuracy-98.6%25-00ff88?style=flat-square&labelColor=0d1117" />
  <img src="https://img.shields.io/badge/Latency-<0.5s-00f0ff?style=flat-square&labelColor=0d1117" />
  <img src="https://img.shields.io/badge/Status-Production%20Ready-ff00ff?style=flat-square&labelColor=0d1117" />
  <img src="https://img.shields.io/badge/License-MIT-00f0ff?style=flat-square&labelColor=0d1117" />
</p>

</div>

---

## 📜 Publication

> **EdgeGuard: A Lightweight AI-Driven Intrusion Detection System for Real-Time Cyberattack Mitigation on Edge Devices**
> 
> *Santosh Kumar, **Amit Kumar Behera**, Shashi Ranjan Kumar, Uttam Kumar, Aman Kumar, Asmita, Suresh Kumar Gaddi, Ankit Kumar, Nitin Kumar Puri*
> 
> **2026 4th International Conference on Artificial Intelligence and Machine Learning Applications (AIMLA)** — *Best Paper Award Recipient*
> 
> [![DOI](https://img.shields.io/badge/DOI-10.1109/AIMLA67915.2026.11522334-00f0ff?style=flat-square&logo=ieee&logoColor=00f0ff&labelColor=0d1117)](https://doi.org/10.1109/AIMLA67915.2026.11522334)
> [![IEEE Xplore](https://img.shields.io/badge/IEEE%20Xplore-View%20Paper-ff00ff?style=flat-square&logo=ieee&logoColor=ff00ff&labelColor=0d1117)](https://ieeexplore.ieee.org/document/11522334)

---

## 🎯 Research Abstract

**EdgeGuard** is a **plug-and-play, lightweight, real-time Intrusion Detection System (IDS)** engineered for resource-constrained edge environments. Deployed on **Raspberry Pi 4**, the system detects and mitigates cyber-attacks — including DDoS, brute-force SSH, and port scans — using ensemble machine learning models that execute entirely at the network edge.

By bridging the device **between the router and switch**, EdgeGuard passively monitors all ingress/egress traffic, predicts threats via **XGBoost + Random Forest** ensemble, and auto-blocks malicious actors through native `iptables` firewall rules within **<<500ms**. The architecture is **zero-cloud** by design: no packet metadata, biometric signatures, or threat telemetry ever leaves the local device, ensuring complete data sovereignty for defense, healthcare, and air-gapped installations.

**Key Contributions:**
- 🧠 **Hybrid ML Ensemble**: XGBoost primary classifier with Random Forest fallback, optimized for ARM Cortex-A72 NEON instruction set
- ⚡ **Sub-Second Mitigation**: Automated `iptables` blocking with end-to-end latency <0.5s on Raspberry Pi 4 (4GB)
- 🔒 **Zero-Cloud Architecture**: 100% offline inference — ideal for remote defense outposts and rural critical infrastructure
- 📡 **LoRa SX1262 Telemetry**: Optional wireless alert transmission for distributed IoT security networks
- 📊 **Real-Time Flask Dashboard**: Live CPU/RAM/traffic visualization with Chart.js and AJAX polling
- 🚨 **Multi-Channel Alerting**: Twilio SMS + SMTP email with RSA signature verification for API authenticity

---

## 🏆 Achievements & Awards

<div align="center">

| Award | Venue | Year |
|:---|:---|:---:|
| 🥇 **Best Paper Award** | IEEE AIMLA 2026 | 2026 |
| 🏆 **Cybersecurity Hackathon Winner** | National-Level CTF / Defense Hackathon | 2024 |
| 🎓 **Samsung ISWDP Fellowship** | IISc Bengaluru | — |

</div>

---

## 🏗️ System Architecture

<div align="center">

```
┌─────────────────┐     ┌─────────────────────────────────────────┐     ┌─────────────────┐
│    Internet     │────▶│           🔒 EdgeGuard IDS              |────▶│     Switch      │
│                 │     │      (Raspberry Pi 4, 4GB RAM)          │     │                 │
└─────────────────┘     │  ┌─────────────────────────────────┐    │     └─────────────────┘
                        │  │     🧠 ML Inference Engine      │    │            │
                        │  │  • XGBoost Classifier           │     │           ▼
                        │  │  • Random Forest Fallback       │     │     ┌─────────────┐
                        │  │  • Real-time Anomaly Prediction │     │     │  Devices    │
                        │  │  • 128-d Feature Embedding    │       │     │  • Laptops  │
                        │  └─────────────────────────────────┘     │     │  • Phones   │
                        │  ┌─────────────────────────────────┐     │     │  • IoT      │
                        │  │     🛡️ Threat Mitigation       │      │     └─────────────┘
                        │  │  • iptables Auto-Block          │      │
                        │  │  • Dynamic Blacklist Manager    │      │
                        │  │  • Rate Limiting & Quarantine   │      │
                        │  └─────────────────────────────────┘      │
                        │  ┌─────────────────────────────────┐      │
                        │  │     📡 LoRa SX1262 Telemetry    │      │
                        │  │  • Wireless Alert Broadcast     │      │
                        │  │  • Long-Range IoT Integration   │      │
                        │  └─────────────────────────────────┘      │
                        │  ┌─────────────────────────────────┐      │
                        │  │     📊 Monitoring & Alerts      │      │
                        │  │  • Flask Dashboard (Chart.js)   │      │
                        │  │  • Twilio SMS Notifications     │      │
                        │  │  • SMTP Email Summaries         │      │
                        │  │  • RSA Signature Verification   │      │
                        │  └─────────────────────────────────┘      │
                        └─────────────────────────────────────────┘
```

</div>

---

## ⚙️ Technical Stack

<div align="center">

| Layer | Technology | Purpose |
|:---|:---|:---|
| **Edge Hardware** | Raspberry Pi 4 (4GB) + Pi Camera v2 | Embedded inference & network bridge |
| **Wireless Module** | LoRa SX1262 (Semtech) | Long-range alert telemetry for IoT networks |
| **Operating System** | Raspberry Pi OS (64-bit Debian) | Hardened Linux foundation |
| **ML Engine** | XGBoost + Random Forest | Anomaly classification & threat detection |
| **Dataset** | MQTT-Based Intrusion Detection Dataset | Training & adversarial validation |
| **Web Framework** | Flask + Jinja2 + Chart.js + AJAX | Real-time dashboard & REST API |
| **System Telemetry** | psutil + netstat + scapy | CPU, RAM, packet-level monitoring |
| **Network Security** | iptables + RSA-2048 + hashlib | Auto-blocking & request verification |
| **Alerting** | Twilio REST API + smtplib (TLS) | Multi-channel threat notifications |
| **Adversarial Testing** | hping3 + hydra + nmap + scapy + Wireshark | Controlled penetration validation |

</div>

---

## 🚀 Core Capabilities

### 🧠 AI-Powered Threat Detection
- **XGBoost Classifier** (primary) with **Random Forest** fallback ensemble
- Trained on real-world **MQTT intrusion dataset** with 10 engineered statistical features
- **98.6% test accuracy** with prediction latency **<<0.5s** on ARM Cortex-A72
- Detects DDoS floods, SSH brute-force, port reconnaissance, and zero-day anomaly signatures

### 🛡️ Real-Time Auto-Mitigation
- Automated malicious IP blocking via native `iptables` `DROP` / `REJECT` rules
- Dynamic blacklist persistence with configurable TTL and manual unblock controls
- Passive network bridge topology — **zero configuration** of existing infrastructure
- Rate-limiting and connection quarantine for suspected attack vectors

### 📡 LoRa Wireless Telemetry
- **Semtech SX1262** long-range radio module integration (`lora_transfer.py`)
- Broadcasts encrypted alert packets to remote monitoring stations (up to 15km LOS)
- Enables **distributed IoT security mesh** across campuses, defense perimeters, or agricultural networks
- AES-128 encrypted payload transmission with frequency hopping

### 📊 Live Flask Dashboard
- Real-time CPU, RAM, disk, and network latency telemetry
- Attack detection logs with **severity classification** (Critical / High / Medium / Low)
- Auto-blocked IP registry with geolocation enrichment and unblock controls
- Traffic statistics rendered via **Chart.js** with 1-second AJAX polling
- Secure access via `http://[pi-ip]:5000` with session-based authentication

### 🚨 Intelligent Alerting
- **Twilio SMS** push notifications to admin mobile upon critical threat detection
- **SMTP email** digests with attack summary, timestamp, and recommended actions
- **RSA-2048 signature verification** for all dashboard API request authenticity

### 🌐 Offline-First Design
- Complete autonomy from cloud services, internet, or external APIs
- Ideal for **defense outposts**, **rural critical infrastructure**, **air-gapped laboratories**

---

## 🔬 Machine Learning Pipeline

### Feature Engineering
| Feature | Description | Importance |
|:---|:---|:---:|
| `duration` | Connection session length (seconds) | 🔴 High |
| `bytes_sent` | Total outbound data volume (bytes) | 🔴 High |
| `packets` | Packet count per flow | 🔴 High |
| `src_port` / `dst_port` | Source & destination port numbers | 🟡 Medium |
| `protocol` | Transport layer protocol (TCP/UDP/ICMP) | 🟡 Medium |
| `ack_flags` | TCP ACK flag frequency | 🔴 High |
| `packet_size_variance` | Statistical variance in packet sizes | 🔴 High |
| `flow_rate` | Packets-per-second throughput | 🔴 High |
| `latency` | Round-trip time (RTT) measurement | 🟡 Medium |
| `inter_arrival_time` | Mean packet inter-arrival delta | 🟡 Medium |

### Model Configuration
```python
# Primary Classifier: XGBoost (gradient-boosted trees)
primary = XGBClassifier(
    n_estimators=250,
    max_depth=7,
    learning_rate=0.08,
    subsample=0.85,
    colsample_bytree=0.85,
    reg_alpha=0.1,
    reg_lambda=1.0,
    tree_method='hist',        # Optimized for ARM
    n_jobs=2                   # Dual-core parallelism on Pi 4
)

# Fallback Classifier: Random Forest (bagging ensemble)
fallback = RandomForestClassifier(
    n_estimators=200,
    max_depth=12,
    criterion='entropy',
    min_samples_split=5,
    n_jobs=2,
    class_weight='balanced'
)

# EdgeGuard Inference Performance
┌────────────────────┬─────────────┬──────────────┐
│ Metric             │ Raspberry Pi│ x86 Reference│
├────────────────────┼─────────────┼──────────────┤
│ Accuracy           │ 98.6%       │ 99.1%        │
│ Precision          │ 98.4%       │ 98.9%        │
│ Recall             │ 98.9%       │ 99.3%        │
│ F1-Score           │ 98.6%       │ 99.1%        │
│ Inference Latency  │ ~450 ms     │ ~85 ms       │
│ Memory Footprint   │ ~310 MB     │ ~520 MB      │
│ Power Draw         │ 5.1 W       │ 42 W         │
└────────────────────┴─────────────┴──────────────┘
```

### 🔗 Reproduce Training
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1y0vSX56S7ObC94boj3f7vqQOSScpUTS7)

---

## 🧪 Adversarial Validation

All attack vectors were simulated in isolated virtualized environments with explicit authorization:

| Tool | Attack Vector | Validation Command |
|:---|:---|:---|
| **hping3** | SYN Flood / DDoS | `hping3 -S -p 80 --flood --rand-source <target>` |
| **hydra** | SSH Brute Force | `hydra -l root -P rockyou.txt ssh://<<target> -t 16` |
| **nmap** | Network Reconnaissance | `nmap -sS -sV -O -p 1-65535 -T4 <target>` |
| **netcat** | Bind Shell / Backdoor | `nc -e /bin/bash -lvp 4444` |
| **scapy** | Custom Packet Crafting | Python-based zero-day signature simulation |
| **Wireshark** | Traffic Analysis | Real-time packet capture & IDS reaction verification |

> **Ethical Compliance:** All penetration testing was conducted in controlled lab environments. No production networks were engaged without written authorization.



## 🛠️ Installation & Deployment

### Hardware Bill of Materials
| Component | Specification | Qty |
|:---|:---|:---:|
| Raspberry Pi 4 | 4GB RAM, 64-bit OS | 1 |
| MicroSD Card | 32GB+, Class 10 UHS-I | 1 |
| Ethernet Cables | Cat6, 1m | 2 |
| LoRa Module | SX1262 HAT (optional) | 1 |
| Power Supply | 5V/3A USB-C | 1 |

### Step 1 — Network Bridge Configuration
```bash
# Enable IP forwarding & configure bridge interfaces
sudo nano /etc/sysctl.conf
# Uncomment: net.ipv4.ip_forward=1

# Configure static IPs for eth0_in (router side) and eth0_out (switch side)
sudo nano /etc/dhcpcd.conf
```

### Step 2 — Clone & Bootstrap
```bash
git clone https://github.com/amitkumarbehera/EdgeGuard-IDS.git
cd EdgeGuard-IDS

chmod +x setup.sh
sudo ./setup.sh    # Installs deps, configures iptables, initializes SQLite
```

### Step 3 — Configure Alert Channels
```bash
nano config.yaml

# Twilio Credentials
twilio:
  account_sid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  auth_token: "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"
  from_number: "+1XXXXXXXXXX"
  to_numbers: ["+91-9431064363", "+91-7981971154"]

# SMTP Configuration
smtp:
  host: "smtp.gmail.com"
  port: 587
  username: "edgeguard.alerts@gmail.com"
  password: "app-specific-password"
  tls: true

# RSA Key Pair (auto-generated if absent)
rsa:
  key_size: 2048
  private_key: "./keys/edgeguard_private.pem"
  public_key: "./keys/edgeguard_public.pem"
```

### Step 4 — Launch
```bash
sudo python dashboard/app.py
# Dashboard: http://[pi-ip]:5000
# Default admin: admin / EdgeGuard2024!
```

---

## 📦 Requirements

```txt
xgboost==2.0.3
scikit-learn==1.3.2
flask==3.0.0
flask-login==0.6.3
pandas==2.1.4
numpy==1.26.2
psutil==5.9.6
twilio==8.10.0
pycryptodome==3.19.0
pyyaml==6.0.1
requests==2.31.0
scapy==2.5.0
pyserial==3.5          # For LoRa SX1262 UART
smbus2==0.4.2          # For I2C peripheral communication
```

---

## 🔮 Research Roadmap

- [ ] **Edge TPU Acceleration**: Google Coral USB integration for 10x inference speedup
- [ ] **Deep Packet Inspection**: Lightweight DPI module for payload-level threat analysis
- [ ] **Federated Threat Intelligence**: Decentralized model updates via secure gossip protocol
- [ ] **Reinforcement Learning**: Adaptive blocking policies via Deep Q-Network agent
- [ ] **Docker Containerization**: Full OCI packaging for Kubernetes edge orchestration
- [ ] **IPv6 Dual-Stack**: Complete next-generation network layer support
- [ ] **TLS Inspection**: Ethical encrypted traffic analysis via passive decryption

---

## 📚 Citation

If this work contributes to your research, please cite:

```bibtex
@INPROCEEDINGS{11522334,
  author={Kumar, Santosh and Behera, Amit Kumar and Kumar, Shashi Ranjan and Kumar, Uttam and Kumar, Aman and Asmita and Gaddi, Suresh Kumar and Kumar, Ankit and Puri, Nitin Kumar},
  booktitle={2026 4th International Conference on Artificial Intelligence and Machine Learning Applications Theme: Healthcare and Internet of Things (AIMLA)}, 
  title={EdgeGuard: A Lightweight AI-Driven Intrusion Detection System for Real-Time Cyberattack Mitigation on Edge Devices}, 
  year={2026},
  volume={},
  number={},
  pages={1-6},
  keywords={Modeling;Machine learning;Signal detection;Internet of Things;Printing;Random forests;Poles and zeros;Fluid flow;Intrusion detection;Machining;Intrusion Detection System;Edge Computing;Cybersecurity;Machine Learning;Raspberry Pi;Anomaly Detection;IoT Security;Real-time Threat Mitigation;Random Forest;Zero-Day Attack Detection},
  doi={10.1109/AIMLA67915.2026.11522334}
}
```

---

## 👥 Research Team

<div align="center">

| Researcher | Role | Affiliation |
|:---|:---|:---|
| **Amit Kumar Behera** | Project Lead · ML & Edge AI Architecture | IIT Patna / IIT Madras |
| **Santosh Kumar** | Penetration Testing & Adversarial QA | Research Collaborator |
| **Shashi Ranjan Kumar** | Flask Dashboard & Frontend Engineering | Research Collaborator |
| **Uttam Kumar** | Dataset Engineering & Feature Selection | Research Collaborator |
| **Aman Kumar** | Network Security & iptables Integration | Research Collaborator |
| **Asmita** | System Testing & Validation | Research Collaborator |
| **Suresh Kumar Gaddi** | LoRa Wireless & IoT Deployment | Research Collaborator |
| **Ankit Kumar** | Alerting & Monitoring Systems | Research Collaborator |
| **Nitin Kumar Puri** | Research Advisor & Domain Expert | Research Collaborator |

</div>

---

## 🔗 Connect & Collaborate

<div align="center">

<p>
  <a href="https://www.linkedin.com/in/amit-behera9/">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0d1117" />
  </a>
  <a href="https://scholar.google.com/citations?user=IjqXBEoAAAAJ&hl=en&authuser=1">
    <img src="https://img.shields.io/badge/Google%20Scholar-4285F4?style=for-the-badge&logo=google-scholar&logoColor=white&labelColor=0d1117" />
  </a>
  <a href="https://orcid.org/0009-0004-6970-9357">
    <img src="https://img.shields.io/badge/ORCID-A6CE39?style=for-the-badge&logo=orcid&logoColor=white&labelColor=0d1117" />
  </a>
  <a href="mailto:amitkumarbehera@email.com">
    <img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0d1117" />
  </a>
</p>

**Research Interests:** Edge AI · Medical Imaging · Self-Supervised Learning · Embedded Computer Vision · IoT Security · Healthcare AI · Federated Learning

</div>

---

<div align="center">

### ⭐ Star this repository to support decentralized, open-source cybersecurity research

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=120&section=footer&text=&fontSize=0" />

<p><i><span style="color:#00f0ff">"Intelligence at the edge.</span> <span style="color:#ff00ff">Security at the speed of light."</span></i></p>

</div>
```
