import PyInstaller.__main__

PyInstaller.__main__.run([
    'code.py',
    '--onefile',
    '-c'
])