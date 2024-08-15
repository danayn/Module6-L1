#Assignment:  Web Fundamentals
'''
2. Exploring the Digital Cosmos with Python and the Web

Problem Statement: Imagine you are a developer tasked with creating a feature for a web application that provides users with 
insightful information about various space objects. Your application will fetch data from a publicly available space API, 
process this data, and display it in a user-friendly format.

Task 1: Set up a Python Virtual Environment and Install Required Packages

Create a new virtual environment in Python. Activate the virtual environment. Install the `requests` package for making HTTP 
requests.

Expected Outcome: A successfully created and activated virtual environment with the `requests` package installed.

Task 2: Fetch Data from a Space API Write a Python script that makes a GET request to a space API (e.g., [The Solar System 
OpenData](https://api.le-systeme-solaire.net/en/)) to fetch data about planets.

Parse the JSON response and extract information about each planet, such as its name, mass, and orbit period.

Code Example:

import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    #process each planet info
    for planet in planets:
        if planet['isPlanet']:
            name = #get planet English name
            mass = #get planet mass
            orbit_period = #get planet orbit period
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

fetch_planet_data()
Expected Outcome:

Planet: Uranus, Mass: 8.68127, Orbit Period: 30685.4 days
Planet: Neptune, Mass: 1.02413, Orbit Period: 60189.0 days
Planet: Jupiter, Mass: 1.89819, Orbit Period: 4332.589 days
Planet: Mars, Mass: 6.41712, Orbit Period: 686.98 days
Planet: Mercury, Mass: 3.30114, Orbit Period: 87.969 days
Planet: Saturn, Mass: 5.68336, Orbit Period: 10759.22 days
Planet: Earth, Mass: 5.97237, Orbit Period: 365.256 days
Planet: Venus, Mass: 4.86747, Orbit Period: 224.701 days
Task 3: Data Presentation and Analysis - Perform a simple analysis, such as finding the planet with the longest orbit period 
or the heaviest planet. 

import requests

def fetch_planet_data():
    # Enhance format the output in a more readable manner
    return #list of planets

def find_heaviest_planet(planets):
    return #heaviest planet

planets = fetch_planet_data()
name, mass = find_heaviest_planet(planets)
print(f"The heaviest planet is {name} with a mass of {mass} kg.")
Expected Outcome: A more structured and formatted output, along with an analysis result, such as identifying the heaviest 
planet in the solar system.

'''

# Task 1: Set up a Python Virtual Environment and Install Required Packages
#
#
import requests
import json



# Task 2: Fetch Data from a Space API
#Fetching data from the SPACE API
def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    #process each planet info
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            #mass is a python dictionary
            mass = planet['mass']
            orbit_period = planet['sideralOrbit']
            massv = mass["massValue"]
            print(f"Planet: {name}, Mass: {massv}, Orbit Period: {orbit_period} days")

fetch_planet_data()
print()


# Task 3: Data Presentation and Analysis 
def fetch_planet_data():
    # Enhance format the output in a more readable manner
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']
    return planets#list of planets

def find_heaviest_planet(planets):
    x = 0
    heaviest = ""
    for planet in planets:
        if planet['isPlanet']:
          mass = planet['mass']
          massv = mass["massValue"]
          if(massv > x):
              x = massv
              name = planet['englishName']
              heaviest = name
        
    return heaviest, x #heaviest planet

planets = fetch_planet_data()
name, mass = find_heaviest_planet(planets)
print(f"The heaviest planet is {name} with a mass of {mass} kg.")