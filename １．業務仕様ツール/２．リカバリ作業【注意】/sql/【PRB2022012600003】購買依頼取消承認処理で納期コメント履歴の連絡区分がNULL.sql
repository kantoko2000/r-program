@%OneDrive%\ツール\１．コマンド実行\Ｚ．共通\共通設定.sql

column spool_filename new_value spool_filename
select to_char(sysdate, 'yyyymmdd_hh24miss') || '_【実施結果】_&1' spool_filename from dual;
spool &spool_filename





set echo on
select '"' ||
DS_REPLIED_DATETIME           || '","' ||
CR_NUM                        || '","' ||
CR_L_NUM                      || '","' ||
DS_CMMNT_HIST_NUM             || '","' ||
DEST_SYS_CD                   || '","' ||
FIXED_DS_CTGR                 || '","' ||
CUST_CONTACT_METHOD_CTGR      || '","' ||
EXT_SYS_CONTACT_METHOD_CTGR   || '","' ||
CONTACT_CTGR                  || '","' ||
DERIVED_ITEM_CONTACT_NEED_FLG || '"' data
from TJFAX201_DS_CMMNT_HIST
where CR_NUM='&2';

update TJFAX201_DS_CMMNT_HIST
 set              DEST_SYS_CD='12', 
                FIXED_DS_CTGR='11', 
     CUST_CONTACT_METHOD_CTGR='91', 
  EXT_SYS_CONTACT_METHOD_CTGR='91', 
                 CONTACT_CTGR='13', 
DERIVED_ITEM_CONTACT_NEED_FLG='1',  
          DS_REPLIED_DATETIME=(SELECT MAX(DS_REPLIED_DATETIME) FROM TJFAX201_DS_CMMNT_HIST WHERE CR_NUM='&2')
where CR_NUM='&2' and DEST_SYS_CD is null;

select '"' ||
DS_REPLIED_DATETIME           || '","' ||
CR_NUM                        || '","' ||
CR_L_NUM                      || '","' ||
DS_CMMNT_HIST_NUM             || '","' ||
DEST_SYS_CD                   || '","' ||
FIXED_DS_CTGR                 || '","' ||
CUST_CONTACT_METHOD_CTGR      || '","' ||
EXT_SYS_CONTACT_METHOD_CTGR   || '","' ||
CONTACT_CTGR                  || '","' ||
DERIVED_ITEM_CONTACT_NEED_FLG || '"' data
from TJFAX201_DS_CMMNT_HIST
where CR_NUM='&2';


PROMPT "内容が問題なければ、コミットとSPOOL OFFを入力します"
PROMPT "内容が問題あれば、ロールバックとSPOOL OFFを入力します"

--exit;
