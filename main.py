import config
import requests
import matplotlib.pyplot as plt

if __name__ == '__main__':
    def api_call(url):
        response = requests.get(url)
        json = response.json()
        return json


    # Geocoding
    while True:
        city = input("Enter the name of the city: ")
        geocoding_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={config.api_key}"
        geocodes = api_call(geocoding_url)
        try:
            city_lon = geocodes[0]['lon']
            city_lat = geocodes[0]['lat']
            break
        except IndexError:
            print("Couldn't find the city.")

    # Getting weather forecast
    forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?lat={str(city_lat)}&lon={str(city_lon)}&units" \
                   f"=metric&appid={config.api_key}"
    forecast = api_call(forecast_url)

    timestamps = []
    temperatures = []
    rain = []

    for i in range(0, 40):
        timestamp = forecast['list'][i]['dt_txt']
        timestamps.append(timestamp[5:-3])
        temperatures.append((forecast['list'][i]['main']['temp']))
        try:
            rain.append(forecast['list'][i]['rain']['3h'])
        except KeyError:
            rain.append(0.0)

    # Plotting the weather forecast
    plt.title(f"Weather forecast for {city} ({timestamps[0]} to {timestamps[-1]})")
    plt.plot(timestamps, temperatures, color='red')
    plt.xticks(rotation=90)
    plt.bar(timestamps, rain)
    plt.xlabel('Date')
    plt.ylabel("Temperature (Celsius)\nPrecipitation (mm)")
    plt.show()

