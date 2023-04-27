from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class MediaDisplay(QWidget):
    """
    MediaDisplay class displays the selected media as thumbnail images in a grid layout.
    """
    def __init__(self):
        super().__init__()

        # Create a grid layout to display the media thumbnails
        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)

    def update_media(self, file_paths):
        """
        Takes a list of file paths and displays the media in a grid layout as thumbnail images,:param file_paths: List of file paths to be displayed as thumbnails.
        """
        # Remove all existing widgets from the grid layout
        for i in reversed(range(self.grid_layout.count())):
            widget = self.grid_layout.itemAt(i).widget()
            self.grid_layout.removeWidget(widget)
            widget.setParent(None)

        # Iterate through the file paths and create thumbnails
        for idx, file_path in enumerate(file_paths):
            pixmap = QPixmap(file_path)
            scaled_pixmap = pixmap.scaled(100, 100, Qt.KeepAspectRatio)
            label = QLabel()
            label.setPixmap(scaled_pixmap)

            # Add the thumbnail to the grid layout
            row = idx // 4
            col = idx % 4
            self.grid_layout.addWidget(label, row, col)
