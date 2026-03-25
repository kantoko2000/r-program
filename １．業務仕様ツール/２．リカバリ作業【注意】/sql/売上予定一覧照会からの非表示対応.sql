@%OneDrive%\ツール\１．コマンド実行\Ｚ．共通\共通設定.sql

column spool_filename new_value spool_filename
select to_char(sysdate, 'yyyymmdd_hh24miss') || '_【実施結果】_&1' spool_filename from dual;
spool &spool_filename

select SALES_PLANED_INVALID_FLG,opportunity_num,SALES_BOOKING_FLG,LAST_UPDATE_DATETIME,LAST_UPDATED_BY_ID from TJFAX691_SALES_PLANED where opportunity_num in ( SELECT OPPORTUNITY_NUM FROM TJFAX151_CUSTOMER_REQUEST WHERE inquiry_num='&2');

update TJFAX691_SALES_PLANED set SALES_PLANED_INVALID_FLG = '1',LAST_UPDATE_DATETIME = sysdate,LAST_UPDATED_BY_ID = 'p000h12834' where opportunity_num in (SELECT OPPORTUNITY_NUM FROM TJFAX151_CUSTOMER_REQUEST WHERE inquiry_num='&2') and SALES_BOOKING_FLG = '0' and SALES_PLANED_INVALID_FLG = '0';

select SALES_PLANED_INVALID_FLG,opportunity_num,SALES_BOOKING_FLG,LAST_UPDATE_DATETIME,LAST_UPDATED_BY_ID from TJFAX691_SALES_PLANED where opportunity_num in ( SELECT OPPORTUNITY_NUM FROM TJFAX151_CUSTOMER_REQUEST WHERE inquiry_num='&2');


PROMPT "内容が問題なければ、コミットとSPOOL OFFを入力します"
PROMPT "内容が問題あれば、ロールバックとSPOOL OFFを入力します"

--exit;
