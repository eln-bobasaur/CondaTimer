import sys
from PyQt6.QtCore import QSize, Qt, QElapsedTimer, QTimer
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QKeyEvent, QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("CondaTimer")
        
        self.label = QLabel("Press Space to Start", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont("Arial", 45)
        self.label.setFont(font)
        
        self.setCentralWidget(self.label)
        
        self.elapsed_timer = QElapsedTimer()
        self.update_timer = QTimer(self)
        
        self.update_timer.timeout.connect(self.update_display)

        self.setFixedSize(QSize(750, 600))
        
        self.running = False    
           
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Space:
            if not self.running:
                self.elapsed_timer.start()
                self.update_timer.start(50)
                self.running = True
            else:
                self.update_timer.stop()
                self.update_display(final=True)
                self.running = False
                
            
    def update_display(self, final = False):
        elapsed_ms = self.elapsed_timer.elapsed()
        seconds = elapsed_ms / 1000
        
        if final:
            self.label.setText(f"{seconds:.3f} seconds")
        else:
            self.label.setText(f"{seconds:.3f} seconds")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())