# Canopy × LCZ × Heat Hazard — Java, Indonesia

## Question
How does projected extreme heat (annual 95th-percentile daily maximum temperature, `Tmax_annual_p95`) vary across Java's urban form (Local Climate Zones, LCZ) and tree canopy, and how much can canopy cover offset urban heat?

## Data
Raw data is **not** in this repo (too large). Put it in a local `data/` folder; paths are set in each notebook's config cell.

| Dataset | Source |
|---|---|
| LCZ map, 100 m | WUDAPT / LCZ-Global |
| Canopy height, ~1 m | Meta / WRI global canopy height map |
| ERA5-Land (2 m temperature, daily/monthly) | Copernicus Climate Data Store (needs a CDS account) |
| Regional climate model | CORDEX-SEA, SINGV-RCM driven by ACCESS-CM2: historical, SSP1-2.6, SSP2-4.5, SSP5-8.5 (monthly tas, tasmin, tasmax) |
| Java boundary | `Java_Coastline/` (included) |

## Method
1. Align LCZ, canopy and climate layers to a common 100 m grid over Java.
2. Derive built-up LCZ classes and canopy fraction per cell.
3. Compute an LCZ thermal modifier from surface-temperature contrasts and add it to the coarse Tmax95 hazard (baseline vs future) to get a 100 m field.
4. Summarise per LCZ class, and regress Tmax95 on canopy fraction (overall and per LCZ).

## Notebooks (run in order)
| # | Notebook | Purpose |
|---|---|---|
| 01 | `notebooks/01_download_era5land_inspect_cordex.ipynb` | Download ERA5-Land via CDS API; inspect CORDEX files |
| 02 | `notebooks/02_cordex_lcz_urban_natural_contrast.ipynb` | Historical and SSP projections; urban vs natural temperature contrast by LCZ group |
| 03 | `notebooks/03_tmax95_lcz_canopy.ipynb` | Tmax95 × LCZ × canopy at 100 m |
| 04 | `notebooks/04_tmax95_lcz_canopy_era5_cordex.ipynb` | Same, with ERA5-Land baseline and CORDEX Tmax95 |

`extras/bali_nbs_minimal.ipynb` is a side workflow (Nature-based Solutions score for Bali). `scripts/convert_tiff_to_nc.py` converts the LCZ GeoTIFF to NetCDF (needs GDAL).

## Key findings
Not yet written up: the committed notebooks have no saved outputs. Add 2–3 numbers (per-LCZ Tmax95 change, canopy slope) after re-running.

## How to run
```bash
pip install -r requirements.txt
# put the datasets above in ./data, then
jupyter lab notebooks/
```

## Reference
Hendrawan et al. (2024), *Future exposure of rainfall and temperature extremes to the most populous cities in Indonesia*, Int. J. Climatol.
