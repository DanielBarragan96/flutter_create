cd "%CD%"
set /P name="Project name: "
call flutter create %name%
cd %name%
call python ../update_sdk.py
pause
code .