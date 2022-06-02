from main import *

GLOBAL_STATE = 0

class UIFunctions(MainWindow):

    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        if status == 0:
            self.showMaximized()

            GLOBAL_STATE = 1

            self.ui.drop_shadow_layout.setContentsMargins(0,0,0,0)
            self.ui.drop_shadow_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1,"
                 " x2:0.006, y2:0.0340909, stop:0.289773 rgba(17, 15, 38, 255), stop:1 rgba(76, 44, 76, 255));"
                                                    "border-radius: 0px;")
            self.ui.btn_maximize.setToolTip("Restore")

        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.widht()+1, self.height()+1)
            self.ui.drop_shadow_layout.setContentsMargins(10,10,10,10)
            self.ui.drop_shadow_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1,"
                " x2:0.006, y2:0.0340909, stop:0.289773 rgba(17, 15, 38, 255), stop:1 rgba(76, 44, 76, 255));"
                                                                                       "border-radius: 10px;")
            self.ui.btn_maximize.setToolTip("Maximize")

    def uiDefinitions(self):

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,0,0,100))

        self.ui.drop_shadow_frame.setGraphicsEffect(self.shadow)
        self.ui.btn_maximize.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        self.ui.btn_close.clicked.connect(lambda: self.close())
#        self.sizegrip = QSizeGrip(self.ui.frame_grip)
#        self.sizegrip.setStyleSheet("QSizeGrip { widht: 10 px; height: 10px; margin: 5px } QSizeGrip:hover { backgrount-color: rgb(50,42,94)}")
#        self.sizegrip.setToolTip("Resize window")

    def returnStatus():
        return GLOBAL_STATE

