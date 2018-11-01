# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_animal.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(416, 313)
        self.bt_confirm = QtWidgets.QDialogButtonBox(Dialog)
        self.bt_confirm.setGeometry(QtCore.QRect(30, 240, 251, 32))
        self.bt_confirm.setOrientation(QtCore.Qt.Horizontal)
        self.bt_confirm.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.bt_confirm.setObjectName("bt_confirm")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(70, 40, 261, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.age_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.age_input.setObjectName("age_input")
        self.gridLayout.addWidget(self.age_input, 3, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.sex_selection = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.sex_selection.setObjectName("sex_selection")
        self.gridLayout.addWidget(self.sex_selection, 2, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.species_selection = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.species_selection.setObjectName("species_selection")
        self.gridLayout.addWidget(self.species_selection, 1, 2, 1, 1)
        self.name_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.name_input.setObjectName("name_input")
        self.gridLayout.addWidget(self.name_input, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.enclosure_selection = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.enclosure_selection.setObjectName("enclosure_selection")
        self.gridLayout.addWidget(self.enclosure_selection, 4, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(150, 10, 181, 16))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        self.bt_confirm.accepted.connect(Dialog.accept)
        self.bt_confirm.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", "Age"))
        self.label.setText(_translate("Dialog", "Name"))
        self.label_2.setText(_translate("Dialog", "Species"))
        self.label_3.setText(_translate("Dialog", "Sex"))
        self.label_6.setText(_translate("Dialog", "Enclosure"))
        self.label_5.setText(_translate("Dialog", "Create a new animal"))

