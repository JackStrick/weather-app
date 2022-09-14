from services.terminal import terminal
from services.apiTools import apiTools
from services.jsonTools import jsonTools
from services.WeatherDisplay import WeatherDisplay


def main():
    #city = terminal.getCity()
    city = jsonTools.getCity() #retrieves the city from a json file
    geo = apiTools.getGeo(city) #gets the coordinates of the selected location
    data = apiTools.getWeather(geo) #returns weather data dictionary
    

    selection = 1
    while selection is not 0:
        selection = terminal.getSelection()
        
        if (selection == '0'):
            break

        elif (selection == '1'):
            WeatherDisplay.currentWeather(data,city) #displays the current temperature
        else:
            break
    


    
    
    




if __name__ == '__main__':
    main()
