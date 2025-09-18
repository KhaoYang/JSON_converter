import json
import re


def check_dms(dms):
     dms_pattern = re.compile(
        r"""^
        (\d{1,3})°          # degrees
        (\d{1,2})'          # minutes
        (\d{1,2}(?:\.\d+)?)"? # seconds (integer or float, optional quotes)
        \s*([NSEW])$        # direction
        """, re.VERBOSE
    )
    return bool(dms_pattern.match(value))

def convert_dms(dms):
    if(!check_dms(dms)):
        print(f"DMS {dms} is not in correct DMS format")
        return None
def JSON_converter(file_path, geo_string):
    if geo_string != "Point" and geo_string != "Polygon" and geo_string != "LineString":
        print(f"Error: The Geometry type '{geo_string}' is invalid")
        return None
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            print("Successfully loaded data: ", data)
            if any(key in data for key in ['coordinates', 'coordinate', 'lat/lon', 'latitude/longitude']):
                print("Found coordinates")
                return data
            else:
                print('Error: No key for coordinates found')
                return None
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from the file '{file_path}'.")
        return None

   



