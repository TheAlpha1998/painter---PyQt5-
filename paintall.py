import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()


        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 300)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)

        self.setMouseTracking(True)
        
        button0 = QtWidgets.QPushButton('free',self)
        button0.move(10,10)
        button0.clicked.connect(self.button0)
        
        button1 = QtWidgets.QPushButton('line',self)
        button1.move(10,40)
        button1.clicked.connect(self.button1)

        button2 = QtWidgets.QPushButton('ellipse',self)
        button2.move(10,70)
        button2.clicked.connect(self.button2)
        
        button3 = QtWidgets.QPushButton('rect',self)
        button3.move(10,100)
        button3.clicked.connect(self.button3)

        self.last_x, self.last_y = None, None
        self.rel_x, self.rel_y = None, None
        self.press_x, self.press_y=None, None
        self.x,self.y = None, None
        self.option = 0

    def button0(self):
        print ("print free")
        self.option = 0

    def button1(self):
        print ("print line")
        self.option = 1
        
    def button2(self):
        print ("print eclipse")
        self.option = 2
            
    def button3(self):
        print ("print rectangle")
        self.option = 3



        
    def mouseMoveEvent(self, e):
        print ("move",self.option)
        if self.last_x is None: # First event.
            self.last_x = e.x()
            self.last_y = e.y()
            return # Ignore the first time.

        self.x = e.x()
        self.y = e.y()
        if self.option == 0:
            painter = QtGui.QPainter(self.label.pixmap())
            painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
            painter.end()
            self.update()

        # Update the origin for next time.
        self.last_x = e.x()
        self.last_y = e.y()

    def mousePressEvent(self, e):
        print ("press")
        self.press_x = e.x()
        self.press_y = e.y()
    
        
    def mouseReleaseEvent(self, e):
        print ("release")
        self.rel_x = e.x()
        self.rel_y = e.y()
        self.drawevent()

    def drawevent(self):
        print("hello")
        painter = QtGui.QPainter(self.label.pixmap())
            
        if self.option == 1:
            print ("line",self.last_x,self.x)
            painter.drawLine(self.press_x, self.press_y, self.rel_x, self.rel_y)   
    
        if self.option == 2:
            painter.drawEllipse(self.press_x, self.press_y, self.rel_x, self.rel_y)

        if self.option ==3:
            painter.drawRect(self.press_x, self.press_y, self.rel_x, self.rel_y)

        painter.end()
        self.update()
              
            
        
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
