# OK Garmin 🎙️

**Completed:** August  3, 2025

A fun Python application inspired by the viral **"OK Garmin, save video"** meme.

Whenever I press my clipping shortcut, the program plays the meme audio. I created this as a humorous personal project to make gaming clips a little more entertaining.

## Features

- **Custom keyboard shortcut:** Press `Alt + ¸` to play the meme.
- **System tray integration:** Runs with an icon in the Windows notification area.
- **Shutdown sound:** Plays a separate audio clip when the shutdown shortcut is activated.
- **Background audio playback:** Uses threading to play audio without blocking the main application.
- **Repeated-trigger prevention:** Avoids continuously restarting the sound while the shortcut is held.
- **Exit option:** Close the program through the system tray or a keyboard shortcut.

## Requirements

- Python 3
- Windows
- `pygame`
- `pynput`
- `pystray`
- `Pillow`

Install the required libraries:

```bash
python -m pip install pygame pynput pystray pillow
```

## Installation

1. Download `ok_garmin.py`.
2. Install the required Python libraries.
3. Provide your own MP3 files and tray icon.
4. Update the audio and icon paths at the beginning of the Python script:

```python
mp3 = r"C:\path\to\ok_garmin.mp3"
shutdown_mp3 = r"C:\path\to\Shutdown-Sound.mp3"
icon_path = r"C:\path\to\garmin-logo.ico"
```

5. Run the program:

```bash
python ok_garmin.py
```

The original meme audio and artwork are not included in this repository.

## Controls

| Shortcut | Action |
|---|---|
| `Alt + ¸` | Play the OK Garmin meme |
| `Shift + Alt + T` | Play the shutdown sound and exit |
| System tray → Exit | Close the application |

The keyboard shortcut may need adjustment depending on your keyboard layout.

**Note:** The program does not actually save video clips. It only plays the corresponding sound.

## How It Works

The application uses several Python libraries:

- **pynput:** Monitors keyboard input and detects specific key combinations.
- **pygame:** Loads and plays MP3 audio files.
- **threading:** Allows the keyboard listener and sound playback to run without blocking the system tray interface.
- **pystray:** Creates the application icon and exit menu in the system tray.
- **Pillow:** Loads the tray icon image.

The program keeps track of pressed keys using a Python `set`. When the required combination is detected, it starts audio playback.

## Known Limitations

- Audio and icon file paths must be configured manually.
- Shortcut detection depends on the keyboard layout.
- Missing audio files may prevent playback, and a missing icon may prevent startup.
- Some keyboard-listener errors are silently ignored.

## Development Note

This project was created primarily with **AI assistance** as a fun personal experiment.

I came up with the original idea and reviewed the generated Python code to understand its functionality. Unlike my independently programmed projects, this application was not primarily written by hand.


**Author:** [Nik Berginc](https://github.com/nikberginc)
