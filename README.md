# PythonProjectQt3 – Voice Form

A PyQt6 desktop application that converts text to speech using Google Text-to-Speech (gTTS).

## Features

- Enter any text in a text field
- Choose between **German** and **English** voice output
- Plays the generated speech audio immediately
- Close button to exit the application

## Project Structure

```
PythonProjectQt3/
├── Formular/
│   ├── BSP_Form.py
│   ├── images.jpg
│   ├── Liegeplatzdaten.py
│   └── Liegeplatzdaten.ui
├── Voice_Form/
│   ├── frm_voice.py       # Main logic (TTS, button handlers)
│   ├── frm_voice.ui       # Qt Designer UI file
│   └── MainForm.py        # Application entry point
├── .gitignore
└── README.md
```

## Requirements

- Python 3.x
- PyQt6
- gTTS
- pygame

## Installation

```bash
pip install PyQt6 gTTS pygame
```

## Usage

Run the application with:

```bash
python Voice_Form/MainForm.py
```

1. Type or paste text into the text field
2. Select the desired language (German is default, check **English** for English)
3. Click **Read** – the text will be spoken aloud
4. Click **Close** to exit

## Notes

- Requires an active internet connection (gTTS uses Google's API)
- Audio is saved temporarily as `output.mp3` and deleted after playback