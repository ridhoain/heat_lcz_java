import subprocess
subprocess.run([
    "gdal_translate",
    "-of", "NetCDF",
    "/Users/ridhoain/Canopy LCZ Project/LCZ_Subset_Java.tif"
    "/Users/ridhoain/Canopy LCZ Project/LCZ_Subset_Java.nc"
])
