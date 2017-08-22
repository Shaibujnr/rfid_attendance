import wx
from controls import Window
from dbhelper import Dbapi
app = wx.App()


if __name__ == "__main__":
    Dbapi.configure()
    Window("Attendance").run()
