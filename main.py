from flask import Flask, render_template, request
import requests
import random

import os 
app = Flask('chaps van de dag')

# Define the API key and base URL for the weather service
api_key = '74343a12d034b366a3631cc809dbe21a'
base_url = 'http://api.weatherstack.com/current'

@app.route('/')
def index():
    return render_template('index.html')
  


@app.route('/get_weather/<stad>')
def get_weer(stad):

    weather_data = get_weather(stad)

    if weather_data:
      season = rate_weather(weather_data)
   
      print(f"Happie van de dag in {stad}: {season}")
      recipe = get_recipe(season)
      print(recipe)
    return "helaas"


def rate_weather(data):
    if data is None:
        return "Kan het weer niet beoordelen vanwege een fout."

    temperature = data['current']['temperature']
    weather_description = data['current']['weather_descriptions'][0].lower()

    if 'rain' in weather_description:
        if temperature < 15:
            return "Winter"
        else:
            return "Spring"
    elif 'cloud' in weather_description:
        return "Potato"
    else:
        if temperature > 20:
            return "Summer"
        else:
            return "Autumn"

def get_weather(city):
    params = {
      'access_key': api_key,
      'query': city,
    }
    try:

      response = requests.get(base_url, params=params)
      response.raise_for_status()  # Check for errors when retrieving data
  
      data = response.json()
      return data
    except requests.exceptions.RequestException as e:
      print(f"Fout bij het ophalen van het weer: {e}")
      return None
    
#if __name__ == "__main__":
#    stad = 'new york'
#    weather_data = get_weather(stad)
#    if weather_data is not None:
#        weather_score = rate_weather(weather_data)
#        print(f"Happie van de dag in {stad}: {weather_score}")

def get_recipe(season):
    url = 'https://api.edamam.com/search'

    # Parameters for the recipe
    parameters = {
        'app_id': 'f2eb4847',
        'app_key': 'c5a1518f1656855055679d83d4872c6f',
        'q': season,  # Assuming 'seazon' is supposed to be 'season'
    }
    print(parameters)

    # Make a GET request to the API
    response = requests.get(url, params=parameters)

    if response.status_code == 200:
        data = response.json()

        # Choose a random recipe from the results
        if 'hits' in data and len(data['hits']) > 0:
            random_recipe = random.choice(data['hits'])
            recipe_label = random_recipe['recipe']['label']
            recipe_url = random_recipe['recipe']['url']

            print(f'Willekeurig recept: {recipe_label}')
            print(f'Recept URL: {recipe_url}')
        else:
            print('Geen recepten gevonden.')
    else:
        print('Fout bij het ophalen van het recept.')

#if __name__ == '__main__':
   # seazon = 'winter'  # Assuming 'seazon' is supposed to be 'season'
   # get_random_recipe()

app.run(host= '0.0.0.0', port=5000	)