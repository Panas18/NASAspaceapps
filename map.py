import turtle
#import urllib.request
#import json
#from bs4 import BeautifulSoup 
#url = 'http://192.168.43.51'

while True:
#    response = urllib.request.urlopen(url)
#  result = json.loads(response.read())
#    print(result)
#    option = (result/400)*10

    image = r"C:\Users\hp\Desktop\New folder\Map.gif"
    screen = turtle.Screen()
    screen.bgpic(image)
    screen.setup(720,360)
    screen.setworldcoordinates(-180,-90,180,90)
    turtle.penup()
    turtle.goto(-5,-30)
    def switch():
        option = int(input(" your option : "))
        def zero():
            turtle.dot(50,"#7FFFD4")

        def one():
            turtle.dot(50,"#76EEC6")

        def two():
            turtle.dot(50,"	#66CDAA")

        def three():
            turtle.dot(50,"	#458B74	")

        def four():
            turtle.dot(50,"#7FFF00")

        def five():
            turtle.dot(50,"	#76EE00	")

        def six():
            turtle.dot(50,"	#FF4040")

        def seven():
            turtle.dot(50,"	#EE3B3B")

        def eight():
            turtle.dot(50,"	#CD3333")

        def nine():
            turtle.dot(50,"#8B2323")

    # If user enters invalid option then this method will be called 
        def default():
            print("Invalid")

    # Dictionary Mapping
        dict = {
            0: zero,
            1 : one,
            2 : two,
            3 : three,
            4 : four,
            5 : five,
            6 : six,
            7 : seven,
            8 : eight,
            9 : nine,

        }
        dict.get(option,default)() # get() method returns the function matching the argument

    switch() 
turtle.mainloop()