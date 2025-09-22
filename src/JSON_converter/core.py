import json
import re

#checks if dms is in correct order
dms_pattern = re.compile(
    r"""^
    (\d{1,3})°          # degrees
    (\d{1,2})'          # minutes
    (\d{1,2}(?:\.\d+)?)"? # seconds (integer or float, optional quotes)
    \s*([NSEW])$        # direction
    """, re.VERBOSE
)

def check_dms(dms):
    return dms_pattern.match(dms)

def convert_dms(dms):
    match = check_dms(dms)
    if not match:
        print(f"DMS {dms} is not in correct DMS format")
        return None
    degrees, minutes, seconds, direction = match.groups()
    degrees = int(degrees)
    minutes = int(minutes)
    seconds = float(seconds)
    decimal = degrees + minutes / 60 + seconds / 3600
    if direction in ['S', 'W']:
        decimal *= -1
    return decimal
#Main Function Definition
def JSON_converter(file_path, geo_string):
    if geo_string != "Point" and geo_string != "Polygon" and geo_string != "LineString":
        print(f"Error: The Geometry type '{geo_string}' is invalid")
        return None
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
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

   



