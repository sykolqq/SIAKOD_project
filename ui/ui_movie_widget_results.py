# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_movie_widget_results.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MovieWidget_results(object):
    def setupUi(self, MovieWidget_results):
        MovieWidget_results.setObjectName("MovieWidget_results")
        MovieWidget_results.resize(910, 188)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MovieWidget_results.sizePolicy().hasHeightForWidth())
        MovieWidget_results.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        MovieWidget_results.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(MovieWidget_results)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_results = QtWidgets.QGroupBox(MovieWidget_results)
        self.groupBox_results.setStyleSheet("#groupBox_results {\n"
"    border: none;\n"
"}")
        self.groupBox_results.setTitle("")
        self.groupBox_results.setObjectName("groupBox_results")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_results)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_place = QtWidgets.QLabel(self.groupBox_results)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_place.sizePolicy().hasHeightForWidth())
        self.label_place.setSizePolicy(sizePolicy)
        self.label_place.setObjectName("label_place")
        self.horizontalLayout_2.addWidget(self.label_place)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.groupBox_movie = QtWidgets.QGroupBox(self.groupBox_results)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_movie.sizePolicy().hasHeightForWidth())
        self.groupBox_movie.setSizePolicy(sizePolicy)
        self.groupBox_movie.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_movie.setFont(font)
        self.groupBox_movie.setStyleSheet("QGroupBox {\n"
"    background: #2e2e2e;\n"
"    border: 4px solid #c5bfe5;\n"
"    border-radius: 0px;\n"
"    margin-top: 2ex;\n"
" } \n"
"QGroupBox::title {\n"
"    \n"
"    color: #c6bfe5;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"} ")
        self.groupBox_movie.setObjectName("groupBox_movie")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_movie)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.vlayout_genres = QtWidgets.QVBoxLayout()
        self.vlayout_genres.setObjectName("vlayout_genres")
        self.label_genres = QtWidgets.QLabel(self.groupBox_movie)
        self.label_genres.setStyleSheet("color: #c3c3c3;")
        self.label_genres.setObjectName("label_genres")
        self.vlayout_genres.addWidget(self.label_genres, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout.addLayout(self.vlayout_genres)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.vlayout_info = QtWidgets.QVBoxLayout()
        self.vlayout_info.setObjectName("vlayout_info")
        spacerItem2 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vlayout_info.addItem(spacerItem2)
        self.label_director = QtWidgets.QLabel(self.groupBox_movie)
        self.label_director.setStyleSheet("color: rgb(198, 190, 229)")
        self.label_director.setObjectName("label_director")
        self.vlayout_info.addWidget(self.label_director)
        self.label_region = QtWidgets.QLabel(self.groupBox_movie)
        self.label_region.setStyleSheet("color: #c3c3c3;")
        self.label_region.setObjectName("label_region")
        self.vlayout_info.addWidget(self.label_region)
        self.label_rating = QtWidgets.QLabel(self.groupBox_movie)
        self.label_rating.setStyleSheet("color: #FFD700;")
        self.label_rating.setObjectName("label_rating")
        self.vlayout_info.addWidget(self.label_rating)
        self.horizontalLayout.addLayout(self.vlayout_info)
        self.horizontalLayout_2.addWidget(self.groupBox_movie)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.label_percents = QtWidgets.QLabel(self.groupBox_results)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_percents.sizePolicy().hasHeightForWidth())
        self.label_percents.setSizePolicy(sizePolicy)
        self.label_percents.setObjectName("label_percents")
        self.horizontalLayout_2.addWidget(self.label_percents)
        self.verticalLayout.addWidget(self.groupBox_results)

        self.retranslateUi(MovieWidget_results)
        QtCore.QMetaObject.connectSlotsByName(MovieWidget_results)

    def retranslateUi(self, MovieWidget_results):
        _translate = QtCore.QCoreApplication.translate
        MovieWidget_results.setWindowTitle(_translate("MovieWidget_results", "Form"))
        self.label_place.setText(_translate("MovieWidget_results", "1 место"))
        self.groupBox_movie.setTitle(_translate("MovieWidget_results", "Movie_name"))
        self.label_genres.setText(_translate("MovieWidget_results", "Жанры:"))
        self.label_director.setText(_translate("MovieWidget_results", "Режисер:"))
        self.label_region.setText(_translate("MovieWidget_results", "Страна:"))
        self.label_rating.setText(_translate("MovieWidget_results", "Рейтинг:"))
        self.label_percents.setText(_translate("MovieWidget_results", "99.99%"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MovieWidget_results = QtWidgets.QWidget()
    ui = Ui_MovieWidget_results()
    ui.setupUi(MovieWidget_results)
    MovieWidget_results.show()
    sys.exit(app.exec_())
