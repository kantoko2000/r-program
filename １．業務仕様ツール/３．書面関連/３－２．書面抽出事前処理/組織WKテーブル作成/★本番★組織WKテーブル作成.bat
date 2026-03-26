CALL C:\定型作業\共通\共通設定.bat
CD C:\定型作業\書面審査\書面集計\書面関連\事前処理\組織WKテーブル作成
cd .
SET NLS_LANG=JAPANESE_JAPAN.JA16SJIS

ECHO "書面審査：事前組織ＷＫテーブル作成"
sqlplus %SYOMEN_AX_USER%/%SYOMEN_AX_USER_PASS%@RISM_JFAG1 @組織WKテーブル作成.sql
exit
