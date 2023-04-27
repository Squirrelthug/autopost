import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from ui.media_selection import MediaSelection
from ui.media_display import MediaDisplay
from ui.posted_media_list import PostedMediaList

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Social Media Manager')

        # Create media_display and media_selection instances
        self.media_display = MediaDisplay()
        self.media_selection = MediaSelection(self.media_display)
        self.posted_media_list = PostedMediaList()

        # Create a main layout and add media_display, media_selection, and posted_media_list
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.media_selection)
        main_layout.addWidget(self.media_display)
        main_layout.addWidget(self.posted_media_list)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
