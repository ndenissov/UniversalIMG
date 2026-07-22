import os
import site
import sys

# https://github.com/pyinstaller/pyinstaller/issues/8878
if getattr(sys, 'frozen', False):
    if site.USER_BASE is None:
        site.USER_BASE = ''
    if site.USER_SITE is None:
        site.USER_SITE = ''
    try:
        os.add_dll_directory(sys._MEIPASS)
    except AttributeError:
        pass
    os.environ['PATH'] = sys._MEIPASS + os.pathsep + os.environ.get('PATH', '')
    os.environ['KIVY_PACKAGING'] = '1'


def main():
    from pyimgedit.gui import run
    run()


if __name__ == '__main__':
    main()
