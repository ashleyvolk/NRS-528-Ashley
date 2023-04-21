# Coding Challenge 7.py
# Our coding challenge this week should make use of temporary folders, output folders and file management.
#
# Convert your Coding Challenge 5.py exercise to work with temporary folders, os.path.join and glob.glob.
# Do not take too much time on this and if you do not have a working Challenge 5.py, talk to the instructor.

import os
import arcpy
import glob
import csv

input_directory = r"C:\NRS_528\Assignment\CodingChallenge05"
data_file = "species_list.csv"

keep_temp_files = False
#
# # In this example,. I show you how to use os.path.join to create directory names, which can be used to
# # test if the directory exists, and if not, create it.
#
if not os.path.exists(os.path.join(input_directory, "temporary_files")):
    os.mkdir(os.path.join(input_directory, "temporary_files"))
if not os.path.exists(os.path.join(input_directory, "outputs")):
    os.mkdir(os.path.join(input_directory, "outputs"))

# Step 1: Lets determine our species

species_list = []
with open(os.path.join(input_directory, data_file)) as species_csv:
    header_line = next(species_csv)
    for row in csv.reader(species_csv):
        try: #Using try/except saves us if there is a line with no data in the file
            if row[0] not in species_list:
                species_list.append(row[0])
        except:
            pass

print("..There are: " + str(len(species_list)) + " species to process..")

# Step 2: Lets split the files
if len(species_list) > 1:
    for s in species_list:
        s_count = 1
        with open(os.path.join(input_directory, data_file)) as species_csv:
            for row in csv.reader(species_csv):
                if row[0] == s:
                    if s_count == 1:
                        file = open(os.path.join(input_directory, "temporary_files", str(s.replace(" ", "_")) + ".csv"), "w")
                        file.write(header_line)
                        s_count = 0
                    #make well formatted line
                    file.write(",".join(row))
                    file.write("\n")
        file.close()


# Step 3: Convert those files into Shapefiles
os.chdir(os.path.join(input_directory, "temporary_files"))# same as env.workspace
species_file_list = glob.glob("*.csv") # Find all CSV files

count = 0

for species_file in species_file_list:
    print(".. Processing: " + str(species_file) + " by converting to shapefile format")

    arcpy.env.workspace = os.path.join(input_directory, "temporary_files")

    in_Table = species_file
    x_coords = "Long"
    y_coords = "Lat"
    z_coords = ""
    out_Layer = "species" + str(count)
    saved_Layer = species_file.replace(".","_") + ".shp"

    # Set the spatial reference
    spRef = arcpy.SpatialReference(4326)  # 4326 == WGS 1984

    lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)
    arcpy.CopyFeatures_management(lyr, saved_Layer)
    count = count + 1
    arcpy.Delete_management(lyr)

    # Describe the extent of the files
    desc = arcpy.Describe(saved_Layer)
    XMin = desc.extent.XMin
    XMax = desc.extent.XMax
    YMin = desc.extent.YMin
    YMax = desc.extent.YMax

    # Set the spatial reference of the data (WGS 1984)
    arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)

    # Create a fishnet shp file for the two different files
    outFeatureClass = species_file.replace(".","_") + "_fishnet.shp"

    # Set the origin of the fishnet
    # Create a variable to change the cell size to make it dynamic (this can be changed based on user need)
    if XMax < 0:
        XMax_Val = XMax * -1
    else:
        XMax_Val = XMax
    if XMin < 0:
        XMin_Val = XMin * -1
    else:
        XMin_Val = XMin

    originCoordinate = str(XMin) + " " + str(YMin)
    yAxisCoordinate = str(XMin) + " " + str(YMin + 1)
    cellSizeWidth = (XMax_Val + XMin_Val)/50
    print(cellSizeWidth)
    cellSizeHeight = (XMax_Val + XMin_Val)/50
    numRows = ""
    numColumns = ""
    oppositeCorner = str(XMax) + " " + str(YMax)
    labels = "NO_LABELS"
    templateExtent = "#"
    geometryType = "POLYGON"

    arcpy.CreateFishnet_management(outFeatureClass, originCoordinate, yAxisCoordinate,
                                   cellSizeWidth, cellSizeHeight, numRows, numColumns,
                                   oppositeCorner, labels, templateExtent, geometryType)

    if arcpy.Exists(outFeatureClass):
        print("Created Fishnet file successfully!")


    # Join the two species using spatial join to create the heatmap
    # Heatmap will be the last output
    target_features = outFeatureClass
    join_features = saved_Layer
    out_feature_class = os.path.join(input_directory, "outputs",species_file.replace(".","_") + "_heatmap.shp")
    join_operation = "JOIN_ONE_TO_ONE"
    join_type = "KEEP_ALL"
    field_mapping = ""
    match_option = "INTERSECT"
    search_radius = ""
    distance_field_name = ""

    arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,
                               join_operation, join_type, field_mapping, match_option,
                               search_radius, distance_field_name)

    # Delete the files other than the Heatmap so that the output is cleaner
    if arcpy.Exists(out_feature_class):
        print("Created Heatmap file successfully!")

if keep_temp_files == False:
    print("Deleting intermediate files")
    arcpy.Delete_management(os.path.join(input_directory, "temporary_files"))