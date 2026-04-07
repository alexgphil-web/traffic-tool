import requests

API_KEY = '827299ced813f996dbc786238b43ebe2fa6d4c75'
DOMAIN = "examplelawyer.com"  # yahan apni website daalo

# Keywords with their monthly search volume
keywords = [
    {"keyword": "personal injury lawyer dallas", "volume": 12000},
    {"keyword": "divorce lawyer near me", "volume": 18000},
    {"keyword": "criminal defense attorney", "volume": 22000}
]

def get_keyword_position(keyword, domain):
    url = "https://api.serper.dev/search"
    headers = {"X-API-KEY": API_KEY}
    payload = {"q": keyword}

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    results = data.get("organic", [])
    for i, result in enumerate(results):
        link = result.get("link", "")
        if domain.lower() in link.lower():
            return i + 1
    return None  # Not in top results

def get_ctr(position):
    if position == 1:
        return 0.30
    elif position == 2:
        return 0.15
    elif position == 3:
        return 0.10
    elif position <= 5:
        return 0.05
    elif position <= 10:
        return 0.03
    else:
        return 0.01

def calculate_traffic(volume, position):
    ctr = get_ctr(position)
    return int(volume * ctr)

# Main flow
total_traffic = 0
for k in keywords:
    pos = get_keyword_position(k["keyword"], DOMAIN)
    if pos is None:
        pos = 10  # assume default if not in top 10
    traffic = calculate_traffic(k["volume"], pos)
    total_traffic += traffic
    print(f"{k['keyword']} → Position: {pos}, Traffic: {traffic}")

print(f"Total Estimated Traffic: {total_traffic}")
