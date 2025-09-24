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

def parse_coordinate(value):
    """Parse a coordinate that could be float, int, or DMS string."""
    if isinstance(value, (int, float)):
        return float(value)
    elif isinstance(value, str):
        value = value.strip()
        if check_dms(value):
            return convert_dms(value)
        try:
            return float(value)
        except ValueError:
            raise ValueError(f"Invalid coordinate format: {value}")
    else:
        raise TypeError(f"Unsupported coordinate type: {type(value)}")
#Main Function Definition
#Outline: Create geoJSON function that changes the JSON into a geoJSON. Add adaptabiility characteristics based on what the format of the JSON is inputted as. Perhaps a coordinate parameter that specifies what object the coordinates are under?
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





