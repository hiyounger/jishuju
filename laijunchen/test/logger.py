# -*- encoding -*-
from laijunchen import config
class Logger():

    @classmethod
    def info(cls, msg):
        print("[INFO] " + str(msg))

    @classmethod
    def debug(cls, msg):
        if config.DEBUG == True:
            print("[DEBUG] " + str(msg))

    @classmethod
    def error(cls, msg):
        print("[ERROR] " + str(msg))