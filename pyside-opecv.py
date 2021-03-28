from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import cv2

def displayFrame():
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    h, w = frame.shape[:2]
    # cv::Mat -> Qt(numpy.array)
    image = QImage(frame.flatten(), w, h, QImage.Format_RGB888) 
    label.setPixmap(QPixmap.fromImage(image))

app = QApplication()
window = QWidget()

# pc Webcam
cap = cv2.VideoCapture(0)

# timer surekli hareket
timer = QTimer()
timer.timeout.connect(displayFrame)
timer.start(33) # [msec]

# ilk label arka tarafa sdusuyor bunu hbocx icine atabilrisiniz ...
label = QLabel(' Camera Feed')  
layout = QVBoxLayout()
layout.addWidget(label)
window.setLayout(layout)
window.setWindowTitle("Camera")
window.show()
app.exec_()
