import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

with open("animals_template.html", "r") as template:
    animals_template = template.read()
    print(animals_template)



# Flatten the data if it's nested lists
def flatten(data):
    result = []
    if isinstance(data, list):
        for item in data:
            if isinstance(item, list):
                result.extend(flatten(item))
            elif isinstance(item, dict):
                result.append(item)
    elif isinstance(data, dict) and "animals" in data:
        result.extend(flatten(data["animals"]))
    return result

animals_list = flatten(animals_data)


output = ""
# Iterate through animals safely
for animal in animals_data:
    name = animal.get("name")
    locations = animal.get("locations", [])
    characteristics = animal.get("characteristics", {})
    diet = characteristics.get("diet")
    animal_type = characteristics.get("type")
    output += name


    if name:
        print(f"Name: {name}")
    if diet:
        print(f"Diet: {diet}")
    if isinstance(locations, list) and locations:
        print(f"Location: {locations[0]}")
    if animal_type:
        print(f"Type: {animal_type}")

    print()  # blank line between animals

print(output)