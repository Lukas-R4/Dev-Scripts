@echo off
:again

echo>code.txt
echo>code.txt list disk
echo>code.txt select disk 1
echo>>code.txt clean
echo>>code.txt create partition primary
echo>>code.txt format quick
echo>>code.txt active
echo>>code.txt assign
diskpart -s code.txt

cls

@echo ----------------------------------------------
@echo ----------------------------------------------
@echo ----------------Formatado!--------------------
@echo ----------------------------------------------
@echo ----------------------------------------------
@echo Feito por: NegaoSheipado.com
@echo.
@echo Insira outro cartao!
@echo.
pause
echo:
del /f code.txt
goto again
exit /b