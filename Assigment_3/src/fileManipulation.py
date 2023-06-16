"""
This module is about manipulating data using python. 
It has several function and each has it's own functionality.
This module contains on topic of file and file manipulation.
"""

import json,os

def readJSON(filePath:str):
    """
    This function is used to read the JSON file from the Specified `filePath`
    
    Args:
        filePath (string): JSON file to be read

    Returns:
        any: Data from the JSON file 
    """
    with open(filePath, 'r') as jsonFile:
        if os.stat(filePath).st_size == 0:
            return "File is empty."
        jsonData = json.load(jsonFile)
        jsonFile.close()
    return jsonData

def writeJSON(filepath:str,data):
    """
    write the given `data` into the `filePath` as JSON format.

    Args:
        filepath (string): JSON file to be written
        data (any): Data to be written in the file
    """
    with open(filepath, 'w') as jsonFile:
        json.dump(data, jsonFile)
        jsonFile.close()