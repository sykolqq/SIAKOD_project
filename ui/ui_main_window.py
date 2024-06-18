# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 800))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(51, 51, 51);\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"Arial\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setStyleSheet("QTabBar::tab {\n"
"    background: #333333;\n"
"    min-width: 8ex;\n"
"    padding: 10px 2px 2px 15px;\n"
"\n"
"    display: flex;\n"
"    justify-content: space-between;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background: #666;\n"
"}\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px;\n"
"}\n"
"")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget.setIconSize(QtCore.QSize(40, 40))
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_quiz_list = QtWidgets.QWidget()
        self.tab_quiz_list.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tab_quiz_list.setStyleSheet("")
        self.tab_quiz_list.setObjectName("tab_quiz_list")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_quiz_list)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.quizlist_text_layout = QtWidgets.QHBoxLayout()
        self.quizlist_text_layout.setObjectName("quizlist_text_layout")
        self.text_movie_for_quiz = QtWidgets.QLabel(self.tab_quiz_list)
        self.text_movie_for_quiz.setStyleSheet("font: 75 italic 18pt \"Helvetica\";\n"
"color: #c5bfe5;\n"
"border-bottom: 2px solid #c5bfe5;\n"
"padding-bottom: 10px;")
        self.text_movie_for_quiz.setObjectName("text_movie_for_quiz")
        self.quizlist_text_layout.addWidget(self.text_movie_for_quiz)
        self.verticalLayout_2.addLayout(self.quizlist_text_layout)
        self.movie_widgets_scrollArea = QtWidgets.QScrollArea(self.tab_quiz_list)
        self.movie_widgets_scrollArea.setStyleSheet("QScrollBar:vertical {\n"
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
        self.movie_widgets_scrollArea.setWidgetResizable(True)
        self.movie_widgets_scrollArea.setObjectName("movie_widgets_scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1162, 659))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.movie_widgets_for_quiz_layout = QtWidgets.QVBoxLayout()
        self.movie_widgets_for_quiz_layout.setObjectName("movie_widgets_for_quiz_layout")
        self.horizontalLayout_3.addLayout(self.movie_widgets_for_quiz_layout)
        self.movie_widgets_scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.movie_widgets_scrollArea)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/quiz_list_icon.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_quiz_list, icon, "")
        self.tab_search = QtWidgets.QWidget()
        self.tab_search.setAutoFillBackground(False)
        self.tab_search.setObjectName("tab_search")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_search)
        self.verticalLayout.setObjectName("verticalLayout")
        self.search_line_layout = QtWidgets.QHBoxLayout()
        self.search_line_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.search_line_layout.setSpacing(0)
        self.search_line_layout.setObjectName("search_line_layout")
        self.label_search = QtWidgets.QLineEdit(self.tab_search)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_search.sizePolicy().hasHeightForWidth())
        self.label_search.setSizePolicy(sizePolicy)
        self.label_search.setMinimumSize(QtCore.QSize(0, 40))
        self.label_search.setStyleSheet("border: 2px solid #c5bfe5;")
        self.label_search.setFrame(True)
        self.label_search.setObjectName("label_search")
        self.search_line_layout.addWidget(self.label_search)
        self.btn_delete = QtWidgets.QPushButton(self.tab_search)
        self.btn_delete.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_delete.setStyleSheet("background-color: rgb(94, 91, 110);\n"
"")
        self.btn_delete.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/delete_icon.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.btn_delete.setIcon(icon1)
        self.btn_delete.setIconSize(QtCore.QSize(40, 20))
        self.btn_delete.setCheckable(False)
        self.btn_delete.setAutoRepeat(False)
        self.btn_delete.setAutoExclusive(False)
        self.btn_delete.setAutoDefault(False)
        self.btn_delete.setDefault(False)
        self.btn_delete.setFlat(False)
        self.btn_delete.setObjectName("btn_delete")
        self.search_line_layout.addWidget(self.btn_delete)
        self.btn_search = QtWidgets.QPushButton(self.tab_search)
        self.btn_search.setMinimumSize(QtCore.QSize(100, 40))
        self.btn_search.setStyleSheet("background-color: rgb(94, 91, 110);\n"
"")
        self.btn_search.setCheckable(False)
        self.btn_search.setAutoRepeat(False)
        self.btn_search.setAutoExclusive(False)
        self.btn_search.setAutoDefault(False)
        self.btn_search.setDefault(False)
        self.btn_search.setFlat(False)
        self.btn_search.setObjectName("btn_search")
        self.search_line_layout.addWidget(self.btn_search)
        self.verticalLayout.addLayout(self.search_line_layout)
        self.search_scrollArea = QtWidgets.QScrollArea(self.tab_search)
        self.search_scrollArea.setStyleSheet("QScrollBar:vertical {\n"
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
        self.search_scrollArea.setWidgetResizable(True)
        self.search_scrollArea.setObjectName("search_scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 1162, 612))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.search_movie_widgets_layout = QtWidgets.QVBoxLayout()
        self.search_movie_widgets_layout.setObjectName("search_movie_widgets_layout")
        self.horizontalLayout_4.addLayout(self.search_movie_widgets_layout)
        self.search_scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout.addWidget(self.search_scrollArea)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_start_quiz = QtWidgets.QPushButton(self.tab_search)
        self.btn_start_quiz.setEnabled(False)
        self.btn_start_quiz.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_start_quiz.setMaximumSize(QtCore.QSize(800, 16777215))
        self.btn_start_quiz.setStyleSheet("background-color: rgb(94, 91, 110);")
        self.btn_start_quiz.setObjectName("btn_start_quiz")
        self.horizontalLayout_5.addWidget(self.btn_start_quiz)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/search_icon.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_search, icon2, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Movie"))
        self.text_movie_for_quiz.setText(_translate("MainWindow", "Фильмы на опрос"))
        self.label_search.setPlaceholderText(_translate("MainWindow", "Введите название фильма..."))
        self.btn_search.setText(_translate("MainWindow", "Найти"))
        self.btn_start_quiz.setText(_translate("MainWindow", "Начать опрос"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
