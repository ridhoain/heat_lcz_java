# Future Temperature Changes in Java's Peri-Urban Landscapes

Code behind the research poster *Future Temperature Changes in Java's Peri-Urban Landscapes* (YES Conference, Theme 3: Climate Action and Adaptation), Ainur Ridho, World Resources Institute Indonesia.

## Poster summary
Peri-urban areas in Java are highly vulnerable to rising temperatures but remain understudied. Using Local Climate Zones (LCZs), the study maps historical and projected daily mean surface air temperature (SAT) and extreme warm days (TG90p, days per year above the historical 90th percentile).

**Research questions**
1. How does temperature vary historically among LCZs?
2. How will near-future (2030–2050) and distant-future (2080–2100) temperatures shift?
3. How will the frequency of extremely warm days (TG90p) change in peri-urban LCZs?

**Poster data and method**
- LCZ map (~100 m), SRTM elevation (30 m), SA-OBS observations (~25 km, 1995–2014), SINGV-RCM driven by EC-Earth3 (~8 km; SSP1-2.6, SSP2-4.5, SSP5-8.5).
- Regrid everything to ~8 km; split LCZs into lowland (<300 m) and highland (>300 m); bias-correct with quantile mapping against observations and transfer the correction to the projections.
- Compute daily mean SAT per lowland LCZ, then TG90p for LCZ 6 (open lowrise) and LCZ 9 (sparsely built) lowland, the populated peri-urban classes.

**Key findings (from the poster)**
- Urban LCZs (28–30 °C) and industrial zones (28 °C) have the highest daily mean SAT; peri-urban and rural areas are ~27 °C.
- Warming reaches ~2 °C by 2080–2100, largest in lowland agricultural and peri-urban areas (Tangerang, Bekasi–Cirebon corridor, Blora–Bojonegoro, Parahyangan, Bromo–Semeru).
- TG90p in peri-urban lowland LCZs rises from ~30 days/year (near future) to ~90 days/year (distant future), with minor differences across SSPs.

> **Note on the code:** the notebooks in this repo are the working analysis and do not all match the poster's setup one-to-one. They use ERA5-Land and CORDEX-SEA SINGV-RCM driven by ACCESS-CM2 (not SA-OBS and EC-Earth3), and compute Tmax95 and canopy relationships rather than TG90p with quantile mapping. Treat the poster as the reference for the published results.

---

# Repository contents

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
