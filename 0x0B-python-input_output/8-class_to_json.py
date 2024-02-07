#!/usr/bin/python3
"""returns dictionary description"""


def class_to_json(obj):
    """Initialize an empty dictionary to store the JSON representation"""
    json_dict = {}
    
    # Iterate over the attributes of the object
    for attr_name in dir(obj):
        # Exclude special attributes (e.g., __class__, __dict__, etc.)
        if not attr_name.startswith("__"):
            # Get the value of the attribute
            attr_value = getattr(obj, attr_name)
            # Check if the attribute value is serializable
            if isinstance(attr_value, (int, float, str, bool)):
                # If serializable, add it to the JSON dictionary
                json_dict[attr_name] = attr_value
            elif isinstance(attr_value, list):
                # If the attribute value is a list, recursively serialize list
                json_dict[attr_name] = [class_to_json(item)
                        if hasattr(item, '__dict__') else item for item in attr_value]
            elif isinstance(attr_value, dict):
                # If the attribute value is a dictionary
                json_dict[attr_name] = {key: class_to_json(value)
                        if hasattr(value, '__dict__')
                        else value for key, value in attr_value.items()}
    
    return json_dict

