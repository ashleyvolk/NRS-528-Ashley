# Coding Challenge 10
# Our coding challenge this week that improves our practice with rasters from Week 10.
#
# Task 1 - Use what you have learned to process the Landsat files provided, this time, you know you are interested in
# the NVDI index which will use Bands 4 (red, aka vis) and 5 (near-infrared, aka nir) from the Landsat 8 imagery,
# see here for more info about the bands: https://www.usgs.gov/faqs/what-are-band-designations-landsat-satellites.
# Data provided are monthly (a couple are missing due to cloud coverage) during the year 2015 for the State of RI,
# and stored in the file Landsat_data_lfs.zip.
#
# Before you start, here is a suggested workflow:
#
# Extract the Landsat_data_lfs.zip file into a known location.
# For each month provided, you want to calculate the NVDI, using the equation: nvdi = (nir - vis) / (nir + vis)
# https://en.wikipedia.org/wiki/Normalized_difference_vegetation_index. Consider using the Raster Calculator Tool in
# ArcMap and using "Copy as Python Snippet" for the first calculation.
# The only rule is, you should run your script once, and generate the NVDI for ALL MONTHS provided. As part of your code

import arcpy
from arcpy.sa import *
import os

arcpy.env.overwriteOutput = True

arcpy.env.workspace = r"C:\NRS_528\Assignment\CodingChallenge10"
arcpy.env.workspace = r"C:\NRS_528\Assignment\CodingChallenge10\Landsat_data_lfs"


list_data = ["201502", "201504", "201505", "201507", "201510", "201511"] ## AD - I would search the directory for these subdirectories computationally.
print(list_data)

for date in list_data: ## AD - I would not use the word raster here, as it could confuse.

    arcpy.env.workspace = os.path.join(r"C:\NRS_528\Assignment\CodingChallenge10\Landsat_data_lfs", date)  ## AD - Need to set location for ListRasters to search

    B4 = arcpy.ListRasters("*B4*", "TIF")[0]
    B5 = arcpy.ListRasters("*B5*", "TIF")[0]

    outRaster = (Raster(B5) - Raster(B4)) / (Raster(B5) + Raster(B4))

    arcpy.env.workspace = os.path.join(r"C:\NRS_528\Assignment\CodingChallenge10\Landsat_data_lfs") # AD - switch back to other dir to save files
    outRaster.save("NVDI_" + date + ".tif")


