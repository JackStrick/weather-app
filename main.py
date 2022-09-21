from symbol import import_from
from time import sleep
from services.terminal import terminal
from services.apiTools import apiTools
from services.jsonTools import jsonTools
from services.WeatherDisplay import WeatherDisplay


def main():
    #city = terminal.getCity()
    selection = 1
    city = terminal.greeting()
    geo = apiTools.getGeo(city) #gets the coordinates of the selected location / checks if the city exists

    while (geo == 0):
        city = terminal.notExist()
        geo = apiTools.getGeo(city)

    #city = jsonTools.getCity() #retrieves the city from a json file
    #selection = terminal.menu(city)
    data = apiTools.getWeather(geo) #returns weather data dictionary

    while selection is not 'Q':
        selection = terminal.menu(city)
        
        if (selection == 'Q'):
            print('Good Bye')
            exit()

        elif (selection == '1'):
            WeatherDisplay.currentWeather(data,city) #displays the current temperature
        
        elif (selection == '2'):
            WeatherDisplay.conditions(data, city) #Displays current conditins
        #elif (selection == '4'):
            #city = terminal.greeting()
        else:
            break
    


    
    
    




if __name__ == '__main__':
    main()
