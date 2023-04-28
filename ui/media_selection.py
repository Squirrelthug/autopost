from PyQt5.QtWidgets import QWidget, QFileDialog, QVBoxLayout, QLabel, QPushButton, QMessageBox

class MediaSelection(QWidget):
    """
    MediaSelection class provides UI elements for selecting media files for each social media site.
    """
    def __init__(self, media_display, posted_media_list):
        super().__init__()
        self.media_display = media_display
        self.posted_media_list = posted_media_list
        self.selected_media = {}  # Add this line to initialize the attribute

        layout = QVBoxLayout()

        choose_master_dir_btn = QPushButton("Choose master directory")
        choose_master_dir_btn.clicked.connect(self.choose_master_directory)

        layout.addWidget(choose_master_dir_btn)

        sites = ['Instagram', 'Twitter', 'OnlyFans']
        for site in sites:
            label = QLabel(f"Select media for {site}:")
            button = QPushButton(f"Choose {site} media")
            button.clicked.connect(self.select_media)

            layout.addWidget(label)
            layout.addWidget(button)

        self.setLayout(layout)

    def select_media(self):
        """
        Opens a file dialog to select media files for a specific social media site and updates the MediaDisplay widget with the selected files.
        """
        sender = self.sender()
        site = sender.text().split(' ')[-2]

        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_paths, _ = QFileDialog.getOpenFileNames(self, f"Choose {site} media", self.master_directory, "Images and Videos (*.jpg *.jpeg *.png *.gif *.mp4);;All Files (*)", options=options)
        if file_paths:
            # Store the selected file paths in a dictionary
            self.selected_media[site] = file_paths
            self.media_display.update_media(file_paths)

            # Check if the selected media has been posted before
            for file_path in file_paths:
                posted_dates = self.posted_media_list.is_media_posted(file_path)
                if posted_dates:
                    # Display a notification with the dates the media was posted
                    QMessageBox.information(self, "Previously posted media", f"The media '{file_path}' has been posted before on the following dates: {', '.join(posted_dates)}")

    def choose_master_directory(self):
        """
        Opens a directory dialog to choose the master directory and stores it in the self.master_directory variable.
        """
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        directory = QFileDialog.getExistingDirectory(self, "Choose master directory", "", options=options)

        if directory:
            self.master_directory = directory

    def post_media(self):
        """
        Triggers the posting process and adds the currently selected media to the PostedMediaList with the current date.
        """
        for site, media_files in self.selected_media.items():
            for media_file in media_files:
                self.posted_media_list.add_media(media_file)