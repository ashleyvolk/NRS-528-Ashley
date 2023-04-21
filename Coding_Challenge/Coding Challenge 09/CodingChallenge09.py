# Coding Challenge 9
# In this coding challenge, your objective is to utilize the arcpy.da module to undertake some basic
# partitioning of your dataset. In this coding challenge, I want you to work with the Forest Health Works dataset
# from RI GIS (I have provided this as a downloadable ZIP file in this repository).
#
# Using the arcpy.da module (yes, there are other ways and better tools to do this), I want you to extract all sites that
# have a photo of the invasive species (Field: PHOTO) into a new Shapefile, and do some basic counts of the dataset.

# In summary, please addressing the following:
# Count how many individual records have photos, and how many do not (2 numbers), print the results.
# Count how many unique species there are in the dataset, print the result.
# Generate two shapefiles, one with photos and the other without.

import arcpy
arcpy.env.overwriteOutput = True
input_shp = r'C:\NRS_528\Assignment\CodingChallenge09\RI_Forest_Health_Works_Project%3A_Points_All_Invasives.shp'
fields = ['photo']

expression = arcpy.AddFieldDelimiters(input_shp, "photo") + " = 'y'"  # Cleaner and easier to code
photos = 0
with arcpy.da.SearchCursor(input_shp, fields, expression) as cursor:
    for row in cursor:
        photos = photos + 1
print("Printing Photos")
print(photos)

expression = arcpy.AddFieldDelimiters(input_shp, "photo") + " = ' '"  # Cleaner and easier to code
no_photos = 0
with arcpy.da.SearchCursor(input_shp, fields, expression) as cursor:
    for row in cursor:
        no_photos = no_photos + 1
print("Printing no Photos")
print(no_photos)

expression = arcpy.AddFieldDelimiters(input_shp, "Species") + " = ' '"  # Cleaner and easier to code
species = 0
with arcpy.da.SearchCursor(input_shp, fields, expression) as cursor:
    for row in cursor:
        species = species + 1
print("Printing species")
print(species)

# # Create an empty Shapefile
arcpy.env.workspace = r"C:\NRS_528\Assignment\CodingChallenge09"

# Set local variables
out_path = arcpy.env.workspace
out_name = "photos.shp"
geometry_type = "POINT"
template = "#"
has_m = "DISABLED"
has_z = "DISABLED"

# Use Describe to get a SpatialReference object
spatial_ref = 4326

# Execute CreateFeatureclass
arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type, template,
                                    has_m, has_z, spatial_ref)

arcpy.analysis.Select("RI_Forest_Health_Works_Project%3A_Points_All_Invasives.shp",
                      "with_Photos.shp", '"photo" = y')

# # Create an empty Shapefile
arcpy.env.workspace = r"C:\NRS_528\Assignment\CodingChallenge09"

# Set local variables
out_path = arcpy.env.workspace
out_name = "no_photos.shp"
geometry_type = "POINT"
template = "#"
has_m = "DISABLED"
has_z = "DISABLED"

# Use Describe to get a SpatialReference object
spatial_ref = 4326

# Execute CreateFeatureclass
arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type, template,
                                    has_m, has_z, spatial_ref)

arcpy.analysis.Select("RI_Forest_Health_Works_Project%3A_Points_All_Invasives.shp",
                      "no_Photos.shp", '"photo" = ')