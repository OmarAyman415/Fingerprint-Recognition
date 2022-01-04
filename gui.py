import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# >>>>>>>>>>>>>>>>>> forth page (Result) <<<<<<<<<<<<<<<<<<
class Forth(QMainWindow):
    def __init__(self, parent=None):
        super(Forth, self).__init__(parent)
        self.resize(800, 600)
        self.setWindowTitle("Result")
        #### Label1
        label1 = QLabel(self, text='<b>This Id image is 00001</b>')
        label1.resize(500, 30)
        label1.setFont(QFont('Arial', 20))
        label1.move(170, 50)
        #### Label2
        label2 = QLabel(self, text='<b> Accuracy is : 0,7954</b>')
        label2.resize(500, 30)
        label2.setFont(QFont('Arial', 20))
        label2.move(180, 150)
        #### img
        img1 = QPixmap('00001_67.bmp')
        img1_label = QLabel(self)
        img1_label.resize(500, 300)
        img1_label.move(170, 200)
        img1_label.setPixmap(img1)
        #### button
        btn1 = QPushButton('Close', self)
        btn1.clicked.connect(self.on_pushButton_clicked)
        btn1.move(300, 500)

    def on_pushButton_clicked(self):
        # self.close()
        sys.exit()


# >>>>>>>>>>>>>>>>>> third page (Import image) <<<<<<<<<<<<<<<<<<

class Third(QMainWindow):
    def __init__(self, parent=None):
        super(Third, self).__init__(parent)
        self.resize(800, 600)
        self.setWindowTitle("Import image")
        # button
        pushButton = QPushButton("click me", self)
        pushButton.resize(200, 50)
        pushButton.move(300, 500)
        pushButton.clicked.connect(self.on_pushButton_clicked)
        self.dialog = Forth(self)

    def on_pushButton_clicked(self):
        self.dialog.show()


# >>>>>>>>>>>>>>>>>> second page (Graphs) <<<<<<<<<<<<<<<<<<

class Second(QMainWindow):
    def __init__(self, parent=None):
        super(Second, self).__init__(parent)
        self.resize(800, 600)
        self.setWindowTitle("Graphs")
        #### Label1
        label1 = QLabel(self, text='<b>Visualising the Training set results</b>')
        label1.resize(500, 30)
        label1.setFont(QFont('Arial', 15))
        label1.move(170, 50)
        #### Label2
        label2 = QLabel(self, text='<b>Visualising the Test set results</b>')
        label2.resize(500, 30)
        label2.setFont(QFont('Arial', 15))
        label2.move(180, 250)
        # button
        pushButton = QPushButton("click me", self)
        pushButton.resize(200, 50)
        pushButton.move(300, 500)
        pushButton.clicked.connect(self.on_pushButton_clicked)
        self.dialog = Third(self)

    def on_pushButton_clicked(self):
        self.dialog.show()


# >>>>>>>>>>>>>>>>>> first page (introduction of project) <<<<<<<<<<<<<<<<<<

class First(QMainWindow):
    def __init__(self, parent=None):
        super(First, self).__init__(parent)
        self.resize(800, 600)
        self.setWindowTitle("Introduction of Project")
        #### Label
        label = QLabel(self, text='<b>Finger print recognition project</b>')
        label.resize(500, 30)
        label.setFont(QFont('Arial', 20))
        label.move(180, 200)
        #### button
        pushButton = QPushButton("click me", self)
        pushButton.resize(200, 50)
        pushButton.move(300, 350)
        pushButton.clicked.connect(self.on_pushButton_clicked)
        self.dialog = Second(self)

    def on_pushButton_clicked(self):
        self.dialog.show()
        # self.close()


def main():
    app = QApplication(sys.argv)
    main = First()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
