@echo off

call %~dp0\Config.cmd
cd /d %sourcePath%

git log -n1