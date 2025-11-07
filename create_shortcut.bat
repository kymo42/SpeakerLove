@echo off
REM Create desktop shortcut for Voice Isolator

setlocal enabledelayexpansion

REM Get the current directory
set "current_dir=%~dp0"
set "shortcut_path=%USERPROFILE%\Desktop\Voice Isolator.lnk"

REM Create VBS script to make shortcut
set "vbs_file=%TEMP%\create_shortcut.vbs"

(
echo Set oWS = WScript.CreateObject("WScript.Shell"^)
echo sLinkFile = "%shortcut_path%"
echo Set oLink = oWS.CreateShortcut(sLinkFile^)
echo oLink.TargetPath = "%current_dir%run.bat"
echo oLink.WorkingDirectory = "%current_dir%"
echo oLink.Description = "Voice Isolator - Remove speaker output from microphone"
echo oLink.Save
) > "%vbs_file%"

REM Run the VBS script
cscript "%vbs_file%"

REM Clean up
del "%vbs_file%"

echo.
echo Desktop shortcut created successfully!
echo Location: %shortcut_path%
echo.
pause
