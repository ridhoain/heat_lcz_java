# Canopy × LCZ × Heat Hazard — Java, Indonesia

Notebooks relating projected heat hazard (annual 95th-percentile daily Tmax, `Tmax_annual_p95`) to urban form (Local Climate Zones, LCZ) and tree canopy height across Java Island, plus a minimal Nature-based Solutions (NbS) canopy workflow for Bali.

## Notebooks
| Notebook | Purpose |
|---|---|
| `Java_Tmax95_LCZ_Canopy.ipynb` | Tmax95 hazard (baseline vs future) × LCZ × canopy on a 100 m grid |
| `Java_Tmax95_LCZ_Canopy_ERA5.ipynb` | Same, with ERA5-Land daily Tmax as baseline and CORDEX Tmax95 for baseline/future |
| `analysis_main.ipynb` | Monthly tas/tasmin/tasmax from SINGV-RCM (ACCESS-CM2) historical and SSP projections, ERA5-Land comparison |
| `Bali_NbS_Minimal.ipynb` | Canopy Height Map + WorldCover + LST → NbS score for Bali |
| `Untitled-1.ipynb` | Scratch: ERA5-Land monthly means download (CDS API) |
| `convert_tiff_to_nc.py` | GeoTIFF → NetCDF via `gdal_translate` |

`Java_Coastline/` holds the Java boundary shapefile used for clipping.

## Data (not in this repo)
Large inputs are git-ignored. Place them locally (paths are set in each notebook's config cell; some are absolute paths from the author's machine and need adjusting):
- **LCZ** — WUDAPT / LCZ-Global, 100 m (`LCZ_Subset_Java.tif`)
- **Canopy height** — Meta/WRI global canopy height map, ~1 m (`Canopy_Height_Java-*.tif`)
- **ERA5-Land** — Copernicus Climate Data Store (requires a CDS account and `~/.cdsapirc`)
- **Regional climate projections** — CORDEX-SEA SINGV-RCM driven by ACCESS-CM2 (historical, SSP scenarios), monthly tas/tasmin/tasmax

## Run
```bash
pip install -r requirements.txt
jupyter lab
```
GDAL is needed only for `convert_tiff_to_nc.py`.

## Reference
Hendrawan et al. (2024), *Future exposure of rainfall and temperature extremes to the most populous cities in Indonesia*, Int. J. Climatol.

*Work in progress; results have not been re-validated.*
