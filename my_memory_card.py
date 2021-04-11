#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,QWidget,QLabel,QPushButton,QVBoxLayout,QMessageBox,QHBoxLayout,QRadioButton,QGroupBox,QButtonGroup
)
from random import shuffle,randint
class Question():
    def __init__(self,question,right_ans,wrong_1,wrong_2,wrong_3):
        self.question = question
        self.right_ans = right_ans
        self.wrong_1 = wrong_1
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_3
question_list = []

question_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский'))
question_list.append(Question('Какого цвета нет на флаге России?','Зелёный','Красный','Белый','Синий'))
question_list.append(Question('Национальная хижина якутов','Ураса','Юрта','Иглу','Хата'))
app = QApplication([])

window = QWidget()
window.setWindowTitle("Memory Card")

rbt1 = QRadioButton("Энцы")
rbt2 = QRadioButton("Энцы")
rbt3 = QRadioButton("Энцы")
rbt4 = QRadioButton("Энцы")

RGB = QGroupBox("Варианты ответов")
lb_question = QLabel("Тестовый вопрос")
ok = QPushButton("Ответит")
layout_main = QVBoxLayout()
line_1 = QHBoxLayout()
line_2 = QHBoxLayout()
line_3 = QHBoxLayout()
layout_ans = QHBoxLayout()
layout_ans1 = QVBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans1.addWidget(rbt1)
layout_ans1.addWidget(rbt2)
layout_ans2.addWidget(rbt3)
layout_ans2.addWidget(rbt4)
layout_ans.addLayout(layout_ans1)
layout_ans.addLayout(layout_ans2)
RGB.setLayout(layout_ans)
radio_group = QButtonGroup()
radio_group.addButton(rbt1)
radio_group.addButton(rbt2)
radio_group.addButton(rbt3)
radio_group.addButton(rbt4)
ANS = QGroupBox("Результаты ответа")
result = QLabel("Прав ли или нет?")
correct = QLabel("Тут будет ответ!")
layout_res = QVBoxLayout()
layout_res.addWidget(result, alignment =(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(correct, alignment=(Qt.AlignHCenter), stretch=2)
ANS.setLayout(layout_res)
ANS.hide() 
line_1.addWidget(lb_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
line_2.addWidget(RGB)
line_2.addWidget(ANS)
line_3.addWidget(ok, stretch=2)
line_3.addStretch(1)
layout_main.addLayout(line_1, stretch=2)
layout_main.addLayout(line_2, stretch=8)
layout_main.addStretch(1)
layout_main.addLayout(line_3, stretch=1)
layout_main.addStretch(1)
layout_main.setSpacing(5)
answer = [rbt1, rbt2, rbt3, rbt4]
def ask(q:Question):
    shuffle(answer)
    answer[0].setText(q.right_ans)
    answer[1].setText(q.wrong_1)
    answer[2].setText(q.wrong_2)
    answer[3].setText(q.wrong_3)
    lb_question.setText(q.question)
    correct.setText(q.right_ans)
    show_question()
def next_quest():
    cur_quest = randint(0,len(question_list)-1)
    q = question_list[cur_quest]
    ask(q)


def check():
    if answer[0].isChecked():
        result.setText("Правильно")   
    else:
        result.setText("Не правильно")
    show_result()



def show_result():
    RGB.hide()
    ANS.show()
    ok.setText("Следующий вопрос")
def show_question():
    RGB.show()
    ANS.hide()
    ok.setText("Ответить")
    radio_group.setExclusive(False)
    rbt1.setChecked(False)
    rbt2.setChecked(False)
    rbt3.setChecked(False)
    rbt4.setChecked(False)
    radio_group.setExclusive(True)
def start_test():
    if ok.text() == 'Ответить':
        check()
    else:
        next_quest()
next_quest()
layout_main.addWidget(RGB)
window.setLayout(layout_main)
ok.clicked.connect(start_test)
window.show()
window.resize(400,300)
app.exec_()
