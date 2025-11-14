# Fuzzy Engine - AI Coding Instructions

## Project Overview
Fuzzy Engine is a data analytics project exploring Etsy shop and listing data to identify trends in handmade crafts (crochet, knitting, macrame, jewelry, etc.). The project focuses on data collection, exploration, and visualization rather than production services.

## Architecture & Data Flow

### Directory Structure
```
fuzzy-engine/
  assets/          # Data exploration and API testing scripts
  data/            # CSV data files (source of truth for analysis)
  README.md        # Project description
```

### Key Data Asset
- **`data/etsy_shops_data.csv`** (20k+ rows): Contains Etsy shop metrics
  - Columns: `creation_date`, `listing_active_count`, `num_favorers`, `currency_code`, `is_shop_us_based`, `sale_message`, `sales_count`, `review_count`, `shop_location`
  - Data quality note: `-99` values indicate missing data (see `check_data.py`)
  - Used as primary data source for all analysis scripts

## Critical Developer Workflows

### Data Exploration Pattern
Use pandas + plotly for analysis:
```python
import pandas as pd
import plotly.express as px

df = pd.read_csv('fuzzy-engine/data/etsy_shops_data.csv')
## .github/copilot-instructions.md — Fuzzy Engine (concise)

Purpose: Help an AI coding assistant be immediately productive in this repository by describing the project shape, key files, conventions, and safe workflows.

1) Quick summary
- This is a data-analytics repository that explores an Etsy shops dataset (CSV-based). Primary work is exploratory analysis, cleaning, and visualization — not a production service.

2) Files and locations to know (examples)
- Project README: `fuzzy-engine/README.md` (business context, dataset description)
- Notebooks: `fuzzy-engine/assets/eda_analysis.ipynb` (main EDA work)
- Raw data: `fuzzy-engine/data/etsy_shops_data.csv`
- Cleaned data (convention): `fuzzy-engine/data/etsy_shops_data_cleaned.csv`

3) How to get started (developer workflow)
- Use Python 3.14 in a virtual environment (project commonly uses `.venv/` — do not commit it).
- Open the EDA notebook in VS Code or Jupyter: `fuzzy-engine/assets/eda_analysis.ipynb` for narrative analysis and plotting.
- For scripted transforms, read/write CSVs under `fuzzy-engine/data/` using relative paths so runs are portable.

4) Project-specific data conventions (important)
- Sentinel for missing numeric data: `-99` — always check and handle these before numeric ops.
- Many location fields are messy or NULL; prefer conservative country inference and document assumptions.
- Typical pattern: call `df.info()` and `df.describe()` early, then drop/replace `-99` and convert boolean-like columns to 0/1.

5) Typical code patterns and examples
- Preferred stack for analyses: pandas + NumPy + matplotlib/seaborn/plotly for visuals.
- Example read pattern:

  - Read: `df = pd.read_csv('fuzzy-engine/data/etsy_shops_data.csv')`
  - Inspect: `df.info()` / `df.isin([-99]).sum()`
  - Save cleaned: `df.to_csv('fuzzy-engine/data/etsy_shops_data_cleaned.csv', index=False)`

6) Integration & secrets
- The repo contains no committed API keys. If an API-test script exists locally, treat it as experimental. Never add keys to the repo; use environment variables or local config files listed in `.gitignore`.

7) Language, style, and file conventions
- File names: snake_case for scripts and clear descriptive names for outputs (use `_cleaned.csv` suffix for cleaned datasets).
- Comments may include Polish; preserve existing language in-place but prefer English for new public-facing docs.

8) When an AI agent should ask for human help
- If a change will alter the canonical dataset in `data/` (e.g., removing columns or re-encoding): ask for confirmation and document the transformation in `README.md` or a short `NOTES.md`.
- If work depends on an Etsy API key or other credential: request a secure way to test (developer-provided key via env only).

9) Helpful pointers to reference in PRs
- Link to the notebook(s) that demonstrate the workflow (`assets/eda_analysis.ipynb`).
- Include before/after dataset samples (small CSV diff) when changing cleaning logic.

If anything here is unclear or you want the instructions to emphasize a different workflow (e.g., adding tests or CI), tell me which parts to expand and I will iterate.
