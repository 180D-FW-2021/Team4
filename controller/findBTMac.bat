@ECHO OFF
for /f "usebackq tokens=3 delims=," %%a in (`getmac /fo csv /v ^| find "Bluetooth"`) do set MAC=%%~a

ECHO %MAC% > %TEMP%\mymac.txt