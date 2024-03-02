import arcpy

def get_council_districts(geometry):
    districts = set()  # Using a set to store unique district numbers
    # Create an in-memory feature layer to store the input geometry
    arcpy.management.CreateFeatureclass("in_memory", "temp_geom", "POLYGON")
    arcpy.management.AddField("in_memory/temp_geom", "SHAPE@", "TEXT")
    with arcpy.da.InsertCursor("in_memory/temp_geom", ["SHAPE@"]) as cursor:
        cursor.insertRow([geometry])
    # Intersect the input geometry with the district boundaries
    arcpy.analysis.Intersect(["in_memory/temp_geom", "district_layer"], "in_memory/intersect_output")
    # Iterate over the intersected features
    for row in arcpy.da.SearchCursor("in_memory/intersect_output", "COUNCIL_DISTRICT"):
        districts.add(str(row[0]))  # Convert district number to string before adding
    if districts:
        return ','.join(sorted(districts, key=int))  # Sort the districts numerically before joining
    else:
        return None
