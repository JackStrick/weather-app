from services.jsonTools import jsonTools

class WeatherDisplay:
    def currentWeather(weatherDict, city):
        msg = "The current temperature in {} is: "
        msg = msg.format(city)
        print(msg)

        curTemp = round(weatherDict['main']['temp'])
        msg = "{} degrees fahrenheit\n"
        msg = msg.format(curTemp)
        print(msg)

        


