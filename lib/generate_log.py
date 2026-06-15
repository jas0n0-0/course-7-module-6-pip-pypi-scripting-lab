import argparse
from datetime import datetime
import os

import requests


def generate_log(data):
    if not isinstance(data, list):
        raise ValueError("Input data must be a list.")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        for entry in data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename


def fetch_data(url=None):
    url = url or "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    payload = response.json()

    title = payload.get("title", "No title").strip()
    body = payload.get("body", "").strip()

    return [
        f"Fetched title: {title}",
        f"Fetched body: {body}",
        f"Source URL: {url}",
        f"Retrieved at: {datetime.now().isoformat()}"
    ]


def main():
    parser = argparse.ArgumentParser(
        description="Generate a dated log file from external data."
    )
    parser.add_argument(
        "--url",
        help="Data source URL to fetch JSON from",
        default="https://jsonplaceholder.typicode.com/posts/1",
    )
    args = parser.parse_args()

    log_entries = fetch_data(args.url)
    filename = generate_log(log_entries)
    print(f"Generated log file: {filename}")


if __name__ == "__main__":
    main()
