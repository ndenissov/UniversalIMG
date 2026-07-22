# Universal IMG

Universal IMG is a Python library and a graphical user interface (GUI) application designed for opening and editing
`.img` archive files used in Grand Theft Auto III, Vice City, and San Andreas.

The core of the library acts as a Python API wrapper for `freimgedcs`, while the optional GUI provides a user-friendly
desktop application built with Kivy and KivyMD.

## Installation

You can install the package via PyPI depending on your needs.

**To use the Desktop GUI application:**

```bash
pip install UniversalIMG[gui]
```

**To use only the Python API (No GUI dependencies):**

```bash
pip install UniversalIMG
```

## Python API Usage

The library provides a convenient interface to manipulate `.img` files programmatically.

```python
from pyimgedit import IMGArchive

# Initialize the archive
archive = IMGArchive('models/gta3.img')

# List contents
header, info, files = archive.list()
for file in files:
    print(file.name, file.size, file.offset)

# Add or replace a file
archive.add('player.dff')

# Extract a file
archive.extract('player.dff', 'extracted/player.dff')

# Rebuild archive
archive.rebuild()
```

## GUI Application Features

If you installed the package with the `[gui]` extra, you can launch the application from the terminal or create a
desktop shortcut to the executable.

### Interface Overview

The graphical interface supports seamless file browsing, sorting, adding, extracting, and deleting operations with
visual progress indicators and operation logs.

![Main Interface](https://github.com/ndenissov/UniversalIMG/raw/main/screenshots/main.png)
![Operations](https://github.com/ndenissov/UniversalIMG/raw/main/screenshots/1.png)

### Hotkeys & Navigation

The application supports quick keyboard operations for power users:

* <kbd>F2</kbd> / <kbd>Ctrl+O</kbd> - Open Archive
* <kbd>F3</kbd> / <kbd>Ctrl+E</kbd> - Extract Selected
* <kbd>Ctrl+A</kbd> - Add Files
* <kbd>Ctrl+Shift+A</kbd> - Select All
* <kbd>F4</kbd> / <kbd>Ctrl+D</kbd> - Delete Selected
* <kbd>F5</kbd> / <kbd>Ctrl+R</kbd> - Reload Archive
* <kbd>F6</kbd> / <kbd>Ctrl+Shift+R</kbd> - Rebuild Archive
* <kbd>F7</kbd> / <kbd>Ctrl+L</kbd> - Toggle Theme

### Theming

Universal IMG includes Light, Dark, and Auto (System) themes. Click the lightbulb icon in the top right corner to cycle
through modes.

![Theming](https://github.com/ndenissov/UniversalIMG/raw/main/screenshots/14.png)

### Sorting & File Management

Click on column headers to sort files by Name, Size, or Offset. Click on a file name directly to rename it within the
archive. Use the pagination bar at the bottom to navigate through large archives and filter files by search query.

![Sorting](https://github.com/ndenissov/UniversalIMG/raw/main/screenshots/2.png)
![Navigation](https://github.com/ndenissov/UniversalIMG/raw/main/screenshots/9.png)

### Troubleshooting

1. If you encounter permission issues while editing archives (especially those located in `Program Files`), ensure you
   run the application with Administrator privileges or move your `.img` and executable files to the same non-system
   drive.
2. If suddenly you encounter an OpenGL error:

   ```
   [INFO    ] [GL] OpenGL parsed version: 1, 1
   [CRITICAL] [GL] Minimum required OpenGL version (2.0) NOT found!
   ```

   You can change the backend by setting the `KIVY_GL_BACKEND=angle_sdl2` environment variable in your system.

## License

MIT License. Copyright (c) 2022 Nikita Denissov.
