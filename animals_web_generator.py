import data_fetcher
import os

TEMPLATE_FILE = "animals_template.html"
OUTPUT_FILE = "animals.html"

def generate_website(animals, animal_name):
    if not os.path.exists(TEMPLATE_FILE):
        print(f"Error: Template file '{TEMPLATE_FILE}' not found.")
        return

    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        template = f.read()

    animals_html = ""

    for animal in animals:
        card = "<li class='cards__item'>"
        card += f"<h2 class='card__title'>{animal.get('name')}</h2>"

        if animal.get('latin_name'):
            card += f"<p>Latin Name: {animal['latin_name']}</p>"
        if animal.get('animal_type'):
            card += f"<p>Type: {animal['animal_type']}</p>"
        if animal.get('active_time'):
            card += f"<p>Active Time: {animal['active_time']}</p>"
        if animal.get('length_min') and animal.get('length_max'):
            card += f"<p>Length: {animal['length_min']} - {animal['length_max']} ft</p>"
        if animal.get('weight_min') and animal.get('weight_max'):
            card += f"<p>Weight: {animal['weight_min']} - {animal['weight_max']} lbs</p>"

        char = animal.get("characteristics", {})
        if char.get("lifespan"):
            card += f"<p>Lifespan: {char['lifespan']}</p>"
        if char.get("habitat"):
            card += f"<p>Habitat: {char['habitat']}</p>"
        if char.get("diet"):
            card += f"<p>Diet: {char['diet']}</p>"

        card += "</li>"
        animals_html += card

    if not animals_html:
        animals_html = f"<h2 style='color:red;'>The animal '{animal_name}' doesn't exist.</h2>"

    html_content = template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Website was successfully generated to {OUTPUT_FILE}")

if __name__ == "__main__":
    user_input = input("Enter a name of an animal: ").strip()
    animals = data_fetcher.fetch_data(user_input)
    generate_website(animals, user_input)