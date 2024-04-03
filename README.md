# Youtube Audio Extractor

This is a simple Python application that allows you to extract the audio from a Youtube video and save it as an mp3 file.

## Features

- Extract audio from Youtube videos using the `pytube` library
- Create a GUI for the application using `tkinter` library
- Use `os` library to create a directory to save the audio file
- Use `sys` library to exit the application
- Use `time` library to get the current time
- Use `pydub` library to convert the audio to mp3 format

## Requirements

- Python 3.6 or later
- `pytube3` library
- `pydub` library
- `ffmpeg`

## Usage

1. Clone the repository

```cmd
git clone https://github.com/<username>/youtube-audio-extractor.git
```

2. Install the required libraries
```cmd
pip install -r requirements.txt
```
(Alternatively, I use poetry to get dependencies from poetry.lock and creating a virtual environment)

3. Run the application
```cmd
python main.py
```


4. Enter the Youtube video url in the text box
5. Select the directory path to save the audio file (or use the default directory path)
6. Click the "Extract audio" button
7. The extraction and conversion process will be displayed in the console.
8. If the extraction and conversion are successful, the message "The audio file has been saved successfully!" will be displayed in the title label.
9. If the extraction and conversion are not successful, the message "Error, the audio file has not been saved!" will be displayed in the title label.
10. Click the "Exit" button to close the application

## Note

- The application requires internet connection to extract audio from Youtube video.
- The application uses ffmpeg for audio conversion, so you need to have ffmpeg installed on your machine.




