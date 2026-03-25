@C:\ローカルツール\python\共通\共通設定.sql

set echo on

column spool_filename new_value spool_filename
select to_char(sysdate, 'yyyymmdd_hh24miss') || '_【実施結果】_&1' spool_filename from dual;
spool &spool_filename

SET SERVEROUTPUT ON

select sysdate from dual;

PROMPT 結果問題なければ、「COMMIT,SPOOL OFF,EXIT」を入力
