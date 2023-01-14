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

        # create a directory to save the audio file if the directory does not exist
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        # extract the audio from the youtube video
        youtube = pytube.YouTube(youtube_video_url)
        video = youtube.streams.filter(only_audio=True).first()
        audio_file_name = video.default_filename
        video.download(output_path=directory_path)

        # convert the audio file to mp3
        mp3_file_path = os.path.join(directory_path, audio_file_name.split(".")[0] + ".mp3")
        try:
            print("Start converting audio file to mp3")
            audio_file = pydub.AudioSegment.from_file(audio_file_path)
            audio_file.export(mp3_file_path, format="mp3")
            print("Conversion to mp3 completed")
            self.title_label.config(text="The audio file has been saved successfully!")
        except Exception as e:
            print("Error converting audio file to mp3:", e)
            self.title_label.config(text="Error, the audio file has not been saved!")

    # function to browse the directory path to save the audio file
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

