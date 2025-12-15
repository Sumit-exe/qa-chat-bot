import requests
from bs4 import BeautifulSoup

def crawl_with_requests(url: str):
    try:
        resp = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        if resp.status_code != 200:
            return []


        soup = BeautifulSoup(resp.text, "html.parser")
        text = soup.get_text(separator=" ", strip=True)
        return [text]
    except Exception:
        return []