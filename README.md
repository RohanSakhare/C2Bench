 C2Bench – Command & Control Detection Benchmark

A lightweight framework to simulate, detect, and analyze Command-and-Control (C2) traffic using Python, Suricata, Elasticsearch, and Docker.

📌 Overview

C2Bench is a cybersecurity project designed to simulate beacon-based Command & Control (C2) communication and evaluate detection mechanisms using IDS and log analytics technologies.

This framework allows students, researchers, and SOC analysts to:

Generate realistic C2 beacon traffic

Capture network events using Suricata IDS

Store logs in Elasticsearch

Visualize activity using Kibana dashboards

Understand how C2 traffic behaves across monitoring layers

This project serves as a practical demonstration for academic submissions and cybersecurity interviews.

🧱 Project Architecture
+--------------+         Beacon         +---------------+
|   C2 Agent   | ---------------------> |   C2 Server   |
| (beacon.py)  | <--------------------- | (server.py)   |
+--------------+       Commands         +---------------+
         |                                      |
         +------------ Network Traffic ---------+
                        |
                        ▼
                +---------------+
                |   Suricata   |
                +---------------+
                        |
                        ▼
              +--------------------+
              |   Elasticsearch    |
              +--------------------+
                        |
                        ▼
                +---------------+
                |    Kibana     |
                +---------------+

📂 Folder Structure
C2Bench/
│── c2_server/
│   ├── server.py
│   └── Dockerfile
│
│── c2_agent/
│   ├── beacon.py
│   └── Dockerfile
│
│── sensors/
│   └── suricata/
│        ├── classification.config
│        ├── reference.config
│        ├── suricata.yaml
│        ├── threshold.config
│        └── update.yaml
│
│── detect_beacon.zeek
│── beacon_times.txt
│── beacons.tsv
│── docker-compose.yml
│── intervals.txt
│── README.md

🚀 Features
🔹 C2 Agent

Generates encrypted Base64 beacons

Sends randomized interval traffic

Mimics real malware behaviour

🔹 C2 Server

Receives beacons on port 8000

Logs agent ID, hostname, payload

Responds with commands (extensible)


Outputs machine-readable JSON logs

🔹 Elasticsearch + Kibana

Stores processed JSON logs

Builds dashboards for threat visibility

Helps analyze beacon patterns over time

🛠️ Setup Instructions
1️⃣ Clone the repository
git clone https://github.com/RohanSakhare/C2Bench.git
cd C2Bench

2️⃣ Start all components using Docker
docker-compose up --build

3️⃣ Run the agent
python3 c2_agent/beacon.py

4️⃣ View logs

Suricata logs → Elasticsearch

Kibana dashboards → http://localhost:5601

C2 server logs → Docker container console

🖼️ Screenshots / Demo
📸 Agent Beacon Output
<img width="1550" height="137" alt="Screenshot 2025-12-11 185958" src="https://github.com/user-attachments/assets/2955732f-8cd0-418e-a5fa-eee571839feb" />



📸 C2 Server Processing Beacons

<img width="1600" height="790" alt="image" src="https://github.com/user-attachments/assets/fc946961-56dd-4eb3-89db-42a5f95ba6a5" />


📸 Suricata Log Output

<img width="1676" height="860" alt="image" src="https://github.com/user-attachments/assets/19295291-e390-4a3d-89af-1f13dcc00cef" />


📸 Kibana Dashboard Visualization
<img width="1851" height="848" alt="Screenshot 2025-12-11 171055" src="https://github.com/user-attachments/assets/bf16fad1-bea7-4e86-a866-38a93ac587ca" />
<img width="1858" height="584" alt="Screenshot 2025-12-11 171107" src="https://github.com/user-attachments/assets/84bf2615-89ef-4b51-a9ae-f89d8ad0f33d" />


📘 Project Report (Summary)
🎯 Objective

To design a functional C2 detection testbed that simulates malicious beacon traffic and evaluates monitoring tools.

🧪 Methodology

Wrote Python agent & server for beacon communication

Configured Suricata IDS for network monitoring

Forwarded JSON logs into Elasticsearch

Designed Kibana dashboards for threat visualization

🛑 Results

Beacon traffic successfully detected

Suricata classified HTTP flows correctly

Elasticsearch stored structured logs

Dashboard created clear visibility into C2 behaviour

✅ Conclusion

C2Bench demonstrates how endpoint, network, and log-based monitoring collaborate in real-world security operations.
This project is suitable as a completed academic submission and a great addition to your cybersecurity portfolio.

🧑‍💻 Author
Rohan Sakhare
