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