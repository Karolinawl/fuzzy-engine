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
# Analysis and visualization follow
```

### External API Integration (Etsy API v3)
- **File**: `assets/etsy_api_test.py`
- **Endpoint**: `https://openapi.etsy.com/v3/application/listings/active`
- **Auth**: `x-api-key` header (client_key stored locally, never commit)
- **Parameters**: Support `keywords`, `limit` for filtering
- **Status**: Experimental - for testing API connectivity only

### Python Environment
- Uses `.venv/` virtual environment (in .gitignore)
- No requirements.txt yet - infer dependencies from imports: pandas, requests, numpy, plotly
- Dependencies are installed in `.venv/` but not tracked in repo

## Project-Specific Patterns & Conventions

### File Naming
- Snake_case for Python scripts (`check_data.py`, `etsy_api_test.py`)
- All paths relative to project root (e.g., `fuzzy-engine/data/`)

### Data Handling Conventions
- Always check for `-99` sentinel values indicating missing data in numeric columns
- Handle `None` values in location fields gracefully (many shops have `None` for `shop_location`)
- Use pandas `.info()` to inspect data structure before analysis

### Polish/English Mix
- Code contains Polish characters and comments (e.g., "Wiersze", "Kolumny")
- Maintain this style when adding to existing files, but prioritize English in new documentation

## Integration Points & External Dependencies

### Etsy API v3
- **Purpose**: Real-time listing/shop data collection
- **Status**: Requires valid API key (not included in repo)
- **Usage**: Reference `etsy_api_test.py` for request structure
- **Limitation**: Currently experimental, not integrated into main analysis workflow

### Data Source
- CSV files are primary data (no database)
- All new data analyses should source from `data/` directory
- No streaming or real-time requirements

## AI Agent Guidelines

1. **Before modifying data handling**: Check `check_data.py` to understand existing data inspection patterns
2. **API changes**: If updating Etsy API calls, test with `etsy_api_test.py` first
3. **New analysis scripts**: Follow the pandas/plotly pattern in existing assets
4. **Path handling**: Use relative paths from project root (`fuzzy-engine/data/...`) for portability across platforms
5. **Never commit**: API keys, credentials, or the `.venv/` directory
6. **Data validation**: Always call `df.info()` and check for `-99` and `None` values when starting new analysis
