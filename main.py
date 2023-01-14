"""
Youtube audio extractor

This application is used to extract audio from youtube videos and save it as mp3 file.
Functions:
- it uses youtube-dl library to extract the audio from the video.
- it uses tkinter library to create a GUI for the application.
- it uses os library to create a directory to save the audio file.
- it uses sys library to exit the application.
- it uses time library to get the current time.
"""

import os
import sys
import time
import pytube
import tkinter as tk
from tkinter import filedialog
import pydub


# UI interface for the application using tkinter library
# Specifications:
# - it has a label to display the title of the application.
# - it has a label to display the message to enter the youtube video url.
# - it has a text box to enter the youtube video url.
# - it has a button to extract the audio from the youtube video.
# - it has a label to display the message to enter the directory path to save the audio file.
# - it has a text box to enter the directory path to save the audio file (optionally, user can enter the directory path by clicking the browse button).
# - it has a button to browse the directory path to save the audio file.
# - it has a button to exit the application.

# Behaviour:
# - when the user clicks the extract audio button, the audio is extracted from the youtube video and saved as mp3 file.
# - The extraction and conversion stages should be displayed in the console.
# - If the extraction and conversion are successful, the message "The audio file has been saved successfully!" is displayed in the title label.
# - If the extraction and conversion are not successful, the message "Error, the audio file has not been saved!" is displayed in the title label.
# - when the user clicks the exit button, the application is closed.

def browse(self):
    directory_path = filedialog.askdirectory()
    self.directory_path_text_box.insert(0, directory_path)


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # title label
        self.title_label = tk.Label(self, text="Youtube audio extractor")
        self.title_label.pack(side="top")

        # youtube video url label
        self.youtube_video_url_label = tk.Label(self, text="Enter the youtube video url:")
        self.youtube_video_url_label.pack(side="top")

        # youtube video url text box
        self.youtube_video_url_text_box = tk.Entry(self)
        self.youtube_video_url_text_box.pack(side="top")
        self.youtube_video_url_text_box.insert(0, "https://www.youtube.com/watch?v=v1vU5Gu4BFw")

        # extract audio button
        self.extract_audio_button = tk.Button(self, text="Extract audio", command=self.extract_audio)
        self.extract_audio_button.pack(side="top")

        # directory path label
        self.directory_path_label = tk.Label(self, text="Enter the directory path to save the audio file:")
        self.directory_path_label.pack(side="top")

        # directory path text box (filled with "c:\temp\" by default)
        self.directory_path_text_box = tk.Entry(self)
        self.directory_path_text_box.pack(side="top")
        self.directory_path_text_box.insert(0, "c:\\temp\\")

        # browse button
        # the browse button opens a file dialog to select the directory path to save the audio file
        self.browse_button = tk.Button(self, text="Browse", command=self.browse)
        self.browse_button.pack(side="top")

        # exit button
        self.exit_button = tk.Button(self, text="Exit", command=self.exit)
        self.exit_button.pack(side="top")

    # function to extract the audio from the youtube video using pytube library
    def extract_audio(self):
        """
        This function extracts the audio from the youtube video and saves it as mp3 file.
        Uses the pydub library to convert the video to mp3.
        """

        # get the youtube video url from the text box
        youtube_video_url = self.youtube_video_url_text_box.get()

        # get the directory path to save the audio file from the text box
        directory_path = self.directory_path_text_box.get()

        # create a directory to save the audio file
        # the directory name is the current time
        directory_name = time.strftime("%Y%m%d-%H%M%S")
        audio_directory = os.path.join(directory_path, directory_name)
        os.mkdir(audio_directory)

        # extract the audio from the youtube video and save it as mp3 file
        # the audio file name is the current time
        audio_file_name = time.strftime("%Y%m%d-%H%M%S")
        audio_file_path = os.path.join(audio_directory, audio_file_name + ".mp3")
        youtube = pytube.YouTube(youtube_video_url)
        video = youtube.streams.first()
        video.download(output_path=audio_directory, filename=audio_file_name + ".mp3")
        pydub.AudioSegment.from_file(audio_file_path).export(audio_file_path, format="mp3")

        # display the message that the audio file has been saved successfully
        self.title_label["text"] = "The audio file has been saved successfully!"

    def browse(self):
        directory_path = filedialog.askdirectory(parent=self.master, initialdir="/", title='Please select a directory')

        self.directory_path_text_box.delete(0, tk.END)
        self.directory_path_text_box.insert(0, directory_path)

    # function to exit the application
    def exit(self):
        sys.exit()

# main function
def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()

