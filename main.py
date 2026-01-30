from scrapers.github_scraper import fetch_github_advisories
from scrapers.reddit_scraper import fetch_reddit_posts
from scrapers.mastodon_scraper import fetch_mastodon_posts

from processor.relevance_filter import is_cyber_relevant
from processor.bert_classifier import classify_severity
from processor.cwe_mapper import infer_cwe

from storage.database import insert_vulnerability


def severity_to_cvss(sev):
    return {
        "CRITICAL": 9.5,
        "HIGH": 8.0,
        "MEDIUM": 5.0,
        "LOW": 3.0
    }.get(sev, 5.0)


#  GitHub 
for adv in fetch_github_advisories():
    summary = adv.get("summary", "")
    if is_cyber_relevant(summary):
        sev, _ = classify_severity(summary)
        cvss = severity_to_cvss(sev)
        cwe = infer_cwe(summary)
        insert_vulnerability(cvss, cwe, summary, "github")


#  Reddit 
for post in fetch_reddit_posts():
    if is_cyber_relevant(post):
        sev, _ = classify_severity(post)
        cvss = severity_to_cvss(sev)
        cwe = infer_cwe(post)
        insert_vulnerability(cvss, cwe, post, "reddit")


#  Mastodon 
for post in fetch_mastodon_posts():
    if is_cyber_relevant(post):
        sev, _ = classify_severity(post)
        cvss = severity_to_cvss(sev)
        cwe = infer_cwe(post)
        insert_vulnerability(cvss, cwe, post, "mastodon")
