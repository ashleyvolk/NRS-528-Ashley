# Define the tools that will be held in this toolbox
# The tools are the Select Tool, the Clip Tool, and again the Select Tool
# The tools were created to work with the municipalities data to select for towns layers in RI
# and to then clip the lakes_and_ponds layer to these areas and then perform a select tool again
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
        self.tools = [Select_Tool, Clip_Tool, Select_Greater, Buffer_Tool]

# This is the select tool that will be used for the first part of the toolbox project
class Select_Tool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Select Tool"
        self.description = "Selects for towns or counties in Rhode Island"
        self.canRunInBackground = False

# The parameters used to run the tool
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

        arcpy.Select_analysis(in_features=input_polygon,
                            where_clause=expression,
                            out_feature_class=output
                            )
        return


# Create the clip tool that will allow for layers to be clipped to a feature layer.
# In this case I used the Lakes_and_Ponds layer
class Clip_Tool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Clip Tool"
        self.description = "Clips lakes to the towns layer"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        clip_features = arcpy.Parameter(name="clip_features",
                                     displayName="Clip Features",
                                     datatype="GPFeatureLayer",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        params.append(clip_features)

        clipping_features = arcpy.Parameter(name="clipping_features",
                                        displayName="Clipping Features",
                                        datatype="GPFeatureLayer",
                                        parameterType="Required",  # Required|Optional|Derived
                                        direction="Input",  # Input|Output
                                        )
        params.append(clipping_features)

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
        clip_features = parameters[0].valueAsText
        clipping_features = parameters[1].valueAsText
        output = parameters[2].valueAsText

        arcpy.Clip_analysis(in_features=clip_features,
                            clip_features=clipping_features,
                            out_feature_class=output,
                            cluster_tolerance="")
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

        arcpy.Buffer_analysis(in_features=buffer,
                              out_feature_class=buffer_output,
                              buffer_distance_or_field=distance_value + " " + distance_field,
                              line_side="FULL",
                              line_end_type="ROUND",
                              dissolve_option="ALL",
                              dissolve_field=[],
                              method="PLANAR")
        return
