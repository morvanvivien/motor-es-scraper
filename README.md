# How to Scrape Motor.es: Used Car Prices, Discounts and Financed Price Data (Spain)

> **Run it now, no code: [motor-es-cars-scraper on the Apify Store](https://apify.com/bibian/motor-es-cars-scraper)** &nbsp;|&nbsp; $2.00 per 1,000 car listings &nbsp;|&nbsp; no browser, no proxy

Motor.es is a major Spanish car portal with over 40,000 used car ads. It has no public export and no official API for third parties. This guide shows how to get the ads as clean structured data: brand, model, price before and after discount, financed price, year, mileage, fuel and province, with a free Apify Actor, from the console or from code.

Searches this page answers: motor.es scraper, spanish used car data, coches de segunda mano scraper, used car price scraper spain.

## What you get from the Motor.es scraper

- Every used car ad with brand, model, version, cash price and the seller's financed price.
- `priceBeforeDiscount`, so you can see exactly when and how much a seller lowered a price.
- Year, registration month, mileage, fuel and power in horsepower.
- Province and city of the seller, plus the publication date.

Export the dataset as JSON, CSV or Excel, or read it through the Apify API. A real sample (five results) is in [`sample-output.json`](sample-output.json).

## Output fields

| Field | What it is |
|---|---|
| `id`, `url` | Motor.es ad id and public link |
| `title`, `brand`, `model`, `version` | Car name as displayed |
| `price`, `priceBeforeDiscount`, `financedPrice`, `currency` | Cash price, previous price when discounted, and the seller's financed price |
| `year`, `registrationMonth`, `mileageKm` | Age and mileage |
| `fuel`, `powerHp`, `ecoLabel` | Technical specs and Spain's environmental badge when shown |
| `province`, `city` | Location of the seller |
| `publishedAt` | When the ad was last published |
| `imageCount`, `imageUrl` | Number of photos and the first photo |

## Use cases

- **Price used cars.** Compare cash price, discount and financed price by brand, model, year, mileage and province.
- **Spot price drops.** `priceBeforeDiscount` tells you exactly when and how much a seller cut the price.
- **Follow new ads.** `publishedAt` lets a daily run surface only what changed since yesterday.
- **Feed a market study.** Track fuel mix, power and price levels across Spain's regions.

## Input

| Field | What it does |
|---|---|
| `startUrl` | Open Motor.es used cars, pick a brand, model, province or body type, then paste the page URL, for example `https://www.motor.es/segunda-mano/renault/clio/madrid/`. Empty means all used cars. |
| `maxItems` | The run stops once this many listings are saved (default 50). |

Example input:

```json
{
  "startUrl": "https://www.motor.es/segunda-mano/renault/clio/",
  "maxItems": 50
}
```

## Three ways to use it

### 1. Apify console, no code

1. Open [the Actor page](https://apify.com/bibian/motor-es-cars-scraper) and click **Try for free** (a free Apify account is enough).
2. Paste a listing URL (or leave it empty for all used cars) and the maximum number of results, then click **Start**.
3. When the run finishes, open the **Output** tab, check the table, then **Export** as CSV, Excel or JSON.
4. For daily price tracking, open **Schedules**, create a daily schedule and, optionally, add an integration that sends new results to Slack, e-mail or Google Sheets.

### 2. Apify API with JavaScript

```bash
npm install apify-client
export APIFY_TOKEN="your token from Apify console, Settings, Integrations"
node examples/run.js
```

```js
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const run = await client.actor('bibian/motor-es-cars-scraper').call({
    "startUrl": "https://www.motor.es/segunda-mano/renault/clio/",
    "maxItems": 50
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const item of items) {
    console.log(`${item.title} | ${item.price} ${item.currency} | ${item.mileageKm} km | ${item.province}`);
}
```

The complete file is [`examples/run.js`](examples/run.js) (ES module, Node 18 or later).

### 3. Apify API with Python

```bash
pip install apify-client
export APIFY_TOKEN="your token from Apify console, Settings, Integrations"
python examples/run.py
```

```python
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("bibian/motor-es-cars-scraper").call(run_input={
    "startUrl": "https://www.motor.es/segunda-mano/renault/clio/",
    "maxItems": 50,
})

for item in client.dataset(run.default_dataset_id).iterate_items():
    print(f"{item['title']} | {item.get('price')} {item.get('currency')} | {item.get('mileageKm')} km | {item.get('province')}")
```

The complete file is [`examples/run.py`](examples/run.py). Never put your token in the code: read it from the `APIFY_TOKEN` environment variable as above.

## Why this one

- **No browser, no proxy.** The ad data is read directly, so runs are fast and cheap, and there is no CAPTCHA risk to manage.
- **Discount history in one field.** `priceBeforeDiscount` makes price-drop tracking a single comparison instead of scraping the ad twice.
- **Seller privacy respected.** Only province and city are kept; seller names and phone numbers are never exported, and the ad page itself is not opened, per Motor.es's robots.txt.

## Pricing

Pay per result: **$2.00 per 1,000 car listings** (that is $0.002 per listing), plus a tiny start fee of $0.00005 per run. You pay only for the results saved to the dataset. Apify's free plan includes monthly credits, enough to try it on a few hundred results. Prices are those shown on the [Store page](https://apify.com/bibian/motor-es-cars-scraper) when this guide was written; the Store page is the reference.

## Limits and honest notes

- The ad pages themselves are not opened (Motor.es's robots.txt asks crawlers not to); the `url` field links to them for your own use.
- `price` is the cash price; `financedPrice` is the price with the seller's financing, when offered.
- Fields such as `registrationMonth` or `ecoLabel` are empty when the seller did not provide them.
- This is an unofficial tool, not affiliated with Motor.es. Check the site terms and the data protection rules that apply to your use.

## FAQ

**Does it need a browser or a proxy?**
No. The Actor reads the listing data directly, so runs are fast and cheap.

**How do I track price drops?**
Compare `price` for the same `id` across scheduled runs, or just read `priceBeforeDiscount` on the current ad.

**Can I scrape a specific brand, model or province only?**
Yes, build the `startUrl` from Motor.es's own filters, for example `/segunda-mano/kia/sportage/barcelona/`.

**Can I get the data in Excel or Google Sheets?**
Yes. Export the dataset as CSV, Excel or JSON from the Apify console, or connect the Apify Google Sheets integration.

## Try it

**[Open motor-es-cars-scraper on the Apify Store](https://apify.com/bibian/motor-es-cars-scraper)**

The code in `examples/` is released under the MIT license (see [LICENSE](LICENSE)). The data belongs to its original publishers.
