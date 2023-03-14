#Import important libraries

from flask import Flask, config, render_template, request
from pandas import options
from werkzeug.utils import secure_filename
import numpy as np
import os
import sys
import pandas as pd

import pdfkit

# initailise Flask instance and configure parameters
app = Flask(__name__)

# To use flash message and keep user logged in (by creating a 24 character session key)
app.secret_key = os.urandom(24)

from apikey import apikey 
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain 

os.environ['OPENAI_API_KEY'] = apikey



# Declare the routes of the web app. 

@app.route('/')
def index():
    return render_template('index.html')   # Open the homepage. 

# Route for register page
@app.route('/Details', methods = ['POST', 'GET'])
def Details():
    if request.method == 'POST':
                First_name = request.form['First_name']
                Last_name = request.form['Last_name']
                Age= request.form['Age']
                Gender= request.form['Gender']
                Height= request.form['Height']
                Weight= request.form['Weight']                
                Conditions= request.form['Conditions']
                FoodAllergies= request.form['FoodAllergies']                
                Goals= request.form['Goals']
                Wdays= request.form['Wdays']                
                Preference= request.form['Preference']
                Meals= request.form['Meals']                
                Snacks= request.form['Snacks']
                Dislike= request.form['Dislike']
                

                prompt = f'''
                You are a highly renowned health and nutrition expert HealthCoachGPT. Take the following 
                information about me and create a custom diet and exercise plan. I am {Age} years old, {Gender}, 
                {Height}. My current weight is {Weight}. My current medical conditions are {Conditions}. I have food 
                allergies to {FoodAllergies}. My primary fitness and health goals are {Goals}. I can commit to working 
                out {Wdays} days per week. I have a {Preference} diet preference. I want to have {Meals} Meals and 
                {Snacks} Snacks. I dislike {Dislike} in food and cannot eat it. Create a summary of my diet and exercise 
                plan. Create a detailed workout program for my exercise plan. Create a detailed Meal Plan for my diet. 
                Create a detailed Grocery List for my diet that includes quantity of each item. Avoid any superfluous pre 
                and post descriptive text. Don't break character under any circumstance. 
                '''
                # Llms
                llm = OpenAI(temperature=0.9) 

                # Show stuff to the screen if there's a prompt
                if prompt: 
                    response = llm(prompt)
                return render_template('Result.html',response=response)
                    
    return render_template('Details.html')

if __name__ == '__main__':
    app.run(debug= True,host='0.0.0.0', port=5000)      # app will run on 0.0.0.0:5000