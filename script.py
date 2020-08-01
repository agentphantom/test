import csv
import os
from datetime import datetime

import requests


headers = {"User-Agent": "Reddit r/all Downloader v1.0"}
url = "https://www.reddit.com/r/all.json?limit=100"

now = "{:%Y-%m-%d %H-%M-%S}".format(datetime.utcnow())
data_list = [["id", "subreddit", "author", "score", "title", "domain",  "url", "created_utc"]]

os.makedirs("./data", exist_ok=True)

with requests.get(url, headers=headers) as response:

    data = response.json()["data"]["children"]

    for item in data:

        item_data = item["data"]
        data_list.append([
            item_data["id"],
            item_data["subreddit"],
            item_data["author"],
            item_data["score"],
            item_data["title"],
            item_data["domain"],
            item_data["url"],
            datetime.fromtimestamp(item_data["created_utc"])
        ])


with open(f"./data/{now}.csv", "w", encoding="utf-8", newline="") as csv_file:
    csv.writer(csv_file).writerows(data_list)
