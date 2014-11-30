__author__ = 'hkapadia'

import threading
import time
from scrapper import mainbackend


class BackgroundTimer(threading.Thread):
    #def __init__(self):
     #   threading.Thread.__init__(self)
    def run(self):
        while 1:
            mainbackend()
            print "Done scrapping twitter. Going to sleep for 1 min"
            time.sleep(60)

