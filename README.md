# Ebrahim Sickkander Nihal's Learn Repo

## Assignment 1

- Create a repo under this specified model `yourname_learnrepo`.
- Create a simple Python File and Push the same to the RemoteRepo.

## Assignment 2 

- TL;DR : Create a Python file that will read a JSON file and Update it.
- Get Sample Data From this [site](https://opensource.adobe.com/Spry/samples/data_region/JSONDataSetSample.html#Example5) (or you can see the [file](./Assigment2.json) ).
- After collecting the data from the site store the json file in the name of `ex5.json`.
- Now, Read the JSON file and Store the content of the file in a variable named `ex5` and use `dictionary` as data type.
- Finally, add a batter named `coffee` for `donut` with name `Old Fashioned` and update the `ex5.json` file.

## Assignment 3
- TL;DR : Create a flask api app for two endpoints.
- create a virtual environment in side working folder for me `Assigment_3`.
  ```bash
  user@username $ python3 -m venv .venv
  ```  
- Then install dependence package flask using pip.
- create two endpoint
  - /api/printHello
  - /api/modifyRecipe
- when you call on the endpoint `printHello` it should return string saying `Helllo World!!`.
- when you call on the endpoint `modifyRecipe` it should return the modified json value.