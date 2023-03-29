# Coding Challenge 5:
# Link to the data is located on GitHub: https://github.com/ashleyvolk/NRS-528-Ashley/tree/main/Data/Coding%20Challenge%2005
# For this coding challenge, I want you to practice the heatmap generation that we went through in class,
# but this time obtain your own input data, and I want you to generate heatmaps for **TWO** species.

# You can obtain species data from a vast array of different sources, for example:
# [obis](https://www.obis.org) - Note: You should delete many columns (keep species name, lat/lon)
# as OBIS adds some really long strings that don't fit the Shapefile specification.

# [GBIF](https://www.gbif.org)
# [Maybe something on RI GIS](http://www.rigis.org)
# Or just *Google* species distribution data

# My requirements are:
# 1. The two input species data must be in a **SINGLE** CSV file, you must process the input data to separate
# out the species (Hint: You can a slightly edited version of our CSV code from a previous session to do this),
# I recommend downloading the species data from the same source so the columns match.
# 2. Only a single line of code needs to be altered (workspace environment) to ensure code runs on my computer,
# and you provide the species data along with your Python code.
# 3. The heatmaps are set to the right size and extent for your species input data, i.e. appropriate fishnet cellSize.
# 4. You leave no trace of execution, except the resulting heatmap files.
# 5. You provide print statements that explain what the code is doing, e.g. Fishnet file generated.
# Import the two packages to help analyze the data

import csv
import arcpy

# Import the csv and read the file
# Create the species list to allow for further analysis of the csv file
# You must change the arcpy.env.workspace on your computer to where you are storing the csv file before running
arcpy.env.workspace = r"C:\NRS_528\Assignment\CodingChallenge05"
arcpy.env.overwriteOutput = True
with open('species_list.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)
    species_list = []
    for row in csv_reader:
        if row[0] not in species_list:
            species_list.append(row[0])

print(species_list)

# Create two csv files with the two different species
# Split the csv file into the two species and create a new line in the csv
for species in species_list:
    print(species)
    file_name = species + ".csv"
    print(species + ".csv")
    file = open(file_name, "w")
    file.write(",".join(header))
    file.write("\n")

    with open('species_list.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        species_list = []
        for row in csv_reader:
            if species == row[0]:
                print(species)
                file.write(",".join(row))
                file.write("\n")

# Create a shp file for the two different species csv files
    in_Table = species + ".csv"
    x_coords = "Long"
    y_coords = "Lat"
    z_coords = ""
    out_Layer = species
    saved_Layer = species + "output.shp"

# Set the spatial reference in this case the spatial reference is WGS 1984
    spRef = arcpy.SpatialReference(4326)  # 4326 == WGS 1984
    lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)

# Count the number of each file and print it
    print(arcpy.GetCount_management(out_Layer))

# Save to a layer file
    arcpy.CopyFeatures_management(lyr, saved_Layer)
    if arcpy.Exists(saved_Layer):
        print("Created file successfully!")

# Describe the extent of the files
    desc = arcpy.Describe(saved_Layer)
    XMin = desc.extent.XMin
    XMax = desc.extent.XMax
    YMin = desc.extent.YMin
    YMax = desc.extent.YMax

# Set the spatial reference of the data (WGS 1984)
    arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)

# Create a fishnet shp file for the two different files
    outFeatureClass = species + "fishnet.shp"

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
    out_feature_class = species + "heatmap.shp"
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
        print("Deleting intermediate files")
        arcpy.Delete_management(target_features)
        arcpy.Delete_management(join_features)