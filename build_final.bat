%echo off

set PYTHON_VENV_SCRIPTS=D:\Projects\_pelican\Scripts
set PELICAN_BINARY=%PYTHON_VENV_SCRIPTS%\pelican.exe
set PYTHON_BINARY=%PYTHON_VENV_SCRIPTS%\python.exe

%PELICAN_BINARY% content -s publishconf.py
cd output
%PYTHON_BINARY% -m pelican.server
cd ..
