set PELICAN_BINARY=D:\Projects\_pelican\Scripts\pelican.exe
set PYTHON_BINARY=D:\Projects\_pelican\Scripts\python.exe

%PELICAN_BINARY% content
cd output
%PYTHON_BINARY% -m pelican.server
cd ..
