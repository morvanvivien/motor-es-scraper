"""Minimal example: run the motor-es-cars-scraper Actor and print the results.

Usage: APIFY_TOKEN=... python run.py   (pip install apify-client)
"""
import os
import sys

from apify_client import ApifyClient

token = os.environ.get("APIFY_TOKEN")
if not token:
    sys.exit("Set the APIFY_TOKEN environment variable first.")

client = ApifyClient(token)

run_input = {
    "startUrl": "https://www.motor.es/segunda-mano/renault/clio/",
    "maxItems": 50,
}

run = client.actor("bibian/motor-es-cars-scraper").call(run_input=run_input)

count = 0
for item in client.dataset(run.default_dataset_id).iterate_items():
    count += 1
    print(f"{item['title']} | {item.get('price')} {item.get('currency')} | {item.get('mileageKm')} km | {item.get('province')}")
print(f"{count} results")
