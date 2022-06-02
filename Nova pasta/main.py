import os
import sys
from ui_functions import *
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication,QPropertyAnimation,QDate,QDateTime,
                            QMetaObject,QObject,QPoint,QRect,QSize,QTime,QUrl,Qt,QEvent)
from PySide2.QtGui import (QBrush,QColor,QConicalGradient,QCursor,QFont,QFontDatabase,QIcon,
                           QKeySequence,QLinearGradient,QPalette,QPainter,QPixmap,QRadialGradient)
from PySide2.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
from ui_main import Ui_MainWindow
from tkinter import filedialog
from tkinter import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        def moveWindow(event):

            if UIFunctions.returnStatus() == 1:
                UIFunctions.maximize_restore(self)

            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.title_bar.mouseMoveEvent = moveWindow

        UIFunctions.uiDefinitions(self)

        self.ui.bt_open_folder.clicked.connect(self.openFolder)
        self.ui.bt_open_file.clicked.connect(self.openFile)

        self.show()

    def mousePressEvent(self,event):
        self.dragPos = event.globalPos()

    def openFolder(self):
        root = Tk()
        root.withdraw()
        folder = filedialog.askdirectory()
        self.ui.le_folder.setText(str(folder))

    def openFile(self):
        root = Tk()
        root.withdraw()
        file = filedialog.askopenfile()
        self.ui.le_file.setText(str(file))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
