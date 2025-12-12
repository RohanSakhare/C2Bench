from flask import Flask, request, jsonify
import base64
app = Flask(__name__)
COMMANDS = {'agent-1': ['echo:hello', 'sleep:5']}
@app.route('/beacon', methods=['POST'])
def beacon():
    data = request.json or {}
    agent_id = data.get('agent_id', 'unknown')
    cmd = COMMANDS.get(agent_id, [])
    payload = ''
    if cmd:
        payload = cmd.pop(0)
    encoded = base64.b64encode(payload.encode()).decode()
    return jsonify({'commands': encoded}), 200
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

