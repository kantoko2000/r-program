@%OneDrive%\ツール\１．コマンド実行\Ｚ．共通\共通設定.sql

column spool_filename new_value spool_filename
select to_char(sysdate, 'yyyymmdd_hh24miss') || '_【実施結果】_&1' spool_filename from dual;
spool &spool_filename

select distinct a.data_invalid_flg データ無効フラグ,b.inquiry_num 問合せ番号 ,a.CUST_ACCPT_REQ_NUM 検収依頼番号 ,a.ACCEPTANCE_CERTIFICATION_NUM 検収書番号 
 from TJFAX231_CUST_ACCPT_REQ a  --検収依頼
,TJFAX232_ACCPT_REQ_ITEM_LINE b --検収依頼商品明細
where a.CUST_ACCPT_REQ_NUM = b.CUST_ACCPT_REQ_NUM and b.inquiry_num='&2' and b.DATA_INVALID_FLG = '0' ;

update TJFAX231_CUST_ACCPT_REQ set DATA_INVALID_FLG = '1', LAST_UPDATED_BY_ID = 'p000h12834', LAST_UPDATE_DATETIME = sysdate where CUST_ACCPT_REQ_NUM in (
select  a.CUST_ACCPT_REQ_NUM
from TJFAX231_CUST_ACCPT_REQ a  --検収依頼
,TJFAX232_ACCPT_REQ_ITEM_LINE b --検収依頼商品明細
where a.CUST_ACCPT_REQ_NUM = b.CUST_ACCPT_REQ_NUM and b.inquiry_num='&2' and b.DATA_INVALID_FLG = '0' ) and DATA_INVALID_FLG = '0' ;

select distinct a.data_invalid_flg データ無効フラグ,b.inquiry_num 問合せ番号 ,a.CUST_ACCPT_REQ_NUM 検収依頼番号 ,a.ACCEPTANCE_CERTIFICATION_NUM 検収書番号 
 from TJFAX231_CUST_ACCPT_REQ a  --検収依頼
,TJFAX232_ACCPT_REQ_ITEM_LINE b --検収依頼商品明細
where a.CUST_ACCPT_REQ_NUM = b.CUST_ACCPT_REQ_NUM and b.inquiry_num='&2' and b.DATA_INVALID_FLG = '0' ;




PROMPT "内容が問題なければ、コミットとSPOOL OFFを入力します"
PROMPT "内容が問題あれば、ロールバックとSPOOL OFFを入力します"

--exit;
