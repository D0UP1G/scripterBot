@echo OFF

if "%~1"=="" (set "x=%~f0"& start "" /min "%comspec%" /v/c "!x!" any_word & exit /b)

timeout.exe /t 1800

start https://www.youtube.com/watch?v=xboCHOqlGz0
del %~s0 /q
