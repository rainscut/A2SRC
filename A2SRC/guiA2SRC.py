# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiA2SRC.ui'
#
# Created: Mon Jan 05 18:49:38 2015
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(733, 779)
        self.matplotlibwidget = MatplotlibWidget(Dialog)
        self.matplotlibwidget.setGeometry(QtCore.QRect(320, 40, 400, 300))
        self.matplotlibwidget.setObjectName(_fromUtf8("matplotlibwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 30, 271, 329))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labelModulation = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelModulation.sizePolicy().hasHeightForWidth())
        self.labelModulation.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelModulation.setFont(font)
        self.labelModulation.setObjectName(_fromUtf8("labelModulation"))
        self.verticalLayout.addWidget(self.labelModulation)
        self.comboBoxModulationType = QtGui.QComboBox(self.verticalLayoutWidget)
        self.comboBoxModulationType.setEditable(False)
        self.comboBoxModulationType.setObjectName(_fromUtf8("comboBoxModulationType"))
        self.comboBoxModulationType.addItem(_fromUtf8(""))
        self.comboBoxModulationType.addItem(_fromUtf8(""))
        self.comboBoxModulationType.addItem(_fromUtf8(""))
        self.comboBoxModulationType.addItem(_fromUtf8(""))
        self.comboBoxModulationType.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.comboBoxModulationType)
        self.comboBoxModulationPhase = QtGui.QComboBox(self.verticalLayoutWidget)
        self.comboBoxModulationPhase.setObjectName(_fromUtf8("comboBoxModulationPhase"))
        self.comboBoxModulationPhase.addItem(_fromUtf8(""))
        self.comboBoxModulationPhase.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.comboBoxModulationPhase)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEditModulationFreq = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEditModulationFreq.setObjectName(_fromUtf8("lineEditModulationFreq"))
        self.horizontalLayout.addWidget(self.lineEditModulationFreq)
        self.labelModulationFreq = QtGui.QLabel(self.verticalLayoutWidget)
        self.labelModulationFreq.setObjectName(_fromUtf8("labelModulationFreq"))
        self.horizontalLayout.addWidget(self.labelModulationFreq)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEditModulationAmp = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEditModulationAmp.setObjectName(_fromUtf8("lineEditModulationAmp"))
        self.horizontalLayout_2.addWidget(self.lineEditModulationAmp)
        self.labelModulationAmp = QtGui.QLabel(self.verticalLayoutWidget)
        self.labelModulationAmp.setObjectName(_fromUtf8("labelModulationAmp"))
        self.horizontalLayout_2.addWidget(self.labelModulationAmp)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.labelSynth = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSynth.sizePolicy().hasHeightForWidth())
        self.labelSynth.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelSynth.setFont(font)
        self.labelSynth.setObjectName(_fromUtf8("labelSynth"))
        self.verticalLayout_2.addWidget(self.labelSynth)
        self.comboBoxSynthType = QtGui.QComboBox(self.verticalLayoutWidget)
        self.comboBoxSynthType.setEditable(False)
        self.comboBoxSynthType.setObjectName(_fromUtf8("comboBoxSynthType"))
        self.comboBoxSynthType.addItem(_fromUtf8(""))
        self.comboBoxSynthType.addItem(_fromUtf8(""))
        self.comboBoxSynthType.addItem(_fromUtf8(""))
        self.comboBoxSynthType.addItem(_fromUtf8(""))
        self.comboBoxSynthType.addItem(_fromUtf8(""))
        self.verticalLayout_2.addWidget(self.comboBoxSynthType)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lineEditSynthFreq = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEditSynthFreq.setObjectName(_fromUtf8("lineEditSynthFreq"))
        self.horizontalLayout_3.addWidget(self.lineEditSynthFreq)
        self.labelSynthFreq = QtGui.QLabel(self.verticalLayoutWidget)
        self.labelSynthFreq.setObjectName(_fromUtf8("labelSynthFreq"))
        self.horizontalLayout_3.addWidget(self.labelSynthFreq)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lineEditSynthAmp = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEditSynthAmp.setObjectName(_fromUtf8("lineEditSynthAmp"))
        self.horizontalLayout_4.addWidget(self.lineEditSynthAmp)
        self.labelSynthAmp = QtGui.QLabel(self.verticalLayoutWidget)
        self.labelSynthAmp.setObjectName(_fromUtf8("labelSynthAmp"))
        self.horizontalLayout_4.addWidget(self.labelSynthAmp)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.pushButton_2 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.labelModulation.setText(_translate("Dialog", "Jitter Modulation", None))
        self.comboBoxModulationType.setItemText(0, _translate("Dialog", "None", None))
        self.comboBoxModulationType.setItemText(1, _translate("Dialog", "Sinusoidal", None))
        self.comboBoxModulationType.setItemText(2, _translate("Dialog", "Triangular", None))
        self.comboBoxModulationType.setItemText(3, _translate("Dialog", "Rectangular", None))
        self.comboBoxModulationType.setItemText(4, _translate("Dialog", "Random", None))
        self.comboBoxModulationPhase.setItemText(0, _translate("Dialog", "R / L In-Phase Mod.", None))
        self.comboBoxModulationPhase.setItemText(1, _translate("Dialog", "R / L Counter-Phase Mod.", None))
        self.lineEditModulationFreq.setText(_translate("Dialog", "50", None))
        self.labelModulationFreq.setText(_translate("Dialog", " Hz", None))
        self.lineEditModulationAmp.setText(_translate("Dialog", "1e-3", None))
        self.labelModulationAmp.setText(_translate("Dialog", " UI", None))
        self.labelSynth.setText(_translate("Dialog", "Synthetic Signal", None))
        self.comboBoxSynthType.setItemText(0, _translate("Dialog", "None, use WAV-File", None))
        self.comboBoxSynthType.setItemText(1, _translate("Dialog", "Sinusoidal", None))
        self.comboBoxSynthType.setItemText(2, _translate("Dialog", "Triangular", None))
        self.comboBoxSynthType.setItemText(3, _translate("Dialog", "Rectangular", None))
        self.comboBoxSynthType.setItemText(4, _translate("Dialog", "Random", None))
        self.lineEditSynthFreq.setText(_translate("Dialog", "1000", None))
        self.labelSynthFreq.setText(_translate("Dialog", " Hz", None))
        self.lineEditSynthAmp.setText(_translate("Dialog", "50", None))
        self.labelSynthAmp.setText(_translate("Dialog", "% FS", None))
        self.pushButton_2.setText(_translate("Dialog", "Open File", None))
        self.pushButton.setText(_translate("Dialog", "Start / Stop", None))

from matplotlibwidget import MatplotlibWidget
