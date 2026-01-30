import requests

def fetch_reddit_posts(limit=300):
    url = "https://www.reddit.com/r/netsec.json"
    headers = {"User-Agent": "academic-security-project"}

    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        return []

    posts = []
    for child in r.json()["data"]["children"]:
        title = child["data"].get("title")
        if title:
            posts.append(title)
        if len(posts) >= limit:
            break

    return posts
