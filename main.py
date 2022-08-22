import sys
import requests
from PyQt5 import QtGui
from PyQt5.QtCore import QTimer, QTime, QDate
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QSplashScreen
from frontend import Ui_MainWindow

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask) 
        self.ui.pushButton_3.clicked.connect(self.steps)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie =  QtGui.QMovie("Assests/Normal_Screen.webp")  
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        

    def showTime(self):
        current_time=QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

    def steps(self):
        url = "https://v1.nocodeapi.com/zetaknight/fit/GpWLJGwidrAOkBVc/aggregatesDatasets?dataTypeName=steps_count,active_minutes,calories_expended&timePeriod=today"
        params = {}
        r = requests.get(url = url, params = params)
        result = r.json()
        steps=str(result['steps_count'][0]['value'])
        active=str(result['active_minutes'][0]['value'])
        calories=str(result['calories_expended'][0]['value'])
        self.ui.textBrowser_3.setText(steps)
        self.ui.textBrowser_7.setText(active)
        self.ui.textBrowser_8.setText(calories)

        



app = QApplication(sys.argv)
baymax = Main()
baymax.show()
exit(app.exec_())