from services.terminal import terminal
from services.apiTools import apiTools
from services.jsonTools import jsonTools
from services.WeatherDisplay import WeatherDisplay


def main():
    #city = terminal.getCity()
    city = jsonTools.getCity()
    geo = apiTools.getGeo(city)
    data = apiTools.getWeather(geo)
    




if __name__ == '__main__':
    main()
