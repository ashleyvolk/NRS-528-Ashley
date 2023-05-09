# Define the tools that will be held in this toolbox
# The tools are the Select Tool, the List Features tool, the Clip Tool, and again the Select Tool
# The tools were created to work with the municipalities data to select for towns layers in RI
# and to then clip the lakes_and_ponds layer to these areas. After this you use the list features tool to identify
# specific features from a folder and then count the features listed. Then perform a select again
# to select to lakes_and_ponds greater than a certain size. Once the lakes_and_ponds are selected then buffer them so that we know what is
# included in the area around them and what can impact the quality of these lakes and ponds.
import arcpy

# Create the toolbox
class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Python Toolbox Final"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [Select_Clip_Tool, List_Features, Select_Greater, Buffer_Tool]

# This tool combines the select tool and clip tool into one so that it can perform both actions
# This tool will first select for towns in Rhode Island based on either name or county
# Then it will clip the lakes and ponds layer to the preset selected areas
class Select_Clip_Tool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Select and Clip Tool"
        self.description = "Selects and Clips lakes to the towns layer"
        self.canRunInBackground = False

# These are the parameters for the select tool
    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []

        input_polygon = arcpy.Parameter(name="input_polygon",
                                     displayName="Input Polygon",
                                     datatype="GPFeatureLayer",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        params.append(input_polygon)
        expression = arcpy.Parameter(name="expression",
                                        displayName="Expression",
                                        datatype="GPSQLExpression",
                                        parameterType="Required",  # Required|Optional|Derived
                                        direction="Input",  # Input|Output
                                        )
        # Add this expression to allow for the SQL expression to run
        expression.parameterDependencies = [input_polygon.name]
        params.append(expression)

        output = arcpy.Parameter(name="output_select",
                                 displayName="Output Select",
                                 datatype="DEFeatureClass",
                                 parameterType="Required",  # Required|Optional|Derived
                                 direction="Output"  # Input|Output
                                 )
        params.append(output)

# Clip tool inputs and outputs
        clip_features = arcpy.Parameter(name="clip_features",
                                     displayName="Clip Features",
                                     datatype="GPFeatureLayer",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        params.append(clip_features)
        output = arcpy.Parameter(name="output_clip",
                                 displayName="Output Clip",
                                 datatype="DEFeatureClass",
                                 parameterType="Required",  # Required|Optional|Derived
                                 direction="Output",  # Input|Output
                                 )
        params.append(output)
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        input_polygon = parameters[0].valueAsText
        expression = parameters[1].valueAsText
        output_select = parameters[2].valueAsText
        clip_features = parameters[3].valueAsText
        output_clip = parameters[4].valueAsText

# These are the two arcpy tools used in this tool
        arcpy.Select_analysis(in_features=input_polygon,
                            where_clause=expression,
                            out_feature_class=output_select)
        arcpy.Clip_analysis(in_features=clip_features,
                            clip_features=output_select,
                            out_feature_class=output_clip,
                            cluster_tolerance="")
        return

# This tool creates a list of specified features and then supplies a count for these features
class List_Features(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "List Features and Count"
        self.description = "Lists the types of data in the specific folder and then counts it"
        self.canRunInBackground = False

# The parameters used to run the tool
# This is the parameters that first allows you to set the workspace where you want to identify and count
# Then allows you to apply the wildcard (recommended to just put * as the value here)
# Then you can add the feature type (Polygon,Polyline,Shapefile,etc.)
# Then you can add a feature type but it is recommended to leave blank for this analysis
    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []

        workspace = arcpy.Parameter(name="workspace",
                                     displayName="Set directory to search",
                                     datatype="DEFolder",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        params.append(workspace)

        wild_card = arcpy.Parameter(name="wild_card",
                                     displayName="Wild Card",
                                     datatype="GPString",
                                     parameterType="Optional",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        params.append(wild_card)

        feature_type = arcpy.Parameter(name="feature_type",
                                        displayName="Feature Type",
                                        datatype="GPString",
                                        parameterType="Optional",  # Required|Optional|Derived
                                        direction="Input",  # Input|Output
                                        )
        params.append(feature_type)

        feature_dataset = arcpy.Parameter(name="feature_dataset",
                                 displayName="Feature Dataset",
                                 datatype="GPString",
                                 parameterType="Optional",  # Required|Optional|Derived
                                 direction="Output"  # Input|Output
                                 )
        params.append(feature_dataset)

        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        workspace = parameters[0].valueAsText
        wild_card = parameters[1].valueAsText
        feature_type = parameters[2].valueAsText
        feature_dataset = parameters[3].valueAsText


        arcpy.env.workspace = workspace
        list_of_feature_classes = arcpy.ListFeatureClasses(wild_card=wild_card,
                            feature_type=feature_type,
                            feature_dataset=feature_dataset)

# Add messages so that you can see the list of features after the tool runs and the count of these features
        arcpy.AddMessage(list_of_feature_classes)
        arcpy.AddMessage("The number of files in that folder is " + str(len(list_of_feature_classes)))

        return

# This is the select tool again, for this time you use the select tool to now select for things only in the specific
# area from the first select and clip. You will select for lakes and ponds that are greater than a
# certain amount in the town or county chosen.
class Select_Greater(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Select Greater Tool"
        self.description = "Selects Lakes larger than a specific amount"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        input_polygon = arcpy.Parameter(name="input_polygon",
                                     displayName="Input Polygon",
                                     datatype="GPFeatureLayer",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        params.append(input_polygon)

        expression = arcpy.Parameter(name="expression",
                                        displayName="Expression",
                                        datatype="GPSQLExpression",
                                        parameterType="Optional",  # Required|Optional|Derived
                                        direction="Input",  # Input|Output
                                        )
        expression.parameterDependencies = [input_polygon.name]
        params.append(expression)

        output = arcpy.Parameter(name="output",
                                 displayName="Output",
                                 datatype="DEFeatureClass",
                                 parameterType="Required",  # Required|Optional|Derived
                                 direction="Output",  # Input|Output
                                 )
        params.append(output)
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        input_polygon = parameters[0].valueAsText
        expression = parameters[1].valueAsText
        output = parameters[2].valueAsText

        arcpy.Select_Greater_analysis(in_features=input_polygon,
                            select_features=expression,
                            out_feature_class=output
                            )
        return

# Use the buffer tool to create a buffer distance around lakes and ponds to figure out what could be
# causing pollution runoff from areas around the lakes and ponds.
class Buffer_Tool(object):
    def __init__(self):
        self.label = "Buffer Tool"
        self.description = "The Buffer tool shows areas around the lakes and ponds"

        self.canRunInBackground = False

    def getParameterInfo(self):
# Once again define your buffer and use output from above for this input:
        params = []
        input_features = arcpy.Parameter(name="input_features",
                                   displayName="Input Features",
                                   datatype="DEShapeFile",
                                   parameterType="Required", # Required|Optional|Derived
                                   direction="Input") # Input|Output
        params.append(input_features)


# Designate what the buffer distance is
        distance_value = arcpy.Parameter(name="distance_value",
                                        displayName="Distance Value",
                                        datatype="Field",
                                        parameterType="Required", # Required|Optional|Derived
                                        direction="Input") # Input|Output
        params.append(distance_value)

# Designate if it is in feet or meters
        distance_field = arcpy.Parameter(name="distance_field",
                                      displayName="Distance Field",
                                      datatype="Field",
                                      parameterType="Required", # Required|Optional|Derived
                                      direction="Input") # Input|Output

        distance_field.columns = [['GPString', 'Field']]
        distance_field.values = [['']]
        distance_field.filters[0].list = ['Feet', 'Meters']
        params.append(distance_field)

# The output of the buffer analysis
        buffer_output = arcpy.Parameter(name="buffer_output",
                                      displayName="Buffer Output",
                                      datatype="DEFeatureClass",
                                      parameterType="Required", # Required|Optional|Derived
                                      direction="Output") # Input|Output
        params.append(buffer_output)
        return params

    def isLicensed(self):
        return True

    def updateParameters(self, parameters):
        return

    def updateMessages(self, parameters):
        return

    def execute(self, parameters, messages):
        input_features = parameters[0].valueAsText
        distance_value = parameters[1].valueAsText
        distance_field = parameters[2].valueAsText
        buffer_output = parameters[3].valueAsText
# the Buffer tool variables
        arcpy.Buffer_analysis(in_features=buffer,
                              out_feature_class=buffer_output,
                              buffer_distance_or_field=distance_value + " " + distance_field,
                              line_side="FULL",
                              line_end_type="ROUND",
                              dissolve_option="ALL",
                              dissolve_field=[],
                              method="PLANAR")
        return
