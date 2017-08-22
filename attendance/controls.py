import wx
from dbhelper import Dbapi
from models import Student
from background import BackThread
from wx.lib.pubsub import pub as Publisher
from wx.lib.scrolledpanel import ScrolledPanel


class ControlPanel(wx.Panel):
    def __init__(self,parent):
        super(ControlPanel,self).__init__(parent)
        self.initUI()

    def __unicode__(self):
        return "Control Panel"

    def initUI(self):
        registerButton = wx.ToggleButton(self, 2, "Register")
        attendanceButton = wx.ToggleButton(self, 4, "Attendance")
        settingsButton = wx.ToggleButton(self,6,"Settings")
        manageButton = wx.ToggleButton(self,8,"Manage")

        controlPanelVerticalSizer = wx.BoxSizer(wx.VERTICAL)
        controlPanelVerticalSizer.Add(registerButton, 2, wx.ALL | wx.EXPAND)
        controlPanelVerticalSizer.Add(attendanceButton, 2, wx.ALL | wx.EXPAND)
        controlPanelVerticalSizer.Add(settingsButton, 2, wx.ALL | wx.EXPAND)
        controlPanelVerticalSizer.Add(manageButton,2,wx.ALL|wx.EXPAND)

        self.SetSizer(controlPanelVerticalSizer)

class AttendancePanel(ScrolledPanel):
    def __init__(self,parent):
        super(AttendancePanel,self).__init__(parent)
        self.initUI()
        self.SetBackgroundColour("#fff")
        self.SetAutoLayout(1)
        self.SetupScrolling()

    def __unicode__(self):
        return "Attendance Panel"

    def initUI(self):
        atSizer = wx.BoxSizer(wx.VERTICAL)
        self.atSizer = atSizer
        self.SetSizer(atSizer)
        # self.tc = wx.StaticText(self)
        # self.atSizer.Add(self.tc)


    def updateUi(self,uid):
        self.atSizer.Add(wx.StaticText(self,label=uid))
        self.Scroll(self.GetClientSize()[0], -1)
        self.Layout()
        self.SetAutoLayout(1)
        self.SetupScrolling()


class SettingsPanel(wx.Panel):
    def __init__(self,parent):
        super(SettingsPanel,self).__init__(parent)
        self.initUI()
        self.SetBackgroundColour("#fff")

    def __unicode__(self):
        return "Settings Panel"

    def initUI(self):
        settingsSizer = wx.BoxSizer(wx.VERTICAL)
        dbNameHBox = wx.BoxSizer(wx.HORIZONTAL)
        dbNameEntryLabel = wx.StaticText(self, label="Database Name", id=1000)
        dbNameEntryBox = wx.TextCtrl(self, id=2000)
        self.dbnBox = dbNameEntryBox
        dbNameHBox.Add(dbNameEntryLabel, 2, wx.ALL, 5)
        dbNameHBox.Add(dbNameEntryBox, 5, wx.ALL, 5)

        tbNameHBox = wx.BoxSizer(wx.HORIZONTAL)
        tbNameEntryLabel = wx.StaticText(self, label="Table Name", id=3000)
        tbNameEntryBox = wx.TextCtrl(self, id=4000)
        self.tbnBox = tbNameEntryBox
        tbNameHBox.Add(tbNameEntryLabel, 2, wx.ALL, 5)
        tbNameHBox.Add(tbNameEntryBox, 5, wx.ALL, 5)

        portHBox = wx.BoxSizer(wx.HORIZONTAL)
        portEntryLabel = wx.StaticText(self, label="Connection Port", id=5000)
        portEntryBox = wx.TextCtrl(self, id=6000)
        self.portBox = portEntryBox
        portHBox.Add(portEntryLabel, 2, wx.ALL, 5)
        portHBox.Add(portEntryBox, 5, wx.ALL, 5)



        actionHBox = wx.BoxSizer(wx.HORIZONTAL)
        buttonDone = wx.Button(self, 30, "Done")
        self.btnDone = buttonDone
        actionHBox.Add(buttonDone, 2, wx.ALL, 5)


        settingsSizer.Add(dbNameHBox, 1, wx.ALL, 4)
        settingsSizer.Add(tbNameHBox, 1, wx.ALL, 4)
        settingsSizer.Add(portHBox, 1, wx.ALL, 4)
        settingsSizer.Add(actionHBox, 1, wx.ALL, 4)

        self.SetSizer(settingsSizer)


class RegisterPanel(wx.Panel):
    def __init__(self,parent):
        super(RegisterPanel,self).__init__(parent)
        self.initUI()
        self.SetBackgroundColour("#fff")

    def initUI(self):
        # registerPanel = wx.Panel(None)
        registerPanelBox = wx.BoxSizer(wx.VERTICAL)
        lastNameHBox = wx.BoxSizer(wx.HORIZONTAL)
        lastNameEntryLabel = wx.StaticText(self, label="Last Name", id=100)
        lastNameEntryBox = wx.TextCtrl(self, id=200)
        self.lnBox = lastNameEntryBox
        lastNameHBox.Add(lastNameEntryLabel, 2, wx.ALL, 5)
        lastNameHBox.Add(lastNameEntryBox, 5, wx.ALL, 5)

        firstNameHBox = wx.BoxSizer(wx.HORIZONTAL)
        firstNameEntryLabel = wx.StaticText(self, label="First Name",id=300)
        firstNameEntryBox = wx.TextCtrl(self,id=400)
        self.fnBox = firstNameEntryBox
        firstNameHBox.Add(firstNameEntryLabel, 2, wx.ALL, 5)
        firstNameHBox.Add(firstNameEntryBox, 5, wx.ALL, 5)

        matricHBox = wx.BoxSizer(wx.HORIZONTAL)
        matricEntryLabel = wx.StaticText(self, label="Matric Number",id=500)
        matricEntryBox = wx.TextCtrl(self,id=600)
        self.mnBox = matricEntryBox
        matricHBox.Add(matricEntryLabel, 2, wx.ALL, 5)
        matricHBox.Add(matricEntryBox, 5, wx.ALL, 5)

        cardHBox = wx.BoxSizer(wx.HORIZONTAL)
        cardEntryLabel = wx.StaticText(self, label="Card Id",id=700)
        cardEntryBox = wx.TextCtrl(self,id=800)
        self.cBox = cardEntryBox
        cardHBox.Add(cardEntryLabel, 2, wx.ALL, 5)
        cardHBox.Add(cardEntryBox, 5, wx.ALL, 5)

        actionHBox = wx.BoxSizer(wx.HORIZONTAL)
        buttonDone = wx.Button(self, 10,"Register")
        self.btnDone = buttonDone
        actionHBox.Add(buttonDone, 2, wx.ALL, 5)


        registerPanelBox.Add(lastNameHBox, 1, wx.ALL, 4)
        registerPanelBox.Add(firstNameHBox, 1, wx.ALL, 4)
        registerPanelBox.Add(matricHBox, 1, wx.ALL, 4)
        registerPanelBox.Add(cardHBox,1,wx.ALL,4)
        registerPanelBox.Add(actionHBox, 1, wx.ALL, 4)


        self.SetSizer(registerPanelBox)

class ManagePanel(ScrolledPanel):
    def __init__(self,parent):
        super(ManagePanel,self).__init__(parent)
        self.registered_students = []
        self.buttons = []
        self.initUI();
        self.SetBackgroundColour("#fff")
        self.SetAutoLayout(1)
        self.SetupScrolling()


    def initUI(self):
        self.registered_students = Dbapi.fetch_students()
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.vbox)
        for student in self.registered_students:
            hbox = wx.BoxSizer(wx.HORIZONTAL)
            label = wx.StaticText(self,label="%s %s %s %s"%(student.last_name,
                                                            student.first_name,
                                                            student.matric_number,
                                                            student.uid))
            button = wx.Button(self,99,"Delete",name=student.uid)
            self.buttons.append(button)
            hbox.Add(label,6,wx.ALL,5)
            hbox.Add(button,2,wx.ALL,5)
            self.vbox.Add(hbox,2,wx.ALL,3)

    def refresh(self):
        self.Refresh()


class Window(wx.Frame):
    def __init__(self,title):
        super(Window,self).__init__(None, -1, title, style=wx.MINIMIZE_BOX | wx.CLOSE_BOX, size=(700, 300))

        self.present_students = []
        self.back_thread = BackThread()
        self.current = None
        self.initUI()
        self.controlRegisterButton = self.FindWindowById(2)
        self.controlAttendanceButton = self.FindWindowById(4)
        self.controlSettingsButton = self.FindWindowById(6)
        self.controlManageButton = self.FindWindowById(8)

        self.lnBox = None
        self.fnBox = None
        self.mBox = None
        self.cBox = None

        self.settingsDone = self.FindWindowById(30)
        self.settingsDbname = self.FindWindowById(2000)
        self.settingsTbname = self.FindWindowById(4000)
        self.settingsPort = self.FindWindowById(6000)
        Publisher.subscribe(self.updateAttendance, "Update")
        self.Center()
        self.Show()


    def initUI(self):
        self.mainPanel = wx.Panel(self, -1)
        self.controlPanel = ControlPanel(self.mainPanel)
        # self.controlPanel.SetBackgroundColour("#bbccdd")
        self.contentPanel = wx.Panel(self.mainPanel)
        wx.StaticText(self.contentPanel,-1,"Attendance System By me")


        self.mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.mainSizer.Add(self.controlPanel, 2, wx.ALL | wx.EXPAND, 10)
        self.mainSizer.Add(self.contentPanel, 6, wx.ALL | wx.EXPAND, 10)


        self.mainPanel.SetSizer(self.mainSizer)
        self.Bind(wx.EVT_TOGGLEBUTTON, handler=self.onRegisterClicked, id=2)
        self.Bind(wx.EVT_TOGGLEBUTTON, handler=self.onAttendanceClicked, id=4)
        self.Bind(wx.EVT_TOGGLEBUTTON, handler=self.onSettings, id=6)
        self.Bind(wx.EVT_TOGGLEBUTTON,handler=self.onManageClicked,id=8)
        self.Bind(wx.EVT_BUTTON, handler=self.onSet, id=30)
        self.Bind(wx.EVT_BUTTON,handler=self.onDelete,id=99)

    def onDelete(self,e):
        Dbapi.unregister_student(e.GetEventObject().GetName())
        self.switchTo(4)

    def onManageClicked(self,e):
        self.switchTo(4)

    def onRegisterClicked(self,e):
        self.switchTo(1)

    def onAttendanceClicked(self,e):
        self.switchTo(2)

    def onRegister(self,e):
        ln = self.lnBox.GetValue() or None
        fn = self.fnBox.GetValue() or None
        mn = self.mBox.GetValue() or None
        cn = self.cBox.GetValue() or None
        ns = Student(cn,ln,fn,mn) or None
        try:
            Dbapi.register_student(ns)
            wx.MessageDialog(None,"Student Sucessfully Registered",
                             "Success",
                             wx.OK|wx.ICON_INFORMATION).ShowModal()
        except:
            wx.MessageDialog(None,
                             """
                             Unable to Register Student
                             Due to one or more of the following reasons
                             1) Student already Exists in Database
                             2) Card has already been assigned 
                                to another student in the database
                             3) Matric Number already exists in database
                             4) Not all form fields were filled
                             """,
                             "Error",
                             wx.OK | wx.ICON_ERROR).ShowModal()

    def onSettings(self,e):
        self.switchTo(3)

    def onSet(self,e):
        try:
            Dbapi.set_config(self.settingsDbname.GetValue(),
                        self.settingsTbname.GetValue(),
                        "Last Name", "First Name", "Matric Number", "UID")
            wx.MessageDialog(None, 'settings', 'Done',
                                wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION).ShowModal()
        except:
            wx.MessageDialog(None, "Settings not stored", "Error", wx.OK | wx.ICON_ERROR).ShowModal()

    def switchTo(self,panel):
        replacable_child = self.mainSizer.GetChildren()[1].GetWindow()
        if panel == 1:
            r = RegisterPanel(self.mainPanel)
            self.current = r
            self.lnBox = r.lnBox
            self.fnBox = r.fnBox
            self.cBox = r.cBox
            self.mBox = r.mnBox
            self.Bind(wx.EVT_BUTTON,self.onRegister,r.btnDone)
            self.mainSizer.Replace(replacable_child,r )
            self.controlRegisterButton.SetValue(True)
            self.controlAttendanceButton.SetValue(False)
            self.controlSettingsButton.SetValue(False)
            self.controlManageButton.SetValue(False)
        elif panel == 2:
            a = AttendancePanel(self.mainPanel)
            self.att = a
            self.current = a
            self.mainSizer.Replace(replacable_child,a)
            self.controlRegisterButton.SetValue(False)
            self.controlAttendanceButton.SetValue(True)
            self.controlSettingsButton.SetValue(False)
            self.controlManageButton.SetValue(False)
            for stu in self.present_students:
                self.att.updateUi("%s %s  %s attended" % (stu.last_name, stu.first_name, stu.matric_number))
        elif panel == 3:
            s = SettingsPanel(self.mainPanel)
            self.current = s
            self.settingsDbname = s.dbnBox
            self.settingsTbname = s.tbnBox
            self.settingsPort = s.portBox
            self.Bind(wx.EVT_BUTTON,self.onSet,s.btnDone)
            self.mainSizer.Replace(replacable_child,s)
            self.controlRegisterButton.SetValue(False)
            self.controlAttendanceButton.SetValue(False)
            self.controlSettingsButton.SetValue(True)
            self.controlManageButton.SetValue(False)
        elif panel == 4:
            m = ManagePanel(self.mainPanel)
            self.current = m
            self.mainSizer.Replace(replacable_child,m)
            self.controlSettingsButton.SetValue(False)
            self.controlAttendanceButton.SetValue(False)
            self.controlRegisterButton.SetValue(False)
            self.controlManageButton.SetValue(True)
        self.mainSizer.Layout()

    def updateAttendance(self,uid):
        if type(self.current) == AttendancePanel:
            print("we are here")
            if uid == "Approximate your card to the reader...":
                self.att.updateUi("Swipe card over reader")
            else:
                print(uid)
                print(self.present_students)
                student = Dbapi.get_student_by_uid(uid)
                if student:
                    for stu in self.present_students:
                        if stu.uid == uid:
                            wx.MessageDialog(None, "Your Attendance has already been taken", "Info",
                                             wx.OK | wx.ICON_INFORMATION).ShowModal()
                            return

                    self.present_students.append(student)
                    self.att.updateUi(
                        "%s %s  %s attended" % (student.last_name, student.first_name, student.matric_number))
                else:
                    wx.MessageDialog(None, "Student Not Registered, Please Register",
                                     "Error",
                                     wx.OK | wx.ICON_ERROR).ShowModal();
                    return
        elif type(self.current) == RegisterPanel:
            # print("we are not not")
            if uid == "Approximate your card to the reader...":
                uid = "swipe card"
            self.cBox.SetValue(uid)

    def run(self):
        app = wx.App()
        app.MainLoop()