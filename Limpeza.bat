@echo off
del /s /f /q %windir%\temp\*.*
rd /s /q %windir%\temp
md %windir%\temp
del /s /f /q %windir%\Prefetch
del /s /f /q %temp%\*.*
rd /s /q %temp%
del /s /f /q %windir%\tempor~1
del /s /f /q %windir%\temp
del /s /f /q %windir%\tmp
del /s /f /q %windir%\ff*.tmp
del /s /f /q %windir%\history
del /s /f /q %windir%\cookies
del /s /f /q %windir%\recent
del /s /f /q %windir%\spool\printers
del /s /f /q c:\WIN386.SWP

%SystemRoot%\System32\Cmd.exe /c Cleanmgr /sageset:65535 & Cleanmgr /sagerun:65535
type in: %windir%\SysWOW64\rundll32.exe advapi32.dll,ProcessIdleTasks

netsh int tcp set global congestionprovider=ctcp 
netsh int tcp set global dca=enabled
netsh int tcp set global ecncapability=enabled
netsh int tcp set global chimney=enabled

cls
@echo.
@echo Limpeza Completa!
pause
exit