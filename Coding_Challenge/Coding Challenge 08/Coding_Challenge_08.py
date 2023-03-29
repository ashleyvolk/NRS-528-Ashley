# Coding Challenge 8
# Our coding challenge this week follows from the last exercise that we did in class during
# Week 8 where we worked with functions.
#
# Convert some of your earlier code into a function. The only rules are:
# 1) You must do more than one thing to your input to the function, and
# 2) the function must take two arguments or more.
# 3) provide a zip file of example data within your repo.

# Plan the task to take an hour or two, so use one of the simpler examples from our past classes.

# Import arcpy to allow for tools from GIS to be present
import arcpy
from arcpy import env

# Describe the shapefile inputs and outputs
def describe_shp(input_shapefile):
    desc = arcpy.Describe(input_shapefile)
    print("Describing: " + str(input_shapefile))
    if arcpy.Exists(input_shapefile):
        if desc.dataType == "ShapeFile":
            # describe the type of shapefile (point, line, or polygon)
            print("Feature Type:  " + desc.shapeType)
            # describe the spatial reference type (geographic or projected)
            print("Coordinate System Type:  " + desc.spatialReference.type)
            # describe the spatial reference (whatever you want to project in)
            print("Coordinate System used:  " + desc.spatialReference.GCSName)

# Make sure you work in these if else tools incase the dataset is not found
        else:
            print("Input data not ShapeFile..")
    else:
        print("Dataset not found, please check the file path..")

# Add in the data you need
# Add where the data is coming from
env.workspace = r"C:\NRS_528\Assignment\CodingChallenge08"

# Add in which feature you want to pull data from
in_features = r"C:\NRS_528\Assignment\CodingChallenge08\Municipalities_(1997).shp"

# Add a name from the output created by the model
out_feature_class = r"C:\NRS_528\Assignment\CodingChallenge08\Washington_County.shp"

# For the select tool you have to add in another parameter to select the data
# For this attempt I chose to select from the towns layer areas that were equal to Washington county
where_clause = "COUNTY = 'WASHINGTON'"

# This is the select tool that will allow the code to run
arcpy.analysis.Select(in_features, out_feature_class, where_clause)

# Set workspace
arcpy.env.workspace = "C:/data"

# Set local variables
in_features = "E911_Sites.shp"
clip_features = "Washington_County.shp"
out_feature_class = r"C:\NRS_528\Assignment\CodingChallenge08\Buildings_Washington.shp"

# Run Clip
arcpy.analysis.Clip(in_features, clip_features, out_feature_class)


input_shapefile = r"C:\NRS_528\Assignment\CodingChallenge08\Washington_County.shp"
describe_shp(input_shapefile)

describe_shp(r"C:\NRS_528\Assignment\CodingChallenge08\E911_Sites.shp")

# print that the code is finished
def word_mixer(first_word, second_word, third_word, fourth_word):
    output = first_word + " " + second_word + " " + third_word + " " + fourth_word
    print(output)
    return

word_mixer(first_word="The", third_word="code", second_word="is", fourth_word="finished")


