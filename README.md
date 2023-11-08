# Weather Information Application

This Python command-line application allows users to check weather information for various cities, add and remove cities from their favorite list, set an auto-refresh interval for weather data, and refresh weather information for the selected city. The application uses the WeatherAPI to fetch weather data.

## Prerequisites

Before you can run this application, make sure you have the following prerequisites in place:

1. **Python**: You should have Python installed on your system. You can download Python from the official website: [Python Downloads](https://www.python.org/downloads/)

2. **Required Python Libraries**: You need to install the necessary Python libraries using pip. Open a terminal or command prompt and run the following command:

`pip install request:`


## Usage

Follow these steps to execute the application:

1. **Obtain an API Key**:

You need to replace the `API_KEY` in the code with your own API key for accessing weather data. You can obtain an API key by signing up at the WeatherAPI website (https://www.weatherapi.com/).

2. **Run the Application**:

- Save the code in a Python file, for example, `weather_app.py`.
- Open a terminal or command prompt.
- Navigate to the directory where `weather_app.py` is located.
- Run the application by executing the following command:

  ```
  python weather_app.py
  ```

3. **Using the Application**:

Once the application is running, you can interact with it using the provided options:

- **Check weather by city name**: Enter '1' and input a city name to retrieve weather information for that city.

- **Add a city to favorites**: Enter '2' and input a city name to add it to your list of favorite cities.

- **Remove a city from favorites**: Enter '3' and input a city name to remove it from your favorite cities.

- **View favorite cities**: Enter '4' to see a list of your favorite cities.

- **Set auto-refresh interval**: Enter '5' and input the desired auto-refresh interval in seconds (between 15 and 30 seconds).

- **Refresh weather for selected city**: Enter '6' to refresh weather information for the previously selected city.

- **Exit**: Enter '7' to exit the application.

4. **Saving Favorite Cities**:

The application will save your list of favorite cities in a file named `favorite_cities.txt`. You can find this file in the same directory where the Python script is located.

## Note

Make sure to keep your API key secure, and do not share it publicly. The application periodically auto-refreshes weather data for the selected city based on the interval you set.

Enjoy using the Weather Information Application! If you have any questions or encounter issues, please refer to the provided information or consult the WeatherAPI documentation for more details.
