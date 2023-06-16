# Importing the required libraries
from flask import Flask,jsonify
from src.fileManipulation import readJSON,writeJSON
from src.dataManipulation import insertBatter,removeBatter
import os

# Defining the Flask app
app = Flask(__name__)

@app.errorhandler(404)
def notAvailable(e):
    """
    returns all unused endpoint as Service Unavailable with code 503.
    response is dict which hold response data such as status & statusCode.
    """
    response = {"status":"Service Unavailable","statusCode":503}
    return jsonify(response),503
    
@app.route('/api/printHello',methods=['GET'])
def printHello():
    """
    returns a simple Message.
    """
    return "Helllo World!!",200

@app.route('/api/modifyRecipe',methods=['GET'])
def modifiedRecipe():
    """
    In this endpoint returns the modified JSON data.
    It return Internal server error on file empty and DataType does not match.
    It return Not Modified message if Coffee is already present.
    response is dict which hold response data such as status & statusCode.
    """
    response = {"status":"Internal Server Error","statusCode":500}
    recipes = readJSON(workingDir+'/ex5.json')
    
    if recipes == 'File is empty.':
        print(f"/api/modifyRecipe")
        return jsonify(response),500
    
    updatedRecipes = insertBatter(recipes)
    
    if updatedRecipes == 'Data is not in the type of dict':
        return jsonify(response),500
    
    if updatedRecipes == 'Type Coffee already present in the batter':
        response['status'] = 'Not Modified'
        response['statusCode'] = 304
        response['message'] = 'Type Coffee already present in the batter'
        response['recipes']=recipes
        return jsonify(response),200
    writeJSON(workingDir+'/ex5.json',updatedRecipes)
    
    response['status']="successful"
    response['statusCode']=200
    response['message'] = 'Successfully added the Coffee batter'
    response['recipes']=recipes
    return jsonify(response),200

@app.route('/api/resetRecipe',methods=['GET'])
def resetRecipe():
    """
    In this endpoint returns the reseted JSON data.
    It return Internal server error on file empty and DataType does not match.
    response is dict which hold response data such as status & statusCode.
    """
    response = {"status":"Internal Server Error","statusCode":500}
    recipes = readJSON(workingDir+'/ex5.json')
    
    if recipes == 'File is empty.':
        return jsonify(response),500
    
    updatedRecipes = removeBatter(recipes)
    
    if updatedRecipes == 'Data is not in the type of dict':
        return jsonify(response),500
    
    writeJSON(workingDir+'/ex5.json',updatedRecipes)
    
    response['status']="successful"
    response['statusCode']=200
    response['recipes']=recipes
    return jsonify(response),200



if __name__=='__main__':
    workingDir = os.getcwd() # Get's current working dir
    app.run(debug=True,port=8080)