import requests

def fetch_github_advisories(pages=5, per_page=100):
    all_advisories = []
    base_url = "https://api.github.com/advisories"

    for page in range(1, pages + 1):
        params = {
            "per_page": per_page,
            "page": page
        }
        r = requests.get(base_url, params=params)
        if r.status_code != 200:
            break
        data = r.json()
        if not data:
            break
        all_advisories.extend(data)

    return all_advisories
