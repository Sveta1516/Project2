from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import * 
from final_win import*
from instr import *
class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()
    def initUI(self):
        self.btn_next = QPushButton(txt_next, self)
        self.btn1_next = QPushButton(txt_next, self)
        self.btn2_next = QPushButton(txt_next, self)
        self.btn3_next = QPushButton(txt_next, self)
        self.hello_text =  QLabel(txt_hello)
        self.hello1_text = QLabel(txt_hello)
        self.hello2_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.instruction2 = QLabel(txt_instruction)
        self.time = QLabel(txt_timer)
        self.lines = QLineEdit(txt_age)
        self.lines1 = QLineEdit(txt_age)
        self.lines2 = QLineEdit(txt_age)
        self.lines3 = QLineEdit(txt_age)
        self.lines4 = QLineEdit(txt_age)
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.lines, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.hello1_text, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.lines1, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.hello2_text, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.btn1_next, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.lines2, alignment = Qt.AlignLeft)
        self.layout_line1 = QHBoxLayout()
        self.layout_line1.addWidget(self.instruction, alignment = Qt.AlignLeft)
        self.layout_line1.addWidget(self.time, alignment = Qt.AlignRight)
        
        self.layout_line.addLayout(self.layout_line1)
        self.layout_line.addWidget(self.btn2_next, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.instruction2, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.btn3_next, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.lines3, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.lines4, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        
        self.setLayout(self.layout_line)
    def next_click(self):
        self.tw = FWin()
        self.hide()
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
    def set_appear(self):
        win_x, win_y = 200, 100
        win_width, win_height = 1000, 600
        self.setWindowTitle('txt_title')
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

