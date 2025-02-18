# <img src="https://github.com/DevelopCMD/videoeditbot-portable/blob/main/banner-szK.png?raw=true" height="148"/>
A portable version of VideoEditBot.
---
![preview](https://github.com/DevelopCMD/videoeditbot-portable/blob/main/exemple.png?raw=true)
## What does this do?
Remember VideoEditBot? The discord editing bot that was popular a long time ago? With this program, you can experience the bot **locally** right on your computer! Just enter the arguments (e.g. "speed=2" "pch 15"), click Run Command, and there is your processed video! For more commands, please refer to COMMANDS.md

This program was tested on Windows 11 with Python 3.11. However, this program can work on as low as Windows 8.1.<br>
**NOTE:** You need to have the FFmpeg and SoX libraries installed on your system for this to work. You can get FFmpeg [here](https://www.gyan.dev/ffmpeg/builds/) and SoX [here.](https://sourceforge.net/projects/sox/files/sox/14.4.2/)<br>
<br>
For best performance, test on the latest Windows versions.<br>
<br>
Linux is currently not supported. This will be added in a future update.

## How to build
1. Install all the packages with `pip -r requirements.txt`
2. Build destroy.py into an exe with `pyinstaller --onefile destroy.py`
3. Build the gui.py with `pyinstaller --onefile gui.py`
4. Locate the freshly built `destroy.exe` and `gui.exe`
5. Place them in the root folder of the app.
6. Run gui.exe, and you're done!

## What was this made with?
The UI was made using the PyQt5 library, and the program was made using Python 3.11.
