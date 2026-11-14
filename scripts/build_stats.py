#!/usr/bin/env python3
"""Collects profile stats from the GitHub API into assets/stats.json.

Needs a token in GITHUB_TOKEN (the Actions token is enough):
    GITHUB_TOKEN=$(gh auth token) python3 scripts/build_stats.py
"""

import json
import os
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

USER = "kasevvlad"
OUT = Path(__file__).resolve().parent.parent / "assets" / "stats.json"
TOKEN = os.environ.get("GITHUB_TOKEN", "")


def request(path, body=None):
    req = urllib.request.Request(
        "https://api.github.com" + path,
        data=json.dumps(body).encode() if body else None,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {TOKEN}",
            "User-Agent": "profile-stats",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def main():
    if not TOKEN:
        raise SystemExit("GITHUB_TOKEN is not set")

    repos = [
        r for r in request(f"/users/{USER}/repos?per_page=100&type=owner")
        if not r["fork"] and not r["private"] and r["name"] != USER
    ]

    downloads, releases = {}, 0
    for repo in repos:
        items = request(f"/repos/{USER}/{repo['name']}/releases?per_page=100")
        if items:
            releases += len(items)
            downloads[repo["name"]] = sum(a["download_count"] for r in items for a in r["assets"])

    query = """query($login: String!) {
      user(login: $login) {
        followers { totalCount }
        contributionsCollection { contributionCalendar { totalContributions } }
      }
    }"""
    user = request("/graphql", {"query": query, "variables": {"login": USER}})["data"]["user"]

    stats = {
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "projects": len(repos),
        "releases": releases,
        "downloads": downloads,
        "total_downloads": sum(downloads.values()),
        "contributions": user["contributionsCollection"]["contributionCalendar"]["totalContributions"],
        "stars": sum(r["stargazers_count"] for r in repos),
        "followers": user["followers"]["totalCount"],
    }
    try:
        previous = json.loads(OUT.read_text())
    except (FileNotFoundError, ValueError):
        previous = {}
    if {**previous, "updated": stats["updated"]} == stats:
        print("No changes")
        return
    OUT.write_text(json.dumps(stats, indent=2) + "\n")
    print(json.dumps(stats))


if __name__ == "__main__":
    main()
