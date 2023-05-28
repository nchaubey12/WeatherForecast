import requests

API_KEY = &#39;YOUR_API_KEY&#39; # Replace with your OpenWeatherMap API
key

def fetch_weather_data(location):
url =
f&#39;http://api.openweathermap.org/data/2.5/weather?q={location}&amp;appid={API_
KEY}&#39;
response = requests.get(url)
return response.json()

def display_weather_data(weather_data):
# Extract relevant information from the weather data
temperature = weather_data[&#39;main&#39;][&#39;temp&#39;]
humidity = weather_data[&#39;main&#39;][&#39;humidity&#39;]
wind_speed = weather_data[&#39;wind&#39;][&#39;speed&#39;]
weather_description = weather_data[&#39;weather&#39;][0][&#39;description&#39;]

# Display the weather information
print(&#39;Weather Information:&#39;)
print(f&#39;Temperature: {temperature} K&#39;)
print(f&#39;Humidity: {humidity}%&#39;)
print(f&#39;Wind Speed: {wind_speed} m/s&#39;)
print(f&#39;Weather Description: {weather_description}&#39;)

# Get user input for the location
location = input(&#39;Enter a city name or coordinates (latitude,longitude): &#39;)

# Fetch weather data based on user input
weather_data = fetch_weather_data(location)

# Display the weather information

display_weather_data(weather_data)