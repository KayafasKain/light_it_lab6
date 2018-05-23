from datetime import datetime
import logging
import sys

class Greeter():

    def greet(self, name):
        name = name.strip()
        name = "Hello, " + name

        name = name.capitalize()

        logging.warning(name)

        return name

    def greet_time(self, name):

        name = name.strip()

        current_time = datetime.now()

        if current_time > 6 and current_time < 12:
            name = "Good morning, " + name
            logging.warning(name)
        elif current_time > 18 and current_time < 22:
            name = "Good evening, " + name
            logging.warning(name)
        elif current_time > 22 :
            name = "Good night, " + name
            logging.warning(name)
            
        name = name.capitalize()
        logging.warning(name)

        return name

lol = Greeter()
lol.greet("lol")