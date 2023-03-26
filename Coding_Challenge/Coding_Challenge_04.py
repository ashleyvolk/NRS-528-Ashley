# Coding Challenge 4.py
# For this coding challenge, I want you to find a particular tool that you like in arcpy.
# It could be a tool that you have used in GIS before or something new.
# Try browsing the full tool list to get some insight here (click Tool Reference on the menu list to the left).
#
# Set up the tool to run in Python, add some useful comments, and importantly,
# provide some example data in your repository
# (try to make it open source, such as Open Streetmap, or RI GIS. You can add it as a zip file to your repository.
#
# My only requirements are:
#
# Comment your code well.
# Ensure that the code will run on my machine with only a
# single change to a single variable (i.e. a base folder location).

# Import arcpy to allow for tools from GIS to be present
import arcpy
# from arcpy import env
# # Add in all of the data you need
# #Add where the data is coming from
env.workspace = r"E:\NRS_528_Ashley\Coding_Challenge_4"

# #Add in which feature you want to pull data from
in_features = r"E:\NRS_528_Ashley\Coding_Challenge_4\Municipalities__1989_.shp"

# #Add a name from the output created by the model
out_feature_class = r"E:\NRS_528_Ashley\Coding_Challenge_4\Washington_town.shp"

# #for the select tool you have to add in another parameter to select the data
# For this attempt I chose to select from the towns layer areas that were equal to Washington county
where_clause = "COUNTY = 'WASHINGTON'"

# #This is the select tool that will allow the code to run
arcpy.analysis.Select(in_features, out_feature_class, where_clause)
