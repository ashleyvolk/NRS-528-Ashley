import arcpy

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Python Toolbox Final"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [Select_Tool, Clip_Tool, Select_Greater]


class Select_Tool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Select Tool"
        self.description = ""
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
                            select_features=expression,
                            out_feature_class=output,
                            cluster_tolerance="")
        return




class Clip_Tool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Clip Tool"
        self.description = ""
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




class Select_Greater(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Select Greater Tool"
        self.description = ""
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
                            out_feature_class=output,
                            cluster_tolerance="")
        return


