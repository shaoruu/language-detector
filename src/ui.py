# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 550)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 550))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 550))
        MainWindow.setStyleSheet("background-color: rgb(27, 42, 73);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(0, 0, 1001, 541))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.left_panel = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.left_panel.setContentsMargins(0, 0, 0, 0)
        self.left_panel.setObjectName("left_panel")
        self.appTitle = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.appTitle.setFont(font)
        self.appTitle.setStyleSheet("color: rgb(238, 238, 238);")
        self.appTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.appTitle.setWordWrap(True)
        self.appTitle.setObjectName("appTitle")
        self.left_panel.addWidget(self.appTitle)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(5, -1, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.inputLabel = QtWidgets.QLabel(self.layoutWidget)
        self.inputLabel.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(16)
        self.inputLabel.setFont(font)
        self.inputLabel.setStyleSheet("color: rgb(238, 238, 238);")
        self.inputLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.inputLabel.setIndent(3)
        self.inputLabel.setObjectName("inputLabel")
        self.verticalLayout.addWidget(self.inputLabel)
        self.inputBox = QtWidgets.QTextEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Waree")
        font.setPointSize(12)
        self.inputBox.setFont(font)
        self.inputBox.setStyleSheet("background-color: rgb(237, 247, 250);")
        self.inputBox.setObjectName("inputBox")
        self.verticalLayout.addWidget(self.inputBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.languagesLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(16)
        self.languagesLabel.setFont(font)
        self.languagesLabel.setStyleSheet("color: rgb(238, 238, 238);")
        self.languagesLabel.setScaledContents(True)
        self.languagesLabel.setWordWrap(False)
        self.languagesLabel.setIndent(3)
        self.languagesLabel.setObjectName("languagesLabel")
        self.verticalLayout_3.addWidget(self.languagesLabel)
        self.languagesTable = QtWidgets.QTableWidget(self.layoutWidget)
        self.languagesTable.setStyleSheet("color: rgb(238, 238, 238);\n"
"background-color: rgb(21, 34, 61);")
        self.languagesTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.languagesTable.setAlternatingRowColors(False)
        self.languagesTable.setTextElideMode(QtCore.Qt.ElideRight)
        self.languagesTable.setObjectName("languagesTable")
        self.languagesTable.setColumnCount(3)
        self.languagesTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.languagesTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.languagesTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.languagesTable.setHorizontalHeaderItem(2, item)
        self.languagesTable.horizontalHeader().setCascadingSectionResizes(False)
        self.languagesTable.horizontalHeader().setDefaultSectionSize(90)
        self.languagesTable.horizontalHeader().setStretchLastSection(True)
        self.languagesTable.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_3.addWidget(self.languagesTable)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.left_panel.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, -1, 0, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.importButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(12)
        self.importButton.setFont(font)
        self.importButton.setStyleSheet("color: rgb(238, 238, 238);")
        self.importButton.setObjectName("importButton")
        self.horizontalLayout.addWidget(self.importButton)
        self.runButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(12)
        self.runButton.setFont(font)
        self.runButton.setStyleSheet("color: rgb(238, 238, 238);")
        self.runButton.setObjectName("runButton")
        self.horizontalLayout.addWidget(self.runButton)
        self.left_panel.addLayout(self.horizontalLayout)
        self.groupBox = QtWidgets.QGroupBox(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.right_panel = QtWidgets.QVBoxLayout(self.groupBox)
        self.right_panel.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.right_panel.setContentsMargins(-1, 0, -1, -1)
        self.right_panel.setObjectName("right_panel")
        self.graphLabel = QtWidgets.QLabel(self.groupBox)
        self.graphLabel.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(16)
        self.graphLabel.setFont(font)
        self.graphLabel.setStyleSheet("color: rgb(238, 238, 238);")
        self.graphLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.graphLabel.setObjectName("graphLabel")
        self.right_panel.addWidget(self.graphLabel)
        self.graph = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(40)
        self.graph.setFont(font)
        self.graph.setStyleSheet("background-color: rgb(0, 64, 133);\n"
"color: rgba(238, 238, 238,.4);")
        self.graph.setScaledContents(False)
        self.graph.setAlignment(QtCore.Qt.AlignCenter)
        self.graph.setWordWrap(True)
        self.graph.setObjectName("graph")
        self.right_panel.addWidget(self.graph)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.appTitle.setText(_translate("MainWindow", "Language Detector"))
        self.inputLabel.setText(_translate("MainWindow", "Text Input:"))
        self.inputBox.setPlaceholderText(_translate("MainWindow", "Enter Text..."))
        self.languagesLabel.setText(_translate("MainWindow", "Detected Language: "))
        item = self.languagesTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Language"))
        item = self.languagesTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "%"))
        item = self.languagesTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Error"))
        self.importButton.setText(_translate("MainWindow", "Import"))
        self.runButton.setText(_translate("MainWindow", "Run"))
        self.graphLabel.setText(_translate("MainWindow", "Prediction Graph"))
        self.graph.setText(_translate("MainWindow", "?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
