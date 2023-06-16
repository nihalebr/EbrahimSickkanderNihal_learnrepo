"""
This module is about manipulating data using python. 
It has several function and each has it's own functionality.
This module contains on topic of data and data manipulation.
"""

def sortById(e):
    return e['id']

def insertBatter(recipes:list):
    """
    This function is used to insert the batter type `coffee` into batters of the `donut` named `Old Fashioned` if it is absent.

    Args:
        recipes (list): A list of recipe to check 

    Returns:
        list: Updated list of recipe
    """
    for recipe in recipes:
        if (type(recipe) is not dict):
            return "Data is not in the type of dict"
        if 'Old Fashioned' in recipe['name'] and 'donut' in recipe['type']:
            batters = recipe['batters']['batter']
            if any('Coffee' in batter['type'] for batter in batters):
                return "Type Coffee already present in the batter"
            batters.sort(key=sortById)
            newId = int(batters[-1]['id'])+1
            batters.append({'id': str(newId), 'type': 'Coffee'})
            return recipes

def removeBatter(recipes:list):
    """
    This function is used to remove the batter type `coffee` from the batters of the `donut` named `Old Fashioned` if it is present.

    Args:
        recipes (list): A list of recipe to check 

    Returns:
        list: Updated list of recipe
    """
    for recipe in recipes:
        if (type(recipe) is not dict):
            return "Data is not in the type of dict"
        if 'Old Fashioned' in recipe['name'] and 'donut' in recipe['type']:
            batters = recipe['batters']['batter']           
            for index in range(len(batters)):
                if batters[index]['type'] == 'Coffee':
                    del batters[index]
        
    return recipes
                    
        