# Converting JSON to Python Objects

import requests
import json

# Fetching data from the Pokemon API
response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
json_data = response.text

# What JSON Data looks like:
"""
{
  "name": "Pikachu",
  "type": "Electric",
  "level": 25
}
"""

# Converting JSON to Python Object (Dictionary)
pikachu_data = json.loads(json_data)

# JSON looks like Dictionaries (Python)

# Accessing data
print(pikachu_data["name"]) # Output: pikachu
print(pikachu_data["types"]) # Outputs the types of Pikachu

