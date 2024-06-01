from PyQt5.QtWidgets import QWidget

from ui.ui_choose_count_of_members import Ui_Form


class WidgetCountOfMembers(QWidget):
    def __init__(self, parent=None):
        super(WidgetCountOfMembers, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

