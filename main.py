import requests
from datetime import datetime

def get_weather_data(api_url):
    try:
        response = requests.get(api_url)
        data = response.json()
        return data['properties']['periods'][:3]  # Retrieve the forecast for the upcoming three days
    except Exception as e:
        print(f"Error fetching data from API: {e}")
        return None

def format_weather_data(weather_data):
    formatted_data = []
    for entry in weather_data:
        location = "San Francisco Bay Area"
        temperature = entry['temperature']
        condition = entry['shortForecast']
        detailed_condition = entry['detailedForecast']

        # Format date and time
        start_time = datetime.strptime(entry['startTime'], "%Y-%m-%dT%H:%M:%S%z")
        formatted_date_time = start_time.strftime("%d/%m/%Y %I:%M %p")

        formatted_entry = f"{location}\n{temperature}°F\n{condition}\n{detailed_condition}\n{formatted_date_time}\n"
        formatted_data.append(formatted_entry)

    return formatted_data

def lambda_handler(event, context):
    api_url = "https://api.weather.gov/gridpoints/MTR/84,105/forecast"
    weather_data = get_weather_data(api_url)

    if weather_data:
        formatted_data = format_weather_data(weather_data)
        return '\n'.join(formatted_data)
    else:
        return "Error fetching weather data from API."

# The following block is for local testing, not needed in AWS Lambda
if __name__ == "__main__":
    result = lambda_handler(None, None)
    print(result)













