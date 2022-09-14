class terminal:    
    def getCity():
        city = input('What city would you like to check?: \n')
        return city

    def getSelection():
        msg = "Enter Your Choice:\n1)Get Current Temperature"
        print(msg)
        selection = input()
        return selection