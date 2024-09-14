# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFrame,
    QHBoxLayout, QLabel, QSizePolicy, QSlider,
    QSpinBox, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(368, 98)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 101, 16))
        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 20, 361, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 50, 51, 16))
        self.horizontalSlider_x1 = QSlider(Form)
        self.horizontalSlider_x1.setObjectName(u"horizontalSlider_x1")
        self.horizontalSlider_x1.setGeometry(QRect(70, 50, 221, 16))
        self.horizontalSlider_x1.setOrientation(Qt.Horizontal)
        self.spinBox_x1 = QSpinBox(Form)
        self.spinBox_x1.setObjectName(u"spinBox_x1")
        self.spinBox_x1.setGeometry(QRect(310, 40, 42, 22))
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 70, 280, 22))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.doubleSpinBox = QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setWrapping(False)
        self.doubleSpinBox.setMaximum(1.000000000000000)
        self.doubleSpinBox.setSingleStep(0.010000000000000)

        self.horizontalLayout.addWidget(self.doubleSpinBox)

        self.checkBox_enableYoloAuxiliary = QCheckBox(self.layoutWidget)
        self.checkBox_enableYoloAuxiliary.setObjectName(u"checkBox_enableYoloAuxiliary")

        self.horizontalLayout.addWidget(self.checkBox_enableYoloAuxiliary)

        self.checkBox_showGunBox = QCheckBox(self.layoutWidget)
        self.checkBox_showGunBox.setObjectName(u"checkBox_showGunBox")

        self.horizontalLayout.addWidget(self.checkBox_showGunBox)


        self.retranslateUi(Form)
        self.horizontalSlider_x1.valueChanged.connect(self.spinBox_x1.setValue)
        self.spinBox_x1.valueChanged.connect(self.horizontalSlider_x1.setValue)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Yolov8-\u548c\u5e73\u7cbe\u82f1", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Yolo\u8bc6\u522b\u62c9\u67aaP\u503c", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"1\u500d\u955c\uff1a", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u7784\u51c6\u4f4d\u7f6e\uff1a", None))
        self.doubleSpinBox.setPrefix("")
        self.checkBox_enableYoloAuxiliary.setText(QCoreApplication.translate("Form", u"\u8f85\u52a9\u7784\u51c6", None))
        self.checkBox_showGunBox.setText(QCoreApplication.translate("Form", u"\u663e\u793a\u8bc6\u522b\u6846", None))
    # retranslateUi

