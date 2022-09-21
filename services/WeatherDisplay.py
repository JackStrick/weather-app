from services.jsonTools import jsonTools

class WeatherDisplay:
    def currentWeather(weatherDict, city):
        print('\n-'*5)
        print('-'*48)
        msg = "The current temperature in {} is: "
        msg = msg.format(city)
        print(msg)
        curTemp = round(weatherDict['main']['temp'])
        msg = "{} degrees fahrenheit"
        msg = msg.format(curTemp)
        print(msg)
        print('-'*48)

    def conditions(weatherDict, city):
        print('\n-'*5)
        print('-'*48)
        condit = weatherDict['weather'][0]['description']
        condit = condit.capitalize()
        humidity = weatherDict['main']['temp']
        msg = "The current conditions in {}: \n{} with {}% humidity"
        msg = msg.format(city, condit, humidity)
        print(msg)
        print('-'*48)

        


