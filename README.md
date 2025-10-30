My-Zootopia: Animals Project
This Python project fetches animal data with API Ninja Animals API and generates an HTML website.

Features:
- Dynamically fetches animal data from the API.
- Generate HTML website with one card for each animal.
- .env contains API.

Installation:
1. Clone the repository:
git clone <your-repo-url>

2. Create and activate your virtual environment (optional but recommended):
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows

3. Install dependencies: 
pip install -r requirements.txt

4. PI-KEY: Create a .env file in the root directory with your'API_KEY'

5. Usage Text: 
- Run the program: python animals_web_generator.py
- Enter the name of an animal when prompted: Fox
- animals.html will be generated with the results for Fox.
