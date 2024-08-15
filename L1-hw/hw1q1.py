#Assignment:  Web Fundamentals
'''
1. Exploring Web Technologies and Python Programming

Objective: The aim of this assignment is to deepen your understanding and practical skills in web technologies and 
Python programming. You will explore the functionalities of the World Wide Web, web architectures, and the Python programming 
language, particularly focusing on setting up environments, API interactions, and data handling.

Problem Statement: You are tasked with creating a Python application that interfaces with a public API, fetches data, 
and processes it. This application should provide insights into how different web architectures work and demonstrate your 
ability to set up a Python environment, make API requests, and handle JSON data.

Task 1: Setting Up a Python Virtual Environment and Installing Packages

1. Create a new Python virtual environment in your project directory.

2. Activate the virtual environment.

3. Install the `requests` packages.

Expected Outcome: A successfully created and activated virtual environment with the required packages installed.

Task 2: Fetching Data from the Pokémon API

1. Write a Python script to make a GET request to the Pokémon API (`https://pokeapi.co/api/v2/pokemon/pikachu`).

2. Extract and print the name and abilities of the Pokémon.

Expected Outcome: The script should output the name of the Pokémon (Pikachu) and a list of its abilities.

Task 3: Analyzing and Displaying Data

1. Modify the script to fetch data for three different Pokémon.

2. Create a function to calculate and return the average weight of these Pokémon.

3. Print the names, abilities, and average weight of the three Pokémon. **Code Example:**

def fetch_pokemon_data(pokemon_name):
    return #json response

def calculate_average_weight(pokemon_list):
    return #average weight

pokemon_names = ["pikachu", "bulbasaur", "charmander"]
Expected Outcome: The script should display the names and abilities of the three chosen Pokémon and their average weight. 
The function should correctly calculate and return the average weight based on the data fetched from the API. 

'''

#Task 1: Setting Up a Python Virtual Environment and Installing Packages -- Done
#
#

#Task 2: Fetching Data from the Pokémon API
import requests
import json
# Fetching data from the Pokemon API
response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
json_data = response.text
pikachu_data = json.loads(json_data)
# Accessing data
print(pikachu_data["name"]) # Output: pikachu
print()
print(pikachu_data["abilities"]) # Outputs the types of Pikachu
print()


#Task 3: Analyzing and Displaying Data

def fetch_pokemon_data(pokemon_name):
    ht = ''
    ht = 'https://pokeapi.co/api/v2/pokemon/'
    ht = ht + pokemon_name
    response = requests.get(ht)
    json_data = response.text
    pokemon_data = json.loads(json_data)
    print(pokemon_data["name"])
    print(pokemon_data["abilities"])
    print()
    return (pokemon_data["weight"])

def calculate_average_weight(pokemon_list):
    avg = 0
    sum = 0
    l = len(pokemon_list)
    for i in pokemon_list:
        sum = sum + i
    avg = sum / l
    print(avg)
    return avg

pokemon_names = ["pikachu", "bulbasaur", "charmander"]
pokemon_list = []
x = 0
for pokemon_name in pokemon_names:
    x = fetch_pokemon_data(pokemon_name)
    pokemon_list.append(x)

calculate_average_weight(pokemon_list)

# This code works with Internet access. 

