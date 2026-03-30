REM ■共通設定ファイルを呼出
call """%OneDrive%\ツール\１．コマンド実行\Ｚ．共通\共通設定.bat"""

REM ■
cd /d %1

rem ■SQL実行
sqlplus %2/%3@%4 @%5 %6 %7 %8 %9 %10 %11 %12 %13 %14 %15

rem ■実施結果コピー処理
dir
RENAME *%6*.LST *%6*.txt
move *%6*.txt c:\tmp\

exit
