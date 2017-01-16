# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Cam.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sys
import glob
import serial
import time

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

####################################################################
####   This Function Lists All Available Serial Ports
####################################################################
def serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

serial_values = [0,0,0,0,0,0]
ser_port = 'COM0'    
ser = serial.Serial()
##################################################################
## UI Objects and methods
##################################################################
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(580, 385)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 60, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 180, 46, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(40, 220, 46, 13))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(120, 60, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 100, 113, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 140, 113, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 180, 113, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 220, 113, 20))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 310, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 310, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(380, 310, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(430, 70, 81, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(335, 70, 61, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(330, 140, 75, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(450, 140, 75, 23))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.progressBar = QtGui.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(320, 230, 241, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        #### Add Items to ComboBox #####
        #ports = ['COM3', 'COM4',  'COM5']
        ser_ports = serial_ports()
        #self.comboBox.addItems(ports)
        self.comboBox.addItems(ser_ports)
        ################################
        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_5.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_4.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_3.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_2.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit.clear)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.progressBar.reset)
        QtCore.QObject.connect(self.lineEdit, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.progressBar.reset)
        QtCore.QObject.connect(self.lineEdit_2, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.progressBar.reset)
        QtCore.QObject.connect(self.lineEdit_3, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.progressBar.reset)
        QtCore.QObject.connect(self.lineEdit_4, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.progressBar.reset)
        QtCore.QObject.connect(self.lineEdit_5, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.progressBar.reset)
        #################################
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.load_values)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.send_values)
        ################################
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Cam1", None))
        self.label_2.setText(_translate("Form", "Cam2", None))
        self.label_3.setText(_translate("Form", "Cam3", None))
        self.label_4.setText(_translate("Form", "Cam4", None))
        self.label_5.setText(_translate("Form", "Cam5l", None))
        self.pushButton.setText(_translate("Form", "Load", None))
        self.pushButton_2.setText(_translate("Form", "Reset", None))
        self.pushButton_3.setText(_translate("Form", "Start", None))
        self.label_6.setText(_translate("Form", "COM Port:", None))
        self.pushButton_4.setText(_translate("Form", "Open", None))
        self.pushButton_5.setText(_translate("Form", "Close", None))

    def load_values(self):
        serial_values[1] = self.lineEdit.text()
        serial_values[2] = self.lineEdit_2.text()
        serial_values[3] = self.lineEdit_3.text()
        serial_values[4] = self.lineEdit_4.text()
        serial_values[5] = self.lineEdit_5.text()
        print serial_values[1]
        print serial_values[2]
        print serial_values[3]
        print serial_values[4]
        print serial_values[5]
        ser_port = str(self.comboBox.currentText())
        print ser_port

    def send_values(self):
        serial_values[1] = self.lineEdit.text()
        serial_values[2] = self.lineEdit_2.text()
        serial_values[3] = self.lineEdit_3.text()
        serial_values[4] = self.lineEdit_4.text()
        serial_values[5] = self.lineEdit_5.text()
        print "Sending Values"
        print serial_values[1]
        print serial_values[2]
        print serial_values[3]
        print serial_values[4]
        print serial_values[5]
        self.progressBar.setValue(0)
        #ser.write(serial_values[1])
        time.sleep(0.2)
        self.progressBar.setValue(20)
        #ser.write(serial_values[2])
        time.sleep(0.2)
        self.progressBar.setValue(40)
        #ser.write(serial_values[3])
        time.sleep(0.2)
        self.progressBar.setValue(100)
        #ser.write(serial_values[4])
        

    def open_port(self):
        ser = serial.Serial(ser_port,9600,timeout=1)
        

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

