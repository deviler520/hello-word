@echo off

call %~dp0\Config.bat
cd /d %sourcePath%

git reset –-hard origin/master 
git.exe pull --progress -v --no-rebase "origin"