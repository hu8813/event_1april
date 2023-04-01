import requests

try:
    name = input("Enter the name of a pokemon: ")
    if name == "":
        raise Exception("Error: No name given")
    name = name.strip().lower()

    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        abilities = [ability['ability']['name'] for ability in data['abilities']]
        print(f"Name: {data['name']}")
        print("Abilities:")
        for ability in abilities:
            print(f"- {ability}")   
    else:
        raise Exception("Error: Could not find Pokemon data")
except Exception as e:
    print(f"An error occurred: {e}")
