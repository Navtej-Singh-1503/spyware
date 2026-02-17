# spyware
A powerful Linux SPYWARE  --- powered by python3 ---- !! For Education only !!


# CyberForge: Advanced Remote Infiltration & Surveillance Framework

**WARNING: FOR EDUCATIONAL PURPOSES AND SECURITY RESEARCH ONLY.**
*CyberForge is a sophisticated Proof-of-Concept (PoC) demonstrating the mechanics of Remote Access Trojans (RATs). Unauthorized deployment against computer systems without explicit consent is strictly prohibited and carries severe legal consequences.*

---

## Project Overview
**CyberForge** is a dual-component command-and-control (C2) architecture designed for covert system monitoring and remote administrative execution. It bridges the gap between an operator and a remote node using low-level Python socket programming and automated persistence hooks.

### Technical Capabilities
* **Persistence Injection:** Automatically deploys a .desktop entry into the Linux autostart sequence (~/.config/autostart), ensuring the payload re-initializes on every system reboot.
* **Aural Exfiltration:** Remotely triggers high-fidelity audio capture via FFmpeg, streaming raw data from the target's microphone back to the operator.
* **Visual Reconnaissance:** Silent activation of the onboard camera via OpenCV to capture and export environment snapshots without user notification.
* **Geospatial Triangulation:** Extracts real-time physical location, ISP metadata, and network coordinates through IP-API integration.
* **System Enumeration:** Provides a total snapshot of the target’s kernel, hardware architecture, internal IP, and processor specifications.
* **Remote Shell Execution:** Establishes a direct pipeline for arbitrary terminal command injection.
* **Notification Interception:** Scrapes the system journalctl to leak private desktop notifications and incoming message logs.

---

## Structural Anatomy

### 1. The Payload (whitehorse.py)
The primary agent designed to operate with suppressed standard output (os.devnull) to remain invisible to the target user.
* **Self-Healing Dependencies:** Automatically attempts to install opencv-python and libgl1 to ensure surveillance modules remain functional.
* **Socket Listener:** Maintains a dedicated port (9999) to receive and execute remote directives.

### 2. The Setup Engine (setup.py)
The configuration module. It hard-codes the target's network coordinates into the local database, preparing the attack vector.

### 3. The Control Console (main.py)
The operator's dashboard. A custom-built CLI featuring real-time data handling and multi-stream exfiltration.

---

## Deployment Protocol

1. **Initialize Target Vector:**
   ```bash
   python3 setup.py



## Support My Work

You can support me via cryptocurrency:

- LTC : ltc1qspfztcvax7g9caqgdmp3ex6fytrr0dlssr0r45
- URL : litecoin:LTC1QSPFZTCVAX7G9CAQGDMP3EX6FYTRR0DLSSR0R45

---

Copyright © 2026 Navtej Singh Saggar

All rights reserved.

This project and its source code are the intellectual property of
Navtej Singh Saggar. No part of this project may be copied, modified,
distributed, or used for commercial purposes without prior written
permission from the author.
