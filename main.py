

from getBudget import currentBudget, path
import os
import time
dataDir2='data'
filename2='records.txt'
path2=os.path.join(os.getcwd(), dataDir2, filename2)


#print(path)



from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(996, 820)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(50, 130, 431, 151))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(26)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(50, 210, 661, 161))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(26)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(50, 300, 721, 151))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(26)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(50, 380, 721, 151))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(26)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setGeometry(QtCore.QRect(50, 470, 721, 151))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(26)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setObjectName("radioButton_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, -60, 581, 211))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 600, 171, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 600, 171, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 310, 931, 121))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(720, 180, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(720, 180, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(10)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setEnabled(True)
        self.textEdit_2.setGeometry(QtCore.QRect(720, 260, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(10)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setAutoFillBackground(False)
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 170, 361, 81))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 250, 361, 81))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(220, 170, 391, 81))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 420, 241, 101))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 996, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton.setText(_translate("MainWindow", "Add an expense"))
        self.radioButton_2.setText(_translate("MainWindow", "Add amount to your budget"))
        self.radioButton_3.setText(_translate("MainWindow", "Check how much you have left"))
        self.radioButton_4.setText(_translate("MainWindow", "Save And Exit"))
        self.radioButton_5.setText(_translate("MainWindow", "Exit without saving"))
        self.label.setText(_translate("MainWindow", "Money Manager"))
        self.pushButton.setText(_translate("MainWindow", "Proceed"))
        self.pushButton_3.setText(_translate("MainWindow", "Process"))
        self.label_2.setText(_translate("MainWindow", ""))
        self.label_3.setText(_translate("MainWindow", "Enter your expense"))
        self.label_4.setText(_translate("MainWindow", "Number of days of spending"))
        self.label_5.setText(_translate("MainWindow", "Amount to be added to your budget"))
        self.pushButton_2.setText(_translate("MainWindow", "Return to main screen"))









if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    _translate = QtCore.QCoreApplication.translate
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.label_4.hide()
    ui.label_3.hide()
    ui.label_5.hide()
    ui.textEdit.hide()
    ui.textEdit_2.hide()
    ui.pushButton.hide()
    ui.label_2.hide()
    MainWindow.show()
    ui.pushButton_2.hide()
    ui.textEdit_3.hide()
    ui.pushButton_3.hide()
    ui.pushButton_3.setEnabled(False)
    flag=0
    flag1=0
    def BTN1():
        file = open(path2, 'rb')
        pos = next = 0
        for line in file:
            pos = next  # position of beginning of this line
            next += len(line)  # compute position of beginning of next line
        file = open(path2   , 'ab')
        file.truncate(pos)
        sys.exit(app.exec_())

    def retrans1():
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Money Manager"))
        ui.radioButton.hide()
        ui.radioButton_2.hide()
        ui.radioButton_3.hide()
        ui.radioButton_4.hide()
        ui.radioButton_5.hide()
        ui.label_3.show()
        ui.label_4.show()
        ui.textEdit.show()
        ui.textEdit_2.show()
        ui.pushButton.show()
        ui.pushButton.setEnabled(True)
        ui.label_2.setText(_translate("MainWindow", ""))
        ui.pushButton_2.hide()
        ui.textEdit_3.hide()
        ui.textEdit_3.setEnabled(False)
        ui.label_5.hide()
        ui.label_2.show()
        ui.pushButton_3.setEnabled(False)
        global flag
        flag=1
        #abc()
    def retrans4():
        ui.label_3.hide()
        ui.label_4.hide()
        ui.textEdit.hide()
        ui.textEdit_2.hide()
        ui.pushButton_3.hide()
        ui.pushButton_2.show()
        global flag
        flag = 1
        ui.radioButton.hide()
        ui.radioButton_2.hide()
        ui.radioButton_3.hide()
        ui.radioButton_4.hide()
        ui.radioButton_5.hide()
        ui.label_2.show()
        ui.radioButton_4.setEnabled(False)
        global flag1
        flag1 = 1
    def retrans2():
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Money Manager"))
        ui.radioButton.hide()
        ui.radioButton_2.hide()
        ui.radioButton_3.hide()
        ui.radioButton_4.hide()
        ui.radioButton_5.hide()
        ui.label_5.show()
        ui.textEdit.hide()
        ui.pushButton.show()
        ui.label_2.show()
        ui.label_3.hide()
        ui.label_4.hide()
        ui.textEdit_3.show()
        ui.pushButton_3.show()
        ui.pushButton_3.setEnabled(True)
        ui.textEdit_3.setEnabled(True)
        ui.pushButton.hide()
        ui.pushButton_2.hide()
        ui.textEdit.hide()
        ui.textEdit.setEnabled(False)
        ui.radioButton_2.setEnabled(False)
        global flag1
        flag1 = 1
        #abc()


    def retrans3():
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Money Manager"))
        ui.radioButton.hide()
        ui.radioButton_2.hide()
        ui.radioButton_3.hide()
        ui.radioButton_4.hide()
        ui.radioButton_5.hide()
        ui.label_5.hide()
        ui.textEdit.hide()
        ui.pushButton.show()
        ui.label_2.hide()
        ui.label_3.hide()
        ui.label_4.hide()
        ui.textEdit_3.hide()
        ui.pushButton_3.hide()
        ui.pushButton_3.setEnabled(False)
        ui.label_2.show()
        ui.pushButton.hide()
        ui.pushButton_2.show()
        ui.textEdit_2.hide()
        ui.radioButton_3.setEnabled(False)
        global flag
        global flag1
        flag1=1
        flag = 1

    def clicked():
        ui.textEdit.setEnabled(True)
        ui.textEdit_2.setEnabled(True)
        retrans1()
        abc()
        return
    def clicked2():
        ui.textEdit.setEnabled(True)
        ui.textEdit_2.hide()
        retrans2()
        abc()
        return
    def clicked3():
        retrans3()
        abc()
    def clicked4():
        flag2=1
        retrans4()
        abc()
    def exit():
        sys.exit(app.exec_())
    ui.radioButton.toggled.connect(clicked)
    ui.radioButton_2.toggled.connect(clicked2)
    ui.radioButton_3.toggled.connect(clicked3)
    ui.radioButton_4.toggled.connect(clicked4)
    ui.radioButton_5.toggled.connect(exit)
    #endProgram = 'no'
    global totalBudget
    totalBudget = currentBudget




    def BTN(MainWindow):
        ui.radioButton.show()
        ui.radioButton_2.show()
        ui.radioButton_3.show()
        ui.radioButton_4.show()
        ui.radioButton_5.show()
        ui.label_3.hide()
        ui.label_4.hide()
        ui.textEdit.hide()
        ui.textEdit_2.hide()
        ui.pushButton_2.hide()
        ui.label_4.hide()
        ui.label_3.hide()
        ui.label_5.hide()
        ui.textEdit.hide()
        ui.textEdit_2.hide()
        ui.pushButton.hide()
        ui.label_2.hide()
        ui.pushButton.setEnabled(False)
        ui.pushButton_3.setEnabled(False)
        ui.textEdit_3.hide()
        ui.textEdit_3.setEnabled(False)
        ui.label_5.hide()
        ui.label_4.hide()
        ui.label_3.hide()





    def abc():
        if(ui.radioButton.isChecked()==True):
            ui.pushButton.clicked.connect(addExpense)
            #MainWindow.show()
            ui.radioButton.setEnabled(False)
            return

        elif(ui.radioButton_2.isChecked()==True):
            ui.pushButton_3.clicked.connect(addRevenue)
            return
           #MainWindow.show()
        elif(ui.radioButton_3.isChecked()==True):
            _translate = QtCore.QCoreApplication.translate
            ui.label_2.setText(_translate("MainWindow",'Your balance is {0}'.format(totalBudget)))
            check(totalBudget)
            ui.pushButton_2.clicked.connect(BTN)
            #MainWindow.show()
            return
        elif(ui.radioButton_4.isChecked()==True):
            flag2=1
            saveBudget(totalBudget)
            record(totalBudget)
            _translate = QtCore.QCoreApplication.translate
            ui.label.setText(_translate("MainWindow", "SAVED"))
            ui.label_2.setText(_translate("MainWindow", "Latest details have been saved,successfully."))
            ui.pushButton_2.setText(_translate("MainWindow", "Exit"))
            ui.radioButton_4.setEnabled(False)
            return
        elif(ui.radioButton_5.isChecked()==True):
            sys.exit(app.exec_())










    def record(totalBudget):
        with open(path2, 'a') as f:
            f.write("Your Budget as of " + str(time.strftime("%d/%m/%Y")) + " " + str(
                time.strftime("%I:%M:%S")) + " is " + str(totalBudget) + "\n")

    def saveBudget(totalBudget):
        with open(path, 'w') as f:
            print("Latest details have been saved.")
            f.write(str(totalBudget))
            f.close()
        ui.pushButton_2.clicked.connect(BTN1)
        return




    def check(totalBudget):
        date = int(time.strftime("%d"))
        if (date >= 1 and date <= 10):
            if (totalBudget <= 500):
                print("Your total budget is Rs " + str(
                    totalBudget) + " only, you might want to cut down on your expenses")

        elif (date >= 25):
            if (totalBudget >= 500):
                print("Your total budget is " + str(totalBudget) + " you can go easy on yourself and spend more")

        else:
            print('Invalid selection, please try again')


    def addExpense():
        global flag1
        Expense = int(ui.textEdit.toPlainText())
        TimesPerMonth=int(ui.textEdit_2.toPlainText())
        if (flag1 == 1):
            Expense = Expense / 2
            TimesPerMonth = TimesPerMonth
        TotalExpense=Expense*TimesPerMonth
        ui.textEdit.hide()
        ui.textEdit_2.hide()
        ui.label_3.hide()
        ui.label_4.hide()
        global totalBudget
        if totalBudget - TotalExpense >= 0:
            totalBudget = totalBudget - TotalExpense
            _translate = QtCore.QCoreApplication.translate
            ui.label_2.setText(_translate("MainWindow", 'The expenses was accepted, your remaining budget is: Rs{0} '.format(totalBudget)))
            print('The expenses was accepted, your remaining budget is: Rs{0} '.format(totalBudget))
            ui.pushButton_2.show()
            ui.pushButton.hide()
            ui.pushButton.setEnabled(False)
            ui.pushButton_2.clicked.connect(BTN)
            #ui.radioButton.setEnabled(False)
            Expense=0
            TimesPerMonth=0
            return totalBudget
        else:
            _translate = QtCore.QCoreApplication.translate
            ui.label_2.setText(_translate("MainWindow",'The expenses was rejected because the budget exceeded.'))
            ui.pushButton_2.show()
            ui.pushButton.hide()
            ui.pushButton_2.clicked.connect(BTN)
            ui.pushButton.setEnabled(False)
            #ui.radioButton.setEnabled(False)
            return totalBudget


    def addRevenue():
        global flag
        ui.pushButton_3.setEnabled(False)
        #ui.radioButton_2.setEnabled(False)
        global totalBudget
        print(totalBudget)
        Revenue=ui.textEdit_3.toPlainText()
        Revenue=int(Revenue)
        print(flag)
        if(flag==1):
            Revenue=Revenue/2
        #revenue = float(input('Enter new monthly allowance: Rs '))
        totalBudget = totalBudget + Revenue
        _translate = QtCore.QCoreApplication.translate
        ui.label_2.setText(_translate("MainWindow",'your new budget is: Rs{0} '.format(totalBudget)))
        print('your new budget is: Rs{0} '.format(totalBudget))
        ui.pushButton_2.show()
        ui.pushButton_3.hide()
        Revenue=0
        ui.pushButton_2.clicked.connect(BTN)
        return

    sys.exit(app.exec_())