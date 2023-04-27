from PyQt5.QtWidgets import QListWidget, QListWidgetItem
from datetime import date

class PostedMediaList(QListWidget):
    """
    PostedMediaList class displays the list of posted media in a QListWidget.
    """

    def __init__(self):
        super().__init__()

    def add_media(self, file_path):
        """
        Adds a media item to the list with the corresponding post date.
        :param file_path: The file path of the media item to be added to the list.
        """
        item = QListWidgetItem(f"{file_path} - {date.today()}")
        self.addItem(item)

    def is_media_posted(self, file_path):
        """
        Checks if the given media has been posted before.
        :param file_path: The file path of the media to check.
        :return: A list of dates the media was posted on, or an empty list if the media hasn't been posted.
        """
        posted_dates = []
        for i in range(self.count()):
            item_text = self.item(i).text()
            if item_text.startswith(file_path):
                posted_dates.append(item_text.split(" - ")[1])
        return posted_dates
