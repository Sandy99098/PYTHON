import requests
import tkinter as tk
from PIL import Image, ImageTk
import io  # Import the io module

def fetch_weather():
    # Get weather data from OpenWeatherMap API
    api_key = 'enter your api'
    latitude = '28.2139'  # Latitude of Pokhara, Nepal
    longitude = '83.9922'  # Longitude of Pokhara, Nepal
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()

    # Extract weather information
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']
    icon_name = data['weather'][0]['icon']

    # Update labels with weather information
    temperature_label.config(text=f'Temperature: {temperature}°C')
    humidity_label.config(text=f'Humidity: {humidity}%')
    description_label.config(text=f'Description: {description.capitalize()}')

    # Load weather icon
    icon_url = f'http://openweathermap.org/img/wn/{icon_name}.png'
    icon_data = requests.get(icon_url).content
    image = Image.open(io.BytesIO(icon_data))  # Use io module to open image
    photo = ImageTk.PhotoImage(image)
    icon_label.config(image=photo)
    icon_label.image = photo

# Create main window
root = tk.Tk()
root.title('Weather App')

# Create labels for weather information
temperature_label = tk.Label(root, text='', font=('Helvetica', 18))
humidity_label = tk.Label(root, text='', font=('Helvetica', 18))
description_label = tk.Label(root, text='', font=('Helvetica', 18))

# Create label for weather icon
icon_label = tk.Label(root)

# Create button to fetch weather data
fetch_button = tk.Button(root, text='Fetch Weather', command=fetch_weather, font=('Helvetica', 14))

# Layout widgets using grid
temperature_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky='w')
humidity_label.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky='w')
description_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky='w')
icon_label.grid(row=0, column=2, rowspan=3, padx=10, pady=5)
fetch_button.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

# Run the Tkinter event loop
root.mainloop()
