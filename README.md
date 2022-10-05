# WeatherForecast

WeatherForecast is a short Python program utilizing OpenWeatherMapsAPI, which visualizes the weather forecast (temperature and precipitation) for the next 5 days using charts. 

## Installation

This program relies on following libraries, install them using pip before running:

- MatPlotLib
- requests
- json

Download the project files, or clone them directly by using:

```bash
gh repo clone Adrian2901/WeatherForecast
```

Since this script is using OpenWeatherMapsAPI, you will need to enter your own API key. To do that, get the key from [OpenWeatherMaps's website](https://openweathermap.org/api), and edit the empty value in config.py.

Then you'll be able to run the main.py script through Command Prompt/Terminal:
```bash
python main.py
```


## Usage

After running the program, you'll be asked to enter the name of the city, of which weather forecast you'd like to see. Whenever possible, you should enter the name in English. After that the script will open the forecast in a new window.

