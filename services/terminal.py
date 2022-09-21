#from consolemenu import *
#from consolemenu.items import *

class terminal:    

    def greeting():
        print('-'*30)
        print(('-'*13) + ' W E A T H E R  A P P '+ ('-' *13))
        print("Enter A City: ")
        city = input()
        return city


    def menu(city):
        print('\nCity Selected: ' + city)
        print('\n1. Get Current Temperature')
        print('2. Get Conditions')
        print('3. ')
        print('4. Change City')
        print('Q. Exit')
        print('-'*48)
        selection = input()
        return selection


        

    def notExist():
        print("The city you entered does not exist")
        print("Enter a new city name: ")
        city = input()
        return city