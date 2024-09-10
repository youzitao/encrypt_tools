# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from ui_my_win.my_dialog import yMainWindow
from main_encry import Ui_EncryWindow

if __name__ == '__main__':
    # 适配2k高分辨率屏幕
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    mainWindow = yMainWindow()
    ui = Ui_EncryWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())