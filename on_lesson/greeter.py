from datetime import datetime
import logging
import sys

class Greeter():
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)     

    def greet(self, name):
        name = name.strip()
        name = "Hello, " + name

        name = name.capitalize()

        self.logger.info(name)

        return name

    def greet_time(self, name):

        name = name.strip()

        current_time = datetime.now()

        if current_time > 6 and current_time < 12:
            name = "Good morning, " + name
            self.logger.info(name)
        elif current_time > 18 and current_time < 22:
            name = "Good evening, " + name
            self.logger.info(name)
        elif current_time > 22 :
            name = "Good night, " + name
            self.logger.info(name)
            
        name = name.capitalize()
        

        return name
