# DVN36104 — Session 2 apps

Three coursework apps prepared with substantial AI assistance, disclosed in AI_DECLARATION.md. No Canvas submission is performed by this repository.

| App | Streamlit entrypoint | Live app |
|---|---|---|
| Uber pickups | `uber_pickups/app.py` | https://yajat-dvn-uber-pickups.streamlit.app/ |
| Star explorer | `star_explorer/app.py` | https://yajat-dvn-star-explorer.streamlit.app/ |
| Multipage tutorial | `multipage_demo/app.py` | https://yajat-dvn-multipage.streamlit.app/ |

Use Python 3.11 and the pinned root requirements. Each folder can also run independently. Example: `streamlit run star_explorer/app.py` from the repository root.

## Attribution and data

The pickups and multipage apps adapt the official Streamlit tutorials:
- https://docs.streamlit.io/get-started/tutorials/create-an-app
- https://docs.streamlit.io/get-started/tutorials/create-a-multipage-app

The star app adapts the supplied teaching model from https://dvn36104.github.io/session2/part-d.html. The unchanged original is retained as star_explorer/starter_reference.py. Model thresholds are simplified classroom rules, not precise stellar predictions.

The pickup CSV contains the tutorial's first 10,000 records from the public September 2014 file. The multipage JSON files come from Streamlit's public example-data repository; the agricultural data come from the historical Streamlit tutorial snapshot. App footnotes link the sources. Map tiles require internet. No private Canvas pages, personal credentials, or Part C submission files are included.

The three Streamlit Community Cloud apps use the entrypoints above with Python 3.11. They were checked publicly on 26 September 2026. Community Cloud apps sleep after inactivity; click the wake button if prompted.
