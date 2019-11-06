@echo off

call %~dp0\Config.bat
cd /d %sourcePath%

git log -n1