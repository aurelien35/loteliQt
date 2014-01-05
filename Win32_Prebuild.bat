@ECHO OFF

REM Environnement
CALL %~p0\Win32_Environment.bat

REM FOR /f "tokens=*" %%i in ('dir /b /s "*.ui"') do copy %%i /B+ ,,/Y %%i
pyrcc4 "sources/loteliQt.qrc" -o "sources/loteliQt_rc.py"
python "PortablePython\App\lib\site-packages\PyQt4\uic\pyuic.py" "sources/MainMenu/MainMenu.ui" -o "sources/MainMenu/MainMenu_ui.py" 
python "PortablePython\App\lib\site-packages\PyQt4\uic\pyuic.py" "sources/Client/ClientForm.ui" -o "sources/Client/ClientForm_ui.py" 
python "PortablePython\App\lib\site-packages\PyQt4\uic\pyuic.py" "sources/Tools/DatePicker.ui" -o "sources/Tools/DatePicker_ui.py" 

rem python prebuild.py

PAUSE
