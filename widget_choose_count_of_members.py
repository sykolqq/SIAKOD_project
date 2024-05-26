from PyQt5.QtWidgets import QWidget

from ui.ui_choose_count_of_members import Ui_WidgetCountOfMembers


class WidgetCountOfMembers(QWidget):
    def __init__(self, parent=None):
        super(WidgetCountOfMembers, self).__init__(parent)
        self.ui = Ui_WidgetCountOfMembers()
        self.ui.setupUi(self)

