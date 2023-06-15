""" Assignment 2 is a function reads the json file and stores it value in dict variable named ex5.

Looping through each element in the list of dict we check for two values to be present in side dict one is name should be `Old Fashioned` other is type `donut` else continue the loop.

if true check for the batter name `Coffee` present in the list of dict then return.

if false sort the list of batters dict based on `id` key. Increment the id by one and set type as `Coffee` , append it to batters dict.
"""

import json


def sortById(e):
    return e['id']


def assignment2():
    with open('ex5.json', 'r') as jsonFile:
        if not jsonFile.readline():
            print('file is empty')
            return
        jsonFile.seek(0)
        ex5 = json.load(jsonFile)
        jsonFile.close()

    for data in ex5:
        if (type(data) is not dict):
            print('Data is not in the type of dict')
            return
        if 'Old Fashioned' in data['name'] and 'donut' in data['type']:
            batters = data['batters']['batter']
            if any('Coffee' in batter['type'] for batter in batters):
                print('Type Coffee already present in the batter')
                return
            batters.sort(key=sortById)
            newId = int(batters[-1]['id'])+1
            batters.append({'id': str(newId), 'type': 'Coffee'})
            print(f"Added batter type Coffee with id {newId}.")

    with open('ex5.json', 'w') as jsonFile:
        json.dump(ex5, jsonFile)
        jsonFile.close()


if __name__ == "__main__":
    assignment2()
