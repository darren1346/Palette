from PyQt5.Qt import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.UI_test()
        self.resize(1000,800)


    def UI_test(self):
        btn = QPushButton('Start here!',self)
        btn.move(0,0)
        btn.clicked.connect(self.fun)
        self.btn = btn
        pass

    def fun(self):
        color = QColor(30,40,50)
        color_dialog =QColorDialog(color,self)
        color_dialog.colorSelected.connect(self.change_color)
        color_dialog.setOptions(QColorDialog.NoButtons | QColorDialog.ShowAlphaChannel)  
        color_dialog.currentColorChanged.connect(self.change_color)      
        self.col_dia = color_dialog
        color_dialog.show()

    def change_color(self,col):
        palette = QPalette()
        palette.setColor(QPalette.Background,col)
        self.setPalette(palette)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
