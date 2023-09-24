# Task 4

import requests

def get_weather_data(api_key, location):
    base_url = "https://api.openweathermap.org/data/2.5/weather?"

    try:
        # Check if the location input is a zip code (numeric) or city name (string)
        if location.isdigit():
            params = f"zip={location},us"
        else:
            params = f"q={location}"

        complete_url = f"{base_url}{params}&appid={api_key}&units=metric"  # You can change units to imperial for Fahrenheit

        response = requests.get(complete_url)

        # Check if the API request was successful
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print("Error: Unable to fetch weather data.")
            return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


def display_weather(weather_data):
    if weather_data:
        city = weather_data['name']
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        description = weather_data['weather'][0]['description']

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Description: {description}")
    else:
        print("No weather data to display.")


def main():
    print("Welcome to the Weather Application")
    api_key = "1fb357471c41c8fafe1a5e40a7cf9ea0"

    while True:
        location = input("Enter a city name or zip code: ")

        weather_data = get_weather_data(api_key, location)

        if weather_data:
            display_weather(weather_data)
        else:
            print("Invalid city name. Please enter a valid city name or zip code.")

        another_time = input("Do you want to check the weather for another location? (yes/no): ")
        if another_time.lower() != "yes":
            print("Thank you for using the Weather Application. Goodbye!")
            break


if __name__ == "__main__":
    main()
