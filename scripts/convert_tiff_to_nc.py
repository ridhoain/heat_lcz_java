import subprocess

# Convert the LCZ GeoTIFF to NetCDF (requires GDAL). Run from the repo root.
subprocess.run([
    "gdal_translate",
    "-of", "NetCDF",
    "data/LCZ_Subset_Java.tif",
    "data/LCZ_Subset_Java.nc",
], check=True)
