import pickle

country_capitals = {}

def add_country(country, capital):
    country_capitals[country] = capital
    print(f"Added: {country} - {capital}")

def delete_country(country):
    if country in country_capitals:
        del country_capitals[country]
        print(f"Deleted: {country}")
    else:
        print(f"{country} not found.")

def find_country(country):
    return country_capitals.get(country, "Not found")

def edit_country(country, new_capital):
    if country in country_capitals:
        country_capitals[country] = new_capital
        print(f"Updated: {country} - {new_capital}")
    else:
        print(f"{country} not found.")

def save_data(filename):
    with open(filename, 'wb') as file:
        pickle.dump(country_capitals, file)
    print("Data saved successfully.")

def load_data(filename):
    global country_capitals
    try:
        with open(filename, 'rb') as file:
            country_capitals = pickle.load(file)
        print("Data loaded successfully.")
    except FileNotFoundError:
        print("File not found. Starting with an empty dictionary.")

if __name__ == "__main__":
    add_country("Slovakia", "Kosice")
    add_country("Czechia", "Praha")
    print("Slovakia:", find_country("Slovakia"))
    edit_country("Slovakia", "Bratislava")
    delete_country("Czechia")
    save_data("countries.pkl")
    load_data("countries.pkl")