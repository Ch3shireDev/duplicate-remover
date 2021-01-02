pyinstaller --noconfirm --onefile --console  "duplicate_remover.py"
move .\dist\*.exe .
rmdir .\dist
del /F/Q/S .\build
del /F/Q/S .\build 
del duplicate_remover.spec