from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
import sys


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
        self.setWindowTitle("현재 날씨 - 대체로 맑음")
        self.mainPictureLabel.setText("사진이 들어갈 자리")
        self.mainWeatherDesLabel.setText("대체로 맑음")
        self.mainTempLabel.setText("10°C")
        self.mainAdditionalInfoLabel.setText("습도 80%\n바람 0.3 km/h @ 20")
        self.mainHiLowTempLabel.setText("7°C / 19°C")


app = QApplication(sys.argv)
w = Ui_MainWindow()
sys.exit(app.exec_())
