# Website Technology Detector

Give it a list of websites, your own or your prospects', and get one row per site with the technologies its homepage shows: CMS or website builder, ecommerce platform, analytics and ad pixels, tag managers, frameworks, CDN, hosting and web server. Every detection names its evidence and carries a confidence level, so you can check it and filter weak guesses out.

[![Run on Apify](https://img.shields.io/badge/Run%20on-Apify-97D700?logo=apify&logoColor=white)](https://apify.com/bardach_technologies/website-tech-detector)

**[Run on Apify: apify.com/bardach_technologies/website-tech-detector](https://apify.com/bardach_technologies/website-tech-detector)**

## Who it is for

- Sales prospecting by platform, for example all Shopify or WooCommerce stores in a list.
- Agency audits of what a client's or a prospect's site runs.
- Competitor research: analytics, tag managers and CDN of rival sites.
- Cleaning a CRM's "website platform" field.

Only the homepage is checked, from one response (headers, cookie names, script and link URLs, meta tags, markup). robots.txt is read first; sign-in, CAPTCHA and blocks are never bypassed. No page text, e-mail addresses, phone numbers or tracking IDs are kept. Technologies that appear only after JavaScript runs, or only on other pages, can be missed.

## Input

```json
{
  "websites": ["example.com", "https://www.example.com/about"],
  "minConfidence": "medium"
}
```

Up to 2,000 websites per run. See [examples/input.json](examples/input.json).

## Output

One row per site (an illustration, shortened):

```json
{
  "website": "https://example.com",
  "outcome": "detected",
  "billable": true,
  "cms": ["WordPress"],
  "ecommerce": ["WooCommerce"],
  "analytics": ["Google Analytics"],
  "tagManagers": ["Google Tag Manager"],
  "frameworks": [],
  "cdn": ["Cloudflare"],
  "webServers": [],
  "technologies": [
    {"name": "WordPress", "category": "CMS", "confidence": "high", "version": "6.4.2",
     "evidence": ["meta generator tag", "link URL from same site"]},
    {"name": "Cloudflare", "category": "CDN", "confidence": "high", "version": null,
     "evidence": ["response header cf-ray", "response header server"]}
  ],
  "technologyCount": 6,
  "httpStatus": 200,
  "robotsTxt": "allowed"
}
```

## Pricing

Pay per event: **USD 0.0015 per website with technologies detected** (USD 1.50 per 1,000), plus Apify's small actor-start event (USD 0.00005 per run). Refused, blocked, failed and empty sites are free, as are sites where only a generic web server header was found.

## Use it from your code

Install the official client and put your API token in the environment (never in the code):

```bash
pip install apify-client
export APIFY_TOKEN=<your Apify API token>
python examples/call_actor.py
```

```python
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("bardach_technologies/website-tech-detector").call(
    run_input={"websites": ["example.com"], "minConfidence": "medium"}
)
for row in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(row["website"], row.get("cms"), row.get("ecommerce"))
```

Full script: [examples/call_actor.py](examples/call_actor.py).

## License

MIT, see [LICENSE](LICENSE). The Actor itself runs on the Apify platform; this repository holds the documentation and usage examples.
