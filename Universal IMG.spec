# -*- mode: python ; coding: utf-8 -*-
from kivy_deps import sdl2, glew, angle

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('pyimgedit/icon.png', 'pyimgedit')],
    hiddenimports=[
        'kivymd.icon_definitions',
        'kivymd.icon_definitions.md_icons',
        'kivy_deps.sdl2',
        'kivy_deps.glew',
        'kivy_deps.angle',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=2,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins + angle.dep_bins)],
    [('O', None, 'OPTION'), ('O', None, 'OPTION')],
    name='Universal IMG',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['pyimgedit/icon.png'],
)