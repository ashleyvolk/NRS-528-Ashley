# Midterm Tool Challenge (due Friday 19th March 17.30pm)
# In this assignment, you are instructed to produce a small script tool that takes advantage of arcpy and Python.
# You will need to provide example data, and the code should run on all PC's. The tool needs to manipulate a dataset
# across three different processes, for example, extracting, modifying and exporting data. The exact workflow is
# entirely up to yourself. You are expected to take 3-4 hours on this coding assignment, and you should deposit your
# code and example files within a Github repository for feedback and grading.
#
# The criteria are:
# Cleanliness of code (10 points)
# Functionality (10 points)
# Appropriate use of documentation (10 points)
# Depth of processing operation (10 points)
# In addition, you must provide example data and minimize the amount of editing a user must make in order for the program to run (10 points).

# In this coding challenge I will be using the select tool to select the westerly towns layer for further analysis.
# Once this is selected I will then import the fire hydrants .csv file so that I can see the fire hydrants and then clip
# them to the westerly layer that I created. Following this I will get the count of the hydrants found in the westerly area.
# Import packages for data analysis
import arcpy
import csv
import os
import glob
arcpy.env.overwriteOutput = True


data_file = "Municipalities__1989_.shp"
input_directory = r"C:\NRS_528\Assignment\MidtermCodingChallenge"

if not os.path.exists(os.path.join(input_directory, "output_files")):
    os.mkdir(os.path.join(input_directory, "output_files"))
if not os.path.exists(os.path.join(input_directory, "temporary_files")):
    os.mkdir(os.path.join(input_directory, "temporary_files"))

os.chdir(os.path.join(input_directory, "temporary_files"))# same as env.workspace
arcpy.env.workspace = os.path.join(input_directory, "output_files")
location_list = glob.glob("*.csv") # Find all CSV files
# Create the workspace
arcpy.env.workspace = r"C:\NRS_528\Assignment\MidtermCodingChallenge"

in_features = "Municipalities__1989_.shp"

# Add a name from the output created by the model
out_feature_class = "Westerly.shp"

# For the select tool you have to add in another parameter to select the data
# For this attempt I chose to select from the towns layer areas that were equal to Washington county
where_clause = "NAME = 'WESTERLY'"

# This is the select tool that will allow the code to run
arcpy.analysis.Select(in_features, out_feature_class, where_clause)

print("Westerly County Selected")

data_file = "E-911_Fire_Hydrants.csv"
input_directory = r"C:\NRS_528\Assignment\MidtermCodingChallenge"

if not os.path.exists(os.path.join(input_directory, "output_files")):
    os.mkdir(os.path.join(input_directory, "output_files"))
if not os.path.exists(os.path.join(input_directory, "temporary_files")):
    os.mkdir(os.path.join(input_directory, "temporary_files"))

os.chdir(os.path.join(input_directory, "temporary_files"))# same as env.workspace
arcpy.env.workspace = os.path.join(input_directory, "output_files")
location_list = glob.glob("*.csv") # Find all CSV files

# This is where I imported the fire hydrants found in the csv file and
# created the list of the locations where they are found
with open('E-911_Fire_Hydrants.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)
    location_list = []
    for row in csv_reader:
        if row[20] not in location_list:
            location_list.append(row[20])

print(location_list)

for hydrants in location_list:
    file_name = hydrants + ".csv"
    print(hydrants + ".csv")
    file = open(file_name, "w")
    file.write(",".join(header))
    file.write("\n")

    with open('E-911_Fire_Hydrants.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        location_list = []
        for row in csv_reader:
            if hydrants == row[20]:
                print(hydrants)
                file.write(",".join(row))
                file.write("\n")

    in_Table = hydrants + ".csv"
    x_coords = "x-Coords"
    y_coords = "y-Coords"
    z_coords = ""
    out_Layer = hydrants
    saved_Layer = "hydrants_output.shp"

# Set the spatial reference in this case the spatial reference is WGS 1984
    spRef = arcpy.SpatialReference(4326)  # 4326 == WGS 1984
    lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)

# Count the number of each file and print it
    print(arcpy.GetCount_management(out_Layer))

# Save to a layer file
    arcpy.CopyFeatures_management(lyr, saved_Layer)
    if arcpy.Exists(saved_Layer):

        print("Created file successfully!")









