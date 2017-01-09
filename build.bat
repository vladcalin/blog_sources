set PYTHON_VENV_SCRIPTS=D:\Projects\Python_venvs\vladcalin.github.io\Scripts
set PELICAN_BINARY=%PYTHON_VENV_SCRIPTS%\pelican.exe
set PYTHON_BINARY=%PYTHON_VENV_SCRIPTS%\python.exe

%PELICAN_BINARY% content
cd output
%PYTHON_BINARY% -m pelican.server
cd ..
