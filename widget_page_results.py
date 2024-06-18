from PyQt5.QtWidgets import QWidget

from ui.ui_results import Ui_WidgetResults


class WidgetPageResults(QWidget):
    def __init__(self, parent=None):
        super(WidgetPageResults, self).__init__(parent)
        self.ui = Ui_WidgetResults()
        self.ui.setupUi(self)
