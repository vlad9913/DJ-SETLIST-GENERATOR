# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/Programming/Licenta/controller/updatedui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import service.execute as ex

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import numpy as np



class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width,height))
        
        self.axes = fig.add_subplot(211)
        self.axes2 = fig.add_subplot(212)
        super(MplCanvas, self).__init__(fig)

class Worker(QObject):
    finished = pyqtSignal()
    output = pyqtSignal(list)
    rest = pyqtSignal(np.ndarray,np.ndarray,np.ndarray,np.ndarray,np.ndarray,np.ndarray,np.ndarray,np.ndarray,np.ndarray)
    
    def __init__(self,setSize,genres):
        super(Worker,self).__init__()
        self.setSize = setSize
        self.genres = genres

    def run(self):

        output,xenergy,yenergy,yenergyorg,xdance,ydance,ydanceorg,xvalence,yvalence,yvalenceorg=ex.generate_setlist(1000, 20, self.setSize, self.genres)
        self.output.emit(output)
        self.rest.emit(xenergy,yenergy,yenergyorg,xdance,ydance,ydanceorg,xvalence,yvalence,yvalenceorg)
        self.finished.emit()
        
        
        
class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(679, 686)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        mainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("DJ.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setAutoFillBackground(False)
        mainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        mainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_a = QtWidgets.QFrame(self.centralwidget)
        self.frame_a.setGeometry(QtCore.QRect(30, 10, 221, 301))
        self.frame_a.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_a.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_a.setObjectName("frame_a")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame_a)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 80, 160, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_1 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("New Century Schoolbook")
        font.setPointSize(9)
        self.checkBox_1.setFont(font)
        self.checkBox_1.setObjectName("checkBox_1")
        self.verticalLayout.addWidget(self.checkBox_1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("New Century Schoolbook")
        font.setPointSize(9)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("New Century Schoolbook")
        font.setPointSize(9)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("New Century Schoolbook")
        font.setPointSize(9)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("New Century Schoolbook")
        font.setPointSize(9)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout.addWidget(self.checkBox_5)
        self.checkBox_6 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("New Century Schoolbook")
        font.setPointSize(9)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout.addWidget(self.checkBox_6)
        self.checkBox_7 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("New Century Schoolbook")
        font.setPointSize(9)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setObjectName("checkBox_7")
        self.verticalLayout.addWidget(self.checkBox_7)
        self.label = QtWidgets.QLabel(self.frame_a)
        self.label.setGeometry(QtCore.QRect(0, 60, 211, 16))
        font = QtGui.QFont()
        font.setFamily("New Century Schoolbook")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.spinBox = QtWidgets.QSpinBox(self.frame_a)
        self.spinBox.setGeometry(QtCore.QRect(0, 30, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.label_2 = QtWidgets.QLabel(self.frame_a)
        self.label_2.setGeometry(QtCore.QRect(0, 10, 201, 16))
        font = QtGui.QFont()
        font.setFamily("New Century Schoolbook")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_a)
        self.pushButton.setGeometry(QtCore.QRect(70, 270, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(310, 40, 361, 271))
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 20, 201, 16))
        font = QtGui.QFont()
        font.setFamily("New Century Schoolbook")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 100, 211, 131))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("arrow.png"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 520, 651, 131))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 320, 541, 181))
        self.label_6.setScaledContents(False)
        self.label_6.setWordWrap(False)
        self.label_6.setObjectName("label_6")
        self.backgroundImageLabel = QtWidgets.QLabel(self.centralwidget)
        self.backgroundImageLabel.setGeometry(QtCore.QRect(0, -10, 681, 681))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backgroundImageLabel.sizePolicy().hasHeightForWidth())
        self.backgroundImageLabel.setSizePolicy(sizePolicy)
        self.backgroundImageLabel.setText("")
        self.backgroundImageLabel.setPixmap(QtGui.QPixmap("sky.jpg"))
        self.backgroundImageLabel.setObjectName("backgroundImageLabel")
        self.backgroundImageLabel.raise_()
        self.frame_a.raise_()
        self.textEdit.setReadOnly(True)
        self.textEdit.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 679, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.energyWindow = QtWidgets.QMainWindow(mainWindow)
        self.danceWindow = QtWidgets.QMainWindow(mainWindow)
        self.valenceWindow = QtWidgets.QMainWindow(mainWindow)
        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        
        
        self.pushButton.clicked.connect(self.handle_generate_button)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Vlad\'s DJ Setlist Generator"))
        self.checkBox_1.setText(_translate("mainWindow", "Techno"))
        self.checkBox_2.setText(_translate("mainWindow", "Tech House"))
        self.checkBox_3.setText(_translate("mainWindow", "Trance"))
        self.checkBox_4.setText(_translate("mainWindow", "Drum n\' Bass"))
        self.checkBox_5.setText(_translate("mainWindow", "Hardstyle"))
        self.checkBox_6.setText(_translate("mainWindow", "Psytrance"))
        self.checkBox_7.setText(_translate("mainWindow", "Trap"))
        self.label.setText(_translate("mainWindow", "Choose your desired genres:"))
        self.label_2.setText(_translate("mainWindow", "Choose the number of tracks:"))
        self.pushButton.setText(_translate("mainWindow", "Generate"))
        self.label_3.setText(_translate("mainWindow", "Your generated setlist:"))
        self.label_5.setText(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; font-style:italic;\">About this:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">This program is intended to help DJs by generating setlists for them. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">It uses a genetic algorithm to create your setlist, based on trends from 817 other </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">setlists taken from the world\'s most respected DJs such as: Tale of Us, Daft Punk, Solomun, </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Nina Kraviz and many more. The algorithm tries to follow (to a certain degree) three attributes</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">which dictate how a setlist &quot;feels&quot; : energy, danceability and valence. After generating</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">your result, the program will display plots representing each of these attributes.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt; font-weight:600;\"><br /></p></body></html>"))
        self.label_6.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; font-style:italic;\">How to use:</span></p><p><span style=\" font-size:9pt; font-weight:600;\">1. </span><span style=\" font-size:9pt;\">Enter the number of tracks you wish your setlist to have.</span></p><p><span style=\" font-size:9pt; font-weight:600;\">2. </span><span style=\" font-size:9pt;\">Tick the checkboxes representing the desired genres to be included.</span></p><p><span style=\" font-size:9pt; font-weight:600;\">3</span><span style=\" font-size:9pt;\">. Click the &quot;Generate&quot; button.</span></p><p><span style=\" font-size:9pt; font-weight:600;\">4.</span><span style=\" font-size:9pt;\"> Wait between 0:30 - 1:00 minutes</span></p><p><span style=\" font-size:9pt;\">(These times may vary based on your computer and the number of tracks)</span></p><p><span style=\" font-size:9pt; font-weight:600;\">5. </span><span style=\" font-size:9pt;\">Enjoy your setlist! </span></p></body></html>"))


    def handle_generate_button(self):
        genres_array=[]
        
        if self.checkBox_1.isChecked():
            genres_array.append("techno")
        if self.checkBox_2.isChecked():
            genres_array.append("techhouse")
        if self.checkBox_3.isChecked():
            genres_array.append("trance")
        if self.checkBox_4.isChecked():
            genres_array.append("dnb")
        if self.checkBox_5.isChecked():
            genres_array.append("hardstyle")
        if self.checkBox_6.isChecked():
            genres_array.append("psytrance")
        if self.checkBox_7.isChecked():
            genres_array.append("trap")
        
        if len(genres_array)==0:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("")
            msg.setInformativeText('Please select at least one genre!')
            msg.setWindowTitle("Error")
            msg.exec_()
            return
        
        if int(self.spinBox.value())<5:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("")
            msg.setInformativeText('At least 5 songs needed!')
            msg.setWindowTitle("Error")
            msg.exec_()
            return
            
        self.thread = QThread()
        self.worker = Worker(int(self.spinBox.value()), genres_array)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.output.connect(self.insert_into_text_box)
        self.thread.start()
        self.worker.rest.connect(self.show_plots)
        
        #output,xenergy,yenergy,yenergyorg,xdance,ydance,ydanceorg,xvalence,yvalence,yvalenceorg = ex.generate_setlist(1000, 20, int(self.spinBox.value()), genres_array)
        #self.insert_into_text_box(output)
        #self.show_plots(xenergy,yenergy,yenergyorg,xdance,ydance,ydanceorg,xvalence,yvalence,yvalenceorg)
        self.pushButton.setText("Loading")
        self.pushButton.setEnabled(False)
        
        self.thread.finished.connect(
            lambda: (self.pushButton.setEnabled(True),self.pushButton.setText("Generate"))

        )
        
   
    def insert_into_text_box(self,songs_array):
       
        self.textEdit.setText("")
        for i in range(len(songs_array)):
            self.textEdit.append(str(i+1)+". "+songs_array[i]+"\n")


    def show_plots(self,xenergy,yenergy,yenergyorg,xdance,ydance,ydanceorg,xvalence,yvalence,yvalenceorg):
        
        energyplot = MplCanvas(self.energyWindow)
        energyplot.axes.plot(xenergy,yenergy,'r')
        energyplot.axes.title.set_text('Generated Setlist Energy')
        
        energyplot.axes2.plot(xenergy,yenergyorg,'b')
        energyplot.axes2.title.set_text('Perfect (Original) Energy')

        self.energyWindow.setCentralWidget(energyplot)
        
        danceplot = MplCanvas(self.danceWindow)
        danceplot.axes.plot(xdance,ydance,'r')
        danceplot.axes.title.set_text('Generated Setlist Danceability')
        
        danceplot.axes2.plot(xdance,ydanceorg,'b')
        danceplot.axes2.title.set_text('Perfect (Original) Danceability')

        self.danceWindow.setCentralWidget(danceplot)
        
        valenceplot = MplCanvas(self.valenceWindow)
        valenceplot.axes.plot(xvalence,yvalence,'r')
        valenceplot.axes.title.set_text('Generated Setlist Valence')
        
        valenceplot.axes2.plot(xvalence,yvalenceorg,'b')
        valenceplot.axes2.title.set_text('Perfect (Original) Valence')

        self.valenceWindow.setCentralWidget(valenceplot)
        
        self.energyWindow.setWindowTitle("Energy plots")
        self.energyWindow.show()
        self.danceWindow.setWindowTitle("Dance plots")
        self.danceWindow.show()
        self.valenceWindow.setWindowTitle("Valence plots")
        self.valenceWindow.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

