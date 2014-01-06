@ECHO OFF

REM Environnement
CALL %~p0\Win32_Environment.bat

REM Compilation des ressources
pyrcc4 "sources/loteliQt.qrc" -o "sources/loteliQt_rc.py"

REM Compilation des .ui
python prebuild.py

PAUSE
