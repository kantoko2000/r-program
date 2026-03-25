@%OneDrive%\ツール\１．コマンド実行\Ｚ．共通\共通設定.sql

column spool_filename new_value spool_filename
select to_char(sysdate, 'yyyymmdd_hh24miss') || '_【実施結果】_&1' spool_filename from dual;
spool &spool_filename

SELECT /*+ index(AX15A XJFAX15A15) */ AX15A.CR_NUM || ',' ||
       AX15A.CR_L_NUM || ',' ||
       AX15A.CR_LINE_HIST_NUM || ',' ||
       AX15A.DEADLINE || ',' ||
       AX15A.INQUIRY_NUM || ',' ||
       AX15A.INQUIRY_L_NUM || ',' ||
       AX15A.CR_ITEM_CD || ',' ||
       AX15A.CR_ITEM_NAME || ',' ||
       AX15A.SHIPPING_SPC_DATE || ',' ||
       AX15A.FIXED_AFTER_DS_DATE || ',' ||
       AX15A.FIRST_DLVRY_TO_REPLIED_DS_DATE || ',' ||
       AX331.PR_ARRANGE_PLAN_DATETIME
  FROM TJFAX15A_CR_ITEM AX15A,
       TJFAX331_PR_ARRANGE AX331
 WHERE AX15A.CR_NUM               = AX331.CR_NUM
   AND AX15A.CR_L_NUM             = AX331.CR_L_NUM
   AND AX15A.CR_LINE_HIST_NUM     = AX331.CR_LINE_HIST_NUM
--   AND AX15A.INQUIRY_NUM          LIKE 'JS3%'
   AND AX15A.ALLOC_INV_GRP_CD     = 'S01'
   AND AX15A.SHIPPING_SPC_DATE    >= TO_CHAR(sysdate-1,'YYYYMMDD')
   AND AX15A.SHIPPING_SPC_DATE <> TO_CHAR(PR_ARRANGE_PLAN_DATETIME,'YYYYMMDD')
   AND AX15A.L_FLG                = '1'
   AND AX15A.CANCEL_FLG           = '0'
   AND AX331.L_FLG                = '1'
   AND AX331.CANCEL_FLG           = '0'
   AND AX331.PR_ARRANGE_STATUS    = '10'
;

DECLARE
  WK_CR_NUM VARCHAR2(1000);
  WK_CR_L_NUM VARCHAR2(1000);
  WK_CR_LINE_HIST_NUM VARCHAR2(1000);
  WK_DEADLINE VARCHAR2(1000);

  update_query  VARCHAR2(1000);

  select_query  VARCHAR2(1000);
  CURSOR c1 IS
SELECT /*+ index(AX15A XJFAX15A15) */ AX15A.CR_NUM,
       AX15A.CR_L_NUM,
       AX15A.CR_LINE_HIST_NUM,
       AX15A.DEADLINE
  FROM TJFAX15A_CR_ITEM AX15A,
       TJFAX331_PR_ARRANGE AX331
 WHERE AX15A.CR_NUM               = AX331.CR_NUM
   AND AX15A.CR_L_NUM             = AX331.CR_L_NUM
   AND AX15A.CR_LINE_HIST_NUM     = AX331.CR_LINE_HIST_NUM
--   AND AX15A.INQUIRY_NUM          LIKE 'JS3%'
   AND AX15A.ALLOC_INV_GRP_CD     = 'S01'
   AND AX15A.SHIPPING_SPC_DATE    >= TO_CHAR(sysdate-1,'YYYYMMDD')
   AND AX15A.SHIPPING_SPC_DATE <> TO_CHAR(PR_ARRANGE_PLAN_DATETIME,'YYYYMMDD')
   AND AX15A.L_FLG                = '1'
   AND AX15A.CANCEL_FLG           = '0'
   AND AX331.L_FLG                = '1'
   AND AX331.CANCEL_FLG           = '0'
   AND AX331.PR_ARRANGE_STATUS    = '10';
BEGIN
  OPEN c1;
  LOOP
    FETCH c1 INTO WK_CR_NUM,WK_CR_L_NUM,WK_CR_LINE_HIST_NUM,WK_DEADLINE;
    EXIT WHEN c1%NOTFOUND;
    update_query := 'UPDATE TJFAX331_PR_ARRANGE SET PR_ARRANGE_PLAN_DATETIME='''|| WK_DEADLINE ||''',last_updated_by_id = ''p000h12834'',last_update_datetime = sysdate WHERE CR_NUM ='''|| WK_CR_NUM ||''' AND CR_L_NUM ='''|| WK_CR_L_NUM ||''' AND CR_LINE_HIST_NUM ='''|| WK_CR_LINE_HIST_NUM ||'''';
    DBMS_OUTPUT.PUT_LINE('update_query: ' || update_query);
    EXECUTE IMMEDIATE update_query;
--    commit;
  END LOOP;
--  ROLLBACK;
  CLOSE c1;
END;
/


SELECT /*+ index(AX15A XJFAX15A15) */ AX15A.CR_NUM || ',' ||
       AX15A.CR_L_NUM || ',' ||
       AX15A.CR_LINE_HIST_NUM || ',' ||
       AX15A.DEADLINE || ',' ||
       AX15A.INQUIRY_NUM || ',' ||
       AX15A.INQUIRY_L_NUM || ',' ||
       AX15A.CR_ITEM_CD || ',' ||
       AX15A.CR_ITEM_NAME || ',' ||
       AX15A.SHIPPING_SPC_DATE || ',' ||
       AX15A.FIXED_AFTER_DS_DATE || ',' ||
       AX15A.FIRST_DLVRY_TO_REPLIED_DS_DATE || ',' ||
       AX331.PR_ARRANGE_PLAN_DATETIME
  FROM TJFAX15A_CR_ITEM AX15A,
       TJFAX331_PR_ARRANGE AX331
 WHERE AX15A.CR_NUM               = AX331.CR_NUM
   AND AX15A.CR_L_NUM             = AX331.CR_L_NUM
   AND AX15A.CR_LINE_HIST_NUM     = AX331.CR_LINE_HIST_NUM
--   AND AX15A.INQUIRY_NUM          LIKE 'JS3%'
   AND AX15A.ALLOC_INV_GRP_CD     = 'S01'
   AND AX15A.SHIPPING_SPC_DATE    >= TO_CHAR(sysdate-1,'YYYYMMDD')
   AND AX15A.SHIPPING_SPC_DATE <> TO_CHAR(PR_ARRANGE_PLAN_DATETIME,'YYYYMMDD')
   AND AX15A.L_FLG                = '1'
   AND AX15A.CANCEL_FLG           = '0'
   AND AX331.L_FLG                = '1'
   AND AX331.CANCEL_FLG           = '0'
   AND AX331.PR_ARRANGE_STATUS    = '10'
;

PROMPT 結果問題なければ、「COMMIT,SPOOL OFF,EXIT」を入力

--SPOOL OFF;

--exit;
