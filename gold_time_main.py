__author__ = 'sshejko'

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QSystemTrayIcon
import gold_time_lib
import sys
import os
import datetime

class MainWindow(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        # adding icon and systray icon
        #if os.path.exists('gold_time.png'):
        #    self.setWindowIcon(QtGui.QIcon('gold_time.png'))
        #    self.trayIcon = QtGui.QSystemTrayIcon(QtGui.QIcon('gold_time.png'))
        #elif os.path.exists(sys.argv[0][:0 - len('gold_time_main.py')] + 'gold_time.png'):
        #    self.setWindowIcon(QtGui.QIcon(sys.argv[0][:0 - len('gold_time_main.py')] + 'gold_time.png'))
        #    self.trayIcon = QtGui.QSystemTrayIcon(QtGui.QIcon(sys.argv[0][:0 - len('gold_time_main.py')] + 'gold_time.png'))

        self.setWindowIcon(QtGui.QIcon('gold_time.png'))
        self.trayIcon = QtGui.QSystemTrayIcon(QtGui.QIcon('gold_time.png'))

        self.trayIcon.show()

        self.trayIcon.showMessage('Current time', str(datetime.datetime.now()), QSystemTrayIcon.Information, 10000)

        #set timer
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(10000)
        self.timer.timeout.connect(self.run_app)
        self.timer.start()

        # set first tooltip
        wake_time = gold_time_lib.get_gold_time()
        cur_time = datetime.datetime.now()
        utc_time = datetime.datetime.utcnow()
        delta_time = cur_time - utc_time
        morn_med_time = datetime.datetime(year=cur_time.year, month=cur_time.month, day=cur_time.day, hour=7)
        evn_med_time = datetime.datetime(year=cur_time.year, month=cur_time.month, day=cur_time.day, hour=19)
        base_meditation_time_m = morn_med_time + delta_time
        base_meditation_time_e = evn_med_time + delta_time

        self.trayIcon.setToolTip('Gold time today at \n ' + str(wake_time) + '\n Meditation time at: \n' + str(base_meditation_time_m) + '\nand\n' + str(base_meditation_time_e))

        exitAction = QtGui.QAction('&Exit', self)
        #exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.closeEvent)

        show_message_Action = QtGui.QAction('&Show times', self)
        #show_message_Action.setStatusTip('Show times')
        show_message_Action.triggered.connect(self.show_message)
        
        menu = QtGui.QMenu(self)
        menu.addAction(exitAction)
        menu.addAction(show_message_Action)
        self.trayIcon.setContextMenu(menu)

    def run_app(self):
        cur_time = datetime.datetime.now()
        utc_time = datetime.datetime.utcnow()
        delta_time = cur_time - utc_time
        morn_med_time = datetime.datetime(year=cur_time.year, month=cur_time.month, day=cur_time.day, hour=7)
        evn_med_time = datetime.datetime(year=cur_time.year, month=cur_time.month, day=cur_time.day, hour=19)
        base_meditation_time_m = morn_med_time + delta_time
        base_meditation_time_e = evn_med_time + delta_time

        wake_time = gold_time_lib.get_gold_time()
        # One minute
        if (int(round(((wake_time-cur_time).total_seconds()), 0)) in range(290, 301)) or \
                int(round(((base_meditation_time_m-cur_time).total_seconds()), 0)) in range(290, 301) or \
                int(round(((base_meditation_time_e-cur_time).total_seconds()), 0)) in range(290, 301):
            self.trayIcon.showMessage('Time is coming!', 'Gold time today at \n ' + str(wake_time) + '\n Meditation time at: \n' + str(base_meditation_time_m) + '\nand\n' + str(base_meditation_time_e), QSystemTrayIcon.Information, 10000)

        # 5 minutes
        if (int(round(((wake_time-cur_time).total_seconds()), 0)) in range(50, 61)) or \
                int(round(((base_meditation_time_m-cur_time).total_seconds()), 0)) in range(50, 61) or \
                int(round(((base_meditation_time_e-cur_time).total_seconds()), 0)) in range(50, 61):
            self.trayIcon.showMessage('Time is coming!', 'Gold time today at \n ' + str(wake_time) + '\n Meditation time at: \n' + str(base_meditation_time_m) + '\nand\n' + str(base_meditation_time_e), QSystemTrayIcon.Information, 10000)

        self.trayIcon.setToolTip('Gold time today at \n ' + str(wake_time) + '\n Meditation time at: \n' + str(base_meditation_time_m) + '\nand\n' + str(base_meditation_time_e))
     
     
    def show_message(self):
        cur_time = datetime.datetime.now()
        utc_time = datetime.datetime.utcnow()
        delta_time = cur_time - utc_time
        morn_med_time = datetime.datetime(year=cur_time.year, month=cur_time.month, day=cur_time.day, hour=7)
        evn_med_time = datetime.datetime(year=cur_time.year, month=cur_time.month, day=cur_time.day, hour=19)
        base_meditation_time_m = morn_med_time + delta_time
        base_meditation_time_e = evn_med_time + delta_time

        wake_time = gold_time_lib.get_gold_time()
        mess = 'Gold time today at \n ' + str(wake_time) + '\n Meditation time at: \n' + str(base_meditation_time_m) + '\nand\n' + str(base_meditation_time_e)
        self.trayIcon.showMessage('Times', mess, QSystemTrayIcon.Information, 10000)

    # http://stackoverflow.com/questions/5506781/pyqt4-application-on-windows-is-crashing-on-exit
    def closeEvent(self, event):
        sys.exit(0)


app = QtGui.QApplication(sys.argv)
w = MainWindow()
#w.show()
sys.exit(app.exec_())