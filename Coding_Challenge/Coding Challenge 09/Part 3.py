import arcpy
arcpy.env.overwriteOutput = True

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
                      "with_Photos.shp", 'photo = 'y')

# # # Create an empty Shapefile
# arcpy.env.workspace = r"C:\NRS_528\Assignment\CodingChallenge09"
#
# # Set local variables
# out_path = arcpy.env.workspace
# out_name = "no_photos.shp"
# geometry_type = "POINT"
# template = "#"
# has_m = "DISABLED"
# has_z = "DISABLED"
#
# # Use Describe to get a SpatialReference object
# spatial_ref = 4326
#
# # Execute CreateFeatureclass
# arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type, template,
#                                     has_m, has_z, spatial_ref)

arcpy.analysis.Select("RI_Forest_Health_Works_Project%3A_Points_All_Invasives.shp",
                      "no_Photos.shp", '"photo" = ')