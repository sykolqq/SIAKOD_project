# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_quiz_round.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WidgetQuizRound(object):
    def setupUi(self, WidgetQuizRound):
        WidgetQuizRound.setObjectName("WidgetQuizRound")
        WidgetQuizRound.resize(800, 700)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(WidgetQuizRound)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setObjectName("main_layout")
        self.label_current_round = QtWidgets.QLabel(WidgetQuizRound)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_current_round.sizePolicy().hasHeightForWidth())
        self.label_current_round.setSizePolicy(sizePolicy)
        self.label_current_round.setStyleSheet("font: 30pt \"Arial\";\n"
"color: rgb(198, 190, 229);")
        self.label_current_round.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_current_round.setObjectName("label_current_round")
        self.main_layout.addWidget(self.label_current_round)
        self.layout_with_group_boxes = QtWidgets.QWidget(WidgetQuizRound)
        self.layout_with_group_boxes.setStyleSheet("#layout_with_group_boxes {\n"
"    background-color: rgb(46, 46, 46);\n"
"    border: 5px solid #242424;\n"
"    padding: 10px;\n"
"}")
        self.layout_with_group_boxes.setObjectName("layout_with_group_boxes")
        self.layout_with_groupBoxes = QtWidgets.QHBoxLayout(self.layout_with_group_boxes)
        self.layout_with_groupBoxes.setObjectName("layout_with_groupBoxes")
        self.groupBox_movie1 = QtWidgets.QGroupBox(self.layout_with_group_boxes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_movie1.sizePolicy().hasHeightForWidth())
        self.groupBox_movie1.setSizePolicy(sizePolicy)
        self.groupBox_movie1.setMinimumSize(QtCore.QSize(200, 300))
        self.groupBox_movie1.setStyleSheet("QGroupBox {\n"
"    /*background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #CC99FF, stop: 1 #CCCCFF);*/\n"
"    background: #666;\n"
"    border: 5px solid #c7bfe6;\n"
"    border-radius: 0px;\n"
"    margin-top: 5px;\n"
"    margin-bottom: 5px;\n"
"}\n"
"QGroupBox QLabel {\n"
"    background: transparent;\n"
"}")
        self.groupBox_movie1.setTitle("")
        self.groupBox_movie1.setObjectName("groupBox_movie1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_movie1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_movie1_title = QtWidgets.QLabel(self.groupBox_movie1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_movie1_title.sizePolicy().hasHeightForWidth())
        self.label_movie1_title.setSizePolicy(sizePolicy)
        self.label_movie1_title.setStyleSheet("font: 20pt \"Arial\";\n"
"color: rgb(198, 190, 229);")
        self.label_movie1_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_movie1_title.setObjectName("label_movie1_title")
        self.verticalLayout_4.addWidget(self.label_movie1_title)
        spacerItem = QtWidgets.QSpacerItem(20, 70, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem)
        self.layout_movie1_info = QtWidgets.QVBoxLayout()
        self.layout_movie1_info.setObjectName("layout_movie1_info")
        self.label_movie1_producer = QtWidgets.QLabel(self.groupBox_movie1)
        self.label_movie1_producer.setStyleSheet("color: rgb(198, 190, 229)")
        self.label_movie1_producer.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_movie1_producer.setObjectName("label_movie1_producer")
        self.layout_movie1_info.addWidget(self.label_movie1_producer)
        self.label_movie1_region = QtWidgets.QLabel(self.groupBox_movie1)
        self.label_movie1_region.setStyleSheet("color: #c3c3c3;")
        self.label_movie1_region.setObjectName("label_movie1_region")
        self.layout_movie1_info.addWidget(self.label_movie1_region, 0, QtCore.Qt.AlignRight)
        self.label_movie1_rating = QtWidgets.QLabel(self.groupBox_movie1)
        self.label_movie1_rating.setStyleSheet("color: #FFD700;")
        self.label_movie1_rating.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_movie1_rating.setObjectName("label_movie1_rating")
        self.layout_movie1_info.addWidget(self.label_movie1_rating)
        self.label_movie1_genre = QtWidgets.QLabel(self.groupBox_movie1)
        self.label_movie1_genre.setStyleSheet("color: #c3c3c3;")
        self.label_movie1_genre.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_movie1_genre.setObjectName("label_movie1_genre")
        self.layout_movie1_info.addWidget(self.label_movie1_genre)
        self.verticalLayout_4.addLayout(self.layout_movie1_info)
        self.layout_with_groupBoxes.addWidget(self.groupBox_movie1)
        self.groupBox_movie2 = QtWidgets.QGroupBox(self.layout_with_group_boxes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_movie2.sizePolicy().hasHeightForWidth())
        self.groupBox_movie2.setSizePolicy(sizePolicy)
        self.groupBox_movie2.setMinimumSize(QtCore.QSize(200, 300))
        self.groupBox_movie2.setStyleSheet("QGroupBox {\n"
"    /*background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #CC99FF, stop: 1 #CCCCFF);*/\n"
"    background: #666;\n"
"    border: 5px solid #c7bfe6;\n"
"    border-radius: 0px;\n"
"    margin-top: 5px;\n"
"    margin-bottom: 5px;\n"
"}\n"
"QGroupBox QLabel {\n"
"    background: transparent;\n"
"}")
        self.groupBox_movie2.setTitle("")
        self.groupBox_movie2.setObjectName("groupBox_movie2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_movie2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_movie2_title = QtWidgets.QLabel(self.groupBox_movie2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_movie2_title.sizePolicy().hasHeightForWidth())
        self.label_movie2_title.setSizePolicy(sizePolicy)
        self.label_movie2_title.setStyleSheet("font: 20pt \"Arial\";\n"
"color: rgb(198, 190, 229);")
        self.label_movie2_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_movie2_title.setObjectName("label_movie2_title")
        self.verticalLayout_6.addWidget(self.label_movie2_title)
        spacerItem1 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem1)
        self.layout_movie2_ifno = QtWidgets.QVBoxLayout()
        self.layout_movie2_ifno.setObjectName("layout_movie2_ifno")
        self.label_movie2_producer = QtWidgets.QLabel(self.groupBox_movie2)
        self.label_movie2_producer.setStyleSheet("color: rgb(198, 190, 229);")
        self.label_movie2_producer.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_movie2_producer.setObjectName("label_movie2_producer")
        self.layout_movie2_ifno.addWidget(self.label_movie2_producer)
        self.label = QtWidgets.QLabel(self.groupBox_movie2)
        self.label.setStyleSheet("color: #c3c3c3;")
        self.label.setObjectName("label")
        self.layout_movie2_ifno.addWidget(self.label, 0, QtCore.Qt.AlignRight)
        self.label_movie2_rating = QtWidgets.QLabel(self.groupBox_movie2)
        self.label_movie2_rating.setStyleSheet("color: #FFD700;")
        self.label_movie2_rating.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_movie2_rating.setObjectName("label_movie2_rating")
        self.layout_movie2_ifno.addWidget(self.label_movie2_rating)
        self.label_movie2_genre = QtWidgets.QLabel(self.groupBox_movie2)
        self.label_movie2_genre.setStyleSheet("color: #c3c3c3;")
        self.label_movie2_genre.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_movie2_genre.setObjectName("label_movie2_genre")
        self.layout_movie2_ifno.addWidget(self.label_movie2_genre)
        self.verticalLayout_6.addLayout(self.layout_movie2_ifno)
        self.layout_with_groupBoxes.addWidget(self.groupBox_movie2)
        self.main_layout.addWidget(self.layout_with_group_boxes)
        spacerItem2 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.main_layout.addItem(spacerItem2)
        self.layout_bottom_part = QtWidgets.QHBoxLayout()
        self.layout_bottom_part.setObjectName("layout_bottom_part")
        spacerItem3 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.layout_bottom_part.addItem(spacerItem3)
        self.layout_which_movie_better = QtWidgets.QVBoxLayout()
        self.layout_which_movie_better.setObjectName("layout_which_movie_better")
        self.label_which_movie_better = QtWidgets.QLabel(WidgetQuizRound)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_which_movie_better.sizePolicy().hasHeightForWidth())
        self.label_which_movie_better.setSizePolicy(sizePolicy)
        self.label_which_movie_better.setStyleSheet("font: 20pt \"Arial\";")
        self.label_which_movie_better.setAlignment(QtCore.Qt.AlignCenter)
        self.label_which_movie_better.setObjectName("label_which_movie_better")
        self.layout_which_movie_better.addWidget(self.label_which_movie_better)
        self.slider = QtWidgets.QSlider(WidgetQuizRound)
        self.slider.setMinimumSize(QtCore.QSize(0, 40))
        self.slider.setStyleSheet("QSlider::groove:horizontal {\n"
"    height: 5px; \n"
"    background-color: #c3c3c3;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #837f98;\n"
"    width: 10px; /* Ширина ползунка */\n"
"    margin: -15px 0; /* Смещение ползунка */\n"
"    border-radius: 3px;\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: #c6bee3;\n"
"}")
        self.slider.setMaximum(20)
        self.slider.setPageStep(1)
        self.slider.setProperty("value", 10)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.layout_which_movie_better.addWidget(self.slider)
        self.layout_percents = QtWidgets.QHBoxLayout()
        self.layout_percents.setObjectName("layout_percents")
        self.label_left_10 = QtWidgets.QLabel(WidgetQuizRound)
        self.label_left_10.setObjectName("label_left_10")
        self.layout_percents.addWidget(self.label_left_10)
        spacerItem4 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.layout_percents.addItem(spacerItem4)
        self.label_center_0 = QtWidgets.QLabel(WidgetQuizRound)
        self.label_center_0.setObjectName("label_center_0")
        self.layout_percents.addWidget(self.label_center_0, 0, QtCore.Qt.AlignHCenter)
        self.label_right_10 = QtWidgets.QLabel(WidgetQuizRound)
        self.label_right_10.setObjectName("label_right_10")
        self.layout_percents.addWidget(self.label_right_10, 0, QtCore.Qt.AlignRight)
        self.layout_which_movie_better.addLayout(self.layout_percents)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layout_which_movie_better.addItem(spacerItem5)
        self.layout_bottom_part.addLayout(self.layout_which_movie_better)
        self.btn_next_round = QtWidgets.QPushButton(WidgetQuizRound)
        self.btn_next_round.setMinimumSize(QtCore.QSize(120, 50))
        self.btn_next_round.setStyleSheet("font: 18pt \"Arial\";\n"
"color: #c1c0c5;\n"
"background: #5e5b6e;")
        self.btn_next_round.setObjectName("btn_next_round")
        self.layout_bottom_part.addWidget(self.btn_next_round, 0, QtCore.Qt.AlignBottom)
        self.main_layout.addLayout(self.layout_bottom_part)
        self.verticalLayout_2.addLayout(self.main_layout)

        self.retranslateUi(WidgetQuizRound)
        QtCore.QMetaObject.connectSlotsByName(WidgetQuizRound)

    def retranslateUi(self, WidgetQuizRound):
        _translate = QtCore.QCoreApplication.translate
        WidgetQuizRound.setWindowTitle(_translate("WidgetQuizRound", "Form"))
        self.label_current_round.setText(_translate("WidgetQuizRound", "РАУНД 0/N"))
        self.label_movie1_title.setText(_translate("WidgetQuizRound", "Movie1"))
        self.label_movie1_producer.setText(_translate("WidgetQuizRound", "Режисер:"))
        self.label_movie1_region.setText(_translate("WidgetQuizRound", "Страна:"))
        self.label_movie1_rating.setText(_translate("WidgetQuizRound", "Рейтинг:"))
        self.label_movie1_genre.setText(_translate("WidgetQuizRound", "Жанр:"))
        self.label_movie2_title.setText(_translate("WidgetQuizRound", "Movie2"))
        self.label_movie2_producer.setText(_translate("WidgetQuizRound", "Режисер:"))
        self.label.setText(_translate("WidgetQuizRound", "Страна:"))
        self.label_movie2_rating.setText(_translate("WidgetQuizRound", "Рейтинг:"))
        self.label_movie2_genre.setText(_translate("WidgetQuizRound", "Жанр:"))
        self.label_which_movie_better.setText(_translate("WidgetQuizRound", "КАКОЙ ФИЛЬМ ЛУЧШЕ?"))
        self.label_left_10.setText(_translate("WidgetQuizRound", "10"))
        self.label_center_0.setText(_translate("WidgetQuizRound", "Одинаково"))
        self.label_right_10.setText(_translate("WidgetQuizRound", "10"))
        self.btn_next_round.setText(_translate("WidgetQuizRound", "ДАЛЕЕ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WidgetQuizRound = QtWidgets.QWidget()
    ui = Ui_WidgetQuizRound()
    ui.setupUi(WidgetQuizRound)
    WidgetQuizRound.show()
    sys.exit(app.exec_())
