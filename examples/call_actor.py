"""Run the Website Technology Detector Actor on Apify and print what each site runs.

Setup:
    pip install apify-client
    export APIFY_TOKEN=<your Apify API token>   # read from the environment, never hard-coded
    python call_actor.py
"""
import json
import os
from pathlib import Path

from apify_client import ApifyClient

ACTOR_ID = "bardach_technologies/website-tech-detector"


def main() -> None:
    token = os.environ.get("APIFY_TOKEN")
    if not token:
        raise SystemExit("Set the APIFY_TOKEN environment variable first.")

    run_input = json.loads((Path(__file__).parent / "input.json").read_text())

    client = ApifyClient(token)
    run = client.actor(ACTOR_ID).call(run_input=run_input)

    for row in client.dataset(run["defaultDatasetId"]).iterate_items():
        print(
            row["website"],
            row["outcome"],
            "cms=" + ",".join(row.get("cms", [])),
            "ecommerce=" + ",".join(row.get("ecommerce", [])),
            "analytics=" + ",".join(row.get("analytics", [])),
        )


if __name__ == "__main__":
    main()
