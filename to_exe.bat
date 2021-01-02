pyinstaller --noconfirm --onefile --console  "duplicate_removal.py"
move .\dist\duplicate_removal.exe .
rmdir .\dist
del /F/Q/S .\build
del /F/Q/S .\build 