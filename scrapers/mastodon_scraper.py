import requests
import re

def clean_html(text):
    return re.sub("<.*?>", "", text)

def fetch_mastodon_posts(limit=300):
    url = "https://infosec.exchange/api/v1/timelines/tag/cve"
    r = requests.get(url)
    if r.status_code != 200:
        return []

    posts = []
    for item in r.json():
        content = item.get("content", "")
        if content:
            posts.append(clean_html(content))
        if len(posts) >= limit:
            break

    return posts
