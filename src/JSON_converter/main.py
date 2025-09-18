from core import JSON_converter, convert_dms

import json

result = JSON_converter("coordinates.json", "Point")
if result:
    lat = convert_dms(result["coordinates"]["latitude"])
    lon = convert_dms(result["coordinates"]["longitude"])
    print("Converted:", lat, lon)
