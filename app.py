from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
API_KEY = '827299ced813f996dbc786238b43ebe2fa6d4c75'

def get_position(keyword, domain):
    url = "https://api.serper.dev/search"
    headers = {"X-API-KEY": API_KEY}
    payload = {"q": keyword}
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    results = data.get("organic", [])
    for i, r in enumerate(results):
        if domain.lower() in r.get("link", "").lower():
            return i + 1
    return None

def get_ctr(pos):
    if pos == 1: return 0.3
    elif pos == 2: return 0.15
    elif pos == 3: return 0.10
    elif pos <=5: return 0.05
    elif pos <=10: return 0.03
    else: return 0.01

@app.route("/traffic", methods=["POST"])
def traffic():
    data = request.json
    domain = data.get('domain')
    keywords = data.get('keywords', [])
    results = []
    for k in keywords:
        pos = get_position(k, domain)
        if pos is None: pos = 10
        traffic = int(get_ctr(pos) * 1000)  # Replace 1000 with real monthly search volume if you have
        results.append({"keyword": k, "position": pos, "traffic": traffic})
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)