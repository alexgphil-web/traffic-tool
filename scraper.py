import requests
from bs4 import BeautifulSoup

def get_keywords(domain):
    try:
        url = f"https://{domain}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=5)

        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string if soup.title else ""
        meta = soup.find("meta", attrs={"name": "description"})
        description = meta["content"] if meta else ""

        words = (title + " " + description).split()

        keywords = list(set(words))[:10]

        return [{"keyword": k, "volume": 1000} for k in keywords]

    except:
        return []