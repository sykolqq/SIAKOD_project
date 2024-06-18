# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_results.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WidgetResults(object):
    def setupUi(self, WidgetResults):
        WidgetResults.setObjectName("WidgetResults")
        WidgetResults.resize(800, 700)
        WidgetResults.setMinimumSize(QtCore.QSize(800, 700))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        WidgetResults.setFont(font)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(WidgetResults)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_results = QtWidgets.QLabel(WidgetResults)

        self.label_results.setStyleSheet("""
        color: #c5bfe5;
        font-size: 30pt;
        """)

        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_results.setFont(font)
        self.label_results.setObjectName("label_results")
        self.verticalLayout_3.addWidget(self.label_results, 0, QtCore.Qt.AlignHCenter)
        self.scrollArea = QtWidgets.QScrollArea(WidgetResults)
        self.scrollArea.setStyleSheet("QScrollBar:vertical {\n"
"                        border: 1px solid #999999;\n"
"                        background: #f0f0f0;\n"
"                        width: 15px;\n"
"                        margin: 20px 0 20px 0;\n"
"                    }\n"
"                    QScrollBar::handle:vertical {\n"
"                        background: #c5bfe5;\n"
"                        min-height: 20px;\n"
"                    }\n"
"                    QScrollBar::add-line:vertical {\n"
"                        background: none;\n"
"                    }\n"
"                    QScrollBar::sub-line:vertical {\n"
"                        background: none;\n"
"                    }\n"
"\n"
"                    QScrollBar:horizontal {\n"
"                        border: 1px solid #99CCFF;\n"
"                        background: #f0f0f0;\n"
"                        margin: 0 20px 0 20px;\n"
"                    }\n"
"                    QScrollBar::handle:horizontal {\n"
"                        background: #c5bfe5;\n"
"                        min-height: 20px;\n"
"                    }\n"
"                    QScrollBar::add-line:horizontal {\n"
"                        background: none;\n"
"                    }\n"
"                    QScrollBar::sub-line:horizontal {\n"
"                        background: none;\n"
"                    }")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 780, 550))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.layout_for_movie_widgets = QtWidgets.QVBoxLayout()
        self.layout_for_movie_widgets.setObjectName("layout_for_movie_widgets")
        self.verticalLayout_4.addLayout(self.layout_for_movie_widgets)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.layout_for_btn = QtWidgets.QHBoxLayout()
        self.layout_for_btn.setContentsMargins(-1, 0, -1, -1)
        self.layout_for_btn.setObjectName("layout_for_btn")
        self.btn_return = QtWidgets.QPushButton(WidgetResults)
        self.btn_return.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_return.setMaximumSize(QtCore.QSize(500, 16777215))
        self.btn_return.setStyleSheet("background-color: rgb(94, 91, 110);")
        self.btn_return.setObjectName("btn_return")
        self.layout_for_btn.addWidget(self.btn_return)
        self.verticalLayout_3.addLayout(self.layout_for_btn)
        spacerItem = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem)

        self.retranslateUi(WidgetResults)
        QtCore.QMetaObject.connectSlotsByName(WidgetResults)

    def retranslateUi(self, WidgetResults):
        _translate = QtCore.QCoreApplication.translate
        WidgetResults.setWindowTitle(_translate("WidgetResults", "Form"))
        self.label_results.setText(_translate("WidgetResults", "Результаты"))
        self.btn_return.setText(_translate("WidgetResults", "Вернуться"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WidgetResults = QtWidgets.QWidget()
    ui = Ui_WidgetResults()
    ui.setupUi(WidgetResults)
    WidgetResults.show()
    sys.exit(app.exec_())