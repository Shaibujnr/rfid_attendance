from threading import Thread,Event
from wx.lib.pubsub import pub as Publisher
import wx
import serial
import configparser

config = configparser.ConfigParser()
config.read("dbconfig.ini")
arduino_section = config["Arduino"]
port = arduino_section.get("port",'/dev/ttyUSB0')

class BackThread(Thread):
    def __init__(self):
        super(BackThread,self).__init__()
        self.ser = serial.Serial(port,9600)
        self._stop_event = Event()
        self.start()

    def run(self):
        while True:
            s = self.ser.readline().decode()
            s = s.strip()
            if s:
                wx.CallAfter(self.postThis,s)

    def postThis(self,uid):
        Publisher.sendMessage("Update",uid=uid)

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()


