# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_movie_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MovieWidget(object):
    def setupUi(self, MovieWidget):
        MovieWidget.setObjectName("MovieWidget")
        MovieWidget.resize(787, 168)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MovieWidget.sizePolicy().hasHeightForWidth())
        MovieWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        MovieWidget.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(MovieWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(MovieWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 130))

        self.groupBox.setStyleSheet("QGroupBox { \n"
                                    "    border: 2px solid #CCFFFF; \n"
                                    "    border-radius: 10px; \n"
                                    "    margin-top: 2ex; \n"
                                    " } \n"
                                    "QGroupBox::title { \n"
                                    "subcontrol-origin: margin;"
                                    "subcontrol-position: top center;"
                                    "padding: 0 3px; \n"
                                    " } ")

        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_picture = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_picture.sizePolicy().hasHeightForWidth())
        self.label_picture.setSizePolicy(sizePolicy)
        self.label_picture.setObjectName("label_picture")

        # self.label_picture.setMinimumSize(QtCore.QSize(0, 50))

        self.horizontalLayout.addWidget(self.label_picture)
        spacerItem = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_rating = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_rating.sizePolicy().hasHeightForWidth())
        self.label_rating.setSizePolicy(sizePolicy)
        self.label_rating.setObjectName("label_rating")
        self.horizontalLayout.addWidget(self.label_rating)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_add_to_quiz = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add_to_quiz.sizePolicy().hasHeightForWidth())
        self.btn_add_to_quiz.setSizePolicy(sizePolicy)
        self.btn_add_to_quiz.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_add_to_quiz.setObjectName("btn_add_to_quiz")
        self.horizontalLayout.addWidget(self.btn_add_to_quiz)
        self.verticalLayout.addWidget(self.groupBox)
        self.retranslateUi(MovieWidget)
        QtCore.QMetaObject.connectSlotsByName(MovieWidget)


    def retranslateUi(self, MovieWidget):
        _translate = QtCore.QCoreApplication.translate
        MovieWidget.setWindowTitle(_translate("MovieWidget", "Form"))
        self.groupBox.setTitle(_translate("MovieWidget", "GroupBox"))
        self.label_picture.setText(_translate("MovieWidget", "\"КАРТИНКА\""))
        self.label_rating.setText(_translate("MovieWidget", "\"РЕЙТИНГ\""))
        self.btn_add_to_quiz.setText(_translate("MovieWidget", "Добавить в опрос"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MovieWidget = QtWidgets.QWidget()
    ui = Ui_MovieWidget()
    ui.setupUi(MovieWidget)
    MovieWidget.show()
    sys.exit(app.exec_())
