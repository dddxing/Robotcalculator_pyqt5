# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'requiredFieldsWarning.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_requiredFieldsWarning(object):
    def setupUi(self, requiredFieldsWarning):
        requiredFieldsWarning.setObjectName("requiredFieldsWarning")
        requiredFieldsWarning.resize(198, 120)
        self.gridLayout = QtWidgets.QGridLayout(requiredFieldsWarning)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(requiredFieldsWarning)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(requiredFieldsWarning)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(requiredFieldsWarning)
        self.buttonBox.accepted.connect(requiredFieldsWarning.accept)
        self.buttonBox.rejected.connect(requiredFieldsWarning.reject)
        QtCore.QMetaObject.connectSlotsByName(requiredFieldsWarning)

    def retranslateUi(self, requiredFieldsWarning):
        _translate = QtCore.QCoreApplication.translate
        requiredFieldsWarning.setWindowTitle(_translate("requiredFieldsWarning", "Dialog"))
        self.label.setText(_translate("requiredFieldsWarning", "Required Fields\", \"Please include all fields!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    requiredFieldsWarning = QtWidgets.QDialog()
    ui = Ui_requiredFieldsWarning()
    ui.setupUi(requiredFieldsWarning)
    requiredFieldsWarning.show()
    sys.exit(app.exec_())
