import requests
import json
import time
import os

# Define your API key for accessing weather data
API_KEY = "095e88e26e214b71968153950230511"  # Replace with your actual API key

auto_refresh_interval = 15  # Initialize auto-refresh interval to 15 seconds

# Function to get weather data for a given city
def get_weather_data(city):
    # Construct the URL with the API key and the city
    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=yes"
    # Send an HTTP GET request to the API
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = json.loads(response.text)
        return data
    else:
        # Raise an exception if the API request failed
        raise Exception("Failed to retrieve weather data for the city.")

# Function to print weather information
def print_weather_data(data):
    # Extract location and current weather data
    location = data["location"]
    current = data["current"]

    # Print weather information
    print("Location: " + location["name"])
    print("Temperature: " + str(current["temp_c"]) + "°C / " + str(current["temp_f"]) + "°F")
    print("Humidity: " + str(current["humidity"]) + "%")
    print("Wind Speed: " + str(current["wind_mph"]) + " mph / " + str(current["wind_kph"]) + " km/h")
    print("Wind Direction: " + current["wind_dir"])

# Function to add a city to the favorite list
def add_favorite_city(city, favorite_cities):
    if city not in favorite_cities:
        favorite_cities.append(city)
        return favorite_cities
    else:
        print(f"{city} is already in your favorite cities.")
        return favorite_cities

# Function to remove a city from the favorite list
def remove_favorite_city(city, favorite_cities):
    if city in favorite_cities:
        favorite_cities.remove(city)
        return favorite_cities
    else:
        print(f"{city} is not in your favorite cities.")
        return favorite_cities

# Main application loop
favorite_cities = []
selected_city = None

# Load favorite cities from a file if it exists
if os.path.exists("favorite_cities.txt"):
    with open("favorite_cities.txt", "r") as file:
        favorite_cities = [line.strip() for line in file]

while True:
    print("Options:")
    print("1. Check weather by city name")
    print("2. Add a city to favorites")
    print("3. Remove a city from favorites")
    print("4. View favorite cities")
    print("5. Set auto-refresh interval")
    print("6. Refresh weather for selected city")
    print("7. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6/7): ")

    if choice == '1':
        city = input("Please enter the name of a city: ")
        weather_data = get_weather_data(city)
        print("Weather information for", city + ":")
        print_weather_data(weather_data)
        selected_city = city

    elif choice == '2':
        city = input("Please enter the name of a city to add to favorites: ")
        favorite_cities = add_favorite_city(city, favorite_cities)
        print(f"{city} has been added to your favorite cities.")

    elif choice == '3':
        city = input("Please enter the name of a city to remove from favorites: ")
        favorite_cities = remove_favorite_city(city, favorite_cities)
        print(f"{city} has been removed from your favorite cities.")

    elif choice == '4':
        print("Your favorite cities:", favorite_cities)

    elif choice == '5':
        try:
            interval = int(input("Enter auto-refresh interval in seconds (15-30 seconds): "))
            if 15 <= interval <= 30:
                auto_refresh_interval = interval
            else:
                print("Interval should be between 15 and 30 seconds.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    elif choice == '6':
        if selected_city:
            weather_data = get_weather_data(selected_city)
            print("Weather information for", selected_city + ":")
            print_weather_data(weather_data)
        else:
            print("No city selected for refreshing.")

    elif choice == '7':
        break

    time.sleep(auto_refresh_interval)

# Save favorite cities to a file
with open("favorite_cities.txt", "w") as file:
    for city in favorite_cities:
        file.write(city + "\n")

print("Goodbye!, Visit Again")
