from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets, QtGui, QtCore

from PyQt5.QtCore import pyqtSlot, pyqtSignal, QThread
import weather_getter
import sys

import glob
import random
import time

class WeatherFetchWorker(QThread):
    sender = pyqtSignal(dict)
    finisher = pyqtSignal()

    def __init__(self, loc):
        super().__init__()
        self.loc = loc

    def run(self):
        code, current_weather = weather_getter.generateRequest()

        result = {
            "wd": current_weather["weather"][0]["description"],
            "ct": current_weather["main"]["temp"],
            "ip": f'sources\\image\\{current_weather["weather"][0]["icon"]}.png',
            "ch": current_weather['main']['humidity'],
            'cw': (current_weather['wind']['speed'], current_weather['wind']['deg']),
            'maxt': current_weather['main']['temp_max'],
            'mint': current_weather['main']['temp_min']
        }
        self.sleep(random.randint(1, 3))
        self.finisher.emit()
        self.sleep(1)
        self.sender.emit(result)

class MainWinowIconChanger(QThread):
    def __init__(self, windowInstance):
        super().__init__()
        self.running = True
        self.icolist = glob.glob("sources\\image\\*.png")
        self.windowInstance = windowInstance

    def run(self):
        while self.running:
            for ico in self.icolist:
                print(self.icolist)
                self.windowInstance.setWindowIcon(QtGui.QIcon(ico))
                self.windowInstance.mainPictureLabel.setPixmap(QtGui.QPixmap(ico))
                self.msleep(random.randint(1, 100))

    def finish(self):
        self.running = False

class Sleeper(QThread):
    def run(self):
        self.msleep(100)


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        font = QtGui.QFont()
        font.setFamily("나눔바른고딕 UltraLight")

        self.resize(989, 689)
        self.centralwidget = QtWidgets.QWidget(self)

        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)

        self.ParentGridLayout = QtWidgets.QGridLayout()

        self.letfTopGrid = QtWidgets.QVBoxLayout()
        self.letfTopGrid.setContentsMargins(-1, -1, -1, 0)

        self.mainPictureLabel = QtWidgets.QLabel(self.centralwidget)
        self.mainPictureLabel.setMinimumSize(QtCore.QSize(0, 290))
        self.mainPictureLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.letfTopGrid.addWidget(self.mainPictureLabel)
        self.mainWeatherDesLabel = QtWidgets.QLabel(self.centralwidget)

        self.mainWeatherDesLabel.setFont(font)
        self.mainWeatherDesLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.letfTopGrid.addWidget(self.mainWeatherDesLabel)
        self.ParentGridLayout.addLayout(self.letfTopGrid, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.ParentGridLayout, 0, 0, 1, 1)
        self.rightTop = QtWidgets.QVBoxLayout()

        self.mainTempLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("나눔바른고딕 Light")
        font.setPointSize(35)
        self.mainTempLabel.setFont(font)
        self.mainTempLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.rightTop.addWidget(self.mainTempLabel)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()

        self.mainAdditionalInfoLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("나눔바른고딕 UltraLight")
        font.setPointSize(12)
        self.mainAdditionalInfoLabel.setFont(font)
        self.mainAdditionalInfoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mainAdditionalInfoLabel.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.mainAdditionalInfoLabel)
        self.mainHiLowTempLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("나눔바른고딕 UltraLight")
        font.setPointSize(12)
        self.mainHiLowTempLabel.setFont(font)
        self.mainHiLowTempLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.mainHiLowTempLabel)
        self.rightTop.addLayout(self.horizontalLayout_3)
        self.gridLayout_2.addLayout(self.rightTop, 0, 1, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 300))
        self.scrollArea.setWidgetResizable(True)

        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 965, 298))

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)

        self.verticalLayout_3 = QtWidgets.QVBoxLayout()

        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()

        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()

        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.addWidget(self.scrollArea, 1, 0, 1, 2)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)

        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        self.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle("현재 날씨 - 날씨 정보를 가져오는 중입니다")
        self.mainPictureLabel.setText("사진이 들어갈 자리")
        self.mainWeatherDesLabel.setText("날씨 정보를 가져오는 중입니다")
        self.mainTempLabel.setText("날씨 정보를 가져오는 중입니다")
        self.mainAdditionalInfoLabel.setText("날씨 정보를 가져오는 중입니다")
        self.mainHiLowTempLabel.setText("날씨 정보를 가져오는 중입니다")
        self.initialize()

    def initialize(self):
        self.setEnabled(False)

        worker = WeatherFetchWorker('Anyang-si,KR')
        worker.sender.connect(self.displayWeather)
        worker.finisher.connect(self.finishChanger)
        worker.start()

        self.changeWorker = MainWinowIconChanger(self)
        self.changeWorker.start()

    @pyqtSlot(dict)
    def displayWeather(self, res):
        print(res)

        self.setWindowTitle("현재 날씨 - {}".format(res['wd']))
        self.mainPictureLabel.setPixmap(QtGui.QPixmap(res['ip']))
        self.mainWeatherDesLabel.setText(res['wd'])
        self.mainTempLabel.setText("{}°C".format(res['ct']))
        self.mainAdditionalInfoLabel.setText("습도 {}%\n바람 {} km/h @ {}".format(res['ch'], res['cw'][0], res['cw'][1]))
        self.mainHiLowTempLabel.setText("{}°C / {}°C".format(res['maxt'], res['mint']))
        self.setWindowIcon(QtGui.QIcon(res['ip']))

        self.setEnabled(True)

    @pyqtSlot()
    def finishChanger(self):
        self.changeWorker.finish()

app = QApplication(sys.argv)
w = Ui_MainWindow()
sys.exit(app.exec_())
