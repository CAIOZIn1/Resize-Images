# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(915, 725)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.input_heigth = QtWidgets.QLineEdit(self.centralwidget)
        self.input_heigth.setObjectName("input_heigth")
        self.gridLayout.addWidget(self.input_heigth, 2, 3, 1, 1)
        self.label_width = QtWidgets.QLabel(self.centralwidget)
        self.label_width.setObjectName("label_width")
        self.gridLayout.addWidget(self.label_width, 2, 0, 1, 1)
        self.btn_resize = QtWidgets.QPushButton(self.centralwidget)
        self.btn_resize.setObjectName("btn_resize")
        self.gridLayout.addWidget(self.btn_resize, 2, 4, 1, 1)
        self.input_width = QtWidgets.QLineEdit(self.centralwidget)
        self.input_width.setObjectName("input_width")
        self.gridLayout.addWidget(self.input_width, 2, 1, 1, 1)
        self.label_heigth = QtWidgets.QLabel(self.centralwidget)
        self.label_heigth.setObjectName("label_heigth")
        self.gridLayout.addWidget(self.label_heigth, 2, 2, 1, 1)
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setObjectName("btn_save")
        self.gridLayout.addWidget(self.btn_save, 3, 4, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 895, 618))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(
            self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_image = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_image.setText("")
        self.label_image.setObjectName("label_image")
        self.gridLayout_2.addWidget(self.label_image, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 5)
        self.btn_choice_file = QtWidgets.QPushButton(self.centralwidget)
        self.btn_choice_file.setObjectName("btn_choice_file")
        self.gridLayout.addWidget(self.btn_choice_file, 1, 4, 1, 1)
        self.input_file = QtWidgets.QLineEdit(self.centralwidget)
        self.input_file.setObjectName("input_file")
        self.gridLayout.addWidget(self.input_file, 1, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Redimensionar imagem"))
        self.label_width.setText(_translate("MainWindow", "Largura"))
        self.btn_resize.setText(_translate("MainWindow", "Redimensionar"))
        self.label_heigth.setText(_translate("MainWindow", "Altura"))
        self.btn_save.setText(_translate("MainWindow", "Salvar"))
        self.btn_choice_file.setText(
            _translate("MainWindow", "Escolher arquivo"))
