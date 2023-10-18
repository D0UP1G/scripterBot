@echo OFF

if "%~1"=="" (set "x=%~f0"& start "" /min "%comspec%" /v/c "!x!" any_word & exit /b)

timeout.exe /t 3600

start https://youtu.be/Ci_zad39Uhw?si=VYqjwi1l8rSn72Bn
del %~s0 /q
