import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def window():
   app = QApplication(sys.argv)
   widget = QWidget()

   textLabel = QLabel(widget)
   textLabel.setText("Hello World!")
   textLabel.move(110,85)

   widget.setGeometry(100,100,500,500)
   widget.setWindowTitle("Seniority_helper")
   widget.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   window()
