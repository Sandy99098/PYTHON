import requests

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
api_key = 'enter your api '
latitude = '28.2139'  # Latitude of pokhara, Nepal
longitude = '83.9922'  # Longitude of pokhara, Nepal
url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric'

response = requests.get(url)
print(response.content)
data = response.json()

if response.status_code == 200:
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']
    print(f'Temperature: {temperature}°C')
    print(f'Humidity: {humidity}%')
    print(f'Description: {description}')
else:
    print('Failed to fetch weather data')
