import arcpy
arcpy.env.overwriteOutput = True
input_shp = r'C:\NRS_528\Assignment\CodingChallenge09\RI_Forest_Health_Works_Project%3A_Points_All_Invasives.shp'
fields = ['species']

expression = arcpy.AddFieldDelimiters(input_shp, "Species") + " <> ' '"  # Cleaner and easier to code
species = 0
with arcpy.da.SearchCursor(input_shp, fields, expression) as cursor:
    for row in cursor:
        species = species + 1
print("Printing species")
print(species)