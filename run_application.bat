echo off


rem Requirements
rem ------------
rem - install Python 3.x (add to system path)
rem - run the prepare_venv.bat script


rem activate the script's virtual environment so that we have access to the correct packages
call venv/Scripts/activate

python example.py

rem disable the script's virtual environment so that we are using the system settings again
call venv/Scripts/deactivate


rem uncomment to stop the commandline window from closing automatically
pause
