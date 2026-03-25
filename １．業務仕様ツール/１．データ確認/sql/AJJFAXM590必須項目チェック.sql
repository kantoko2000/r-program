set echo on
SET head OFF
set pages 10000
SET SERVEROUTPUT OFF
SET LINESIZE  2000 COLSEP,

SET head OFF
SET VERIFY OFF
set feed off
SET ECHO OFF

select DISTINCT
case when instr(REPLACE(convert(UTL_RAW.CAST_TO_VARCHAR2(DBMS_LOB.SUBSTR( d.base_message_raw_data ,2000,139)),'JA16SJIS','UTF8'), '><', '>'||CHR(13)||'<'),(SELECT EMP_EMAIL FROM  TJFXX049_EMP_BASIC_M  WHERE EMP_CD=A.LAST_UPDATED_BY_ID)) > 0 then '更新者ｱﾄﾞﾚｽCC含む→〇'
     else '更新者ｱﾄﾞﾚｽCC含む→×'
     end ||','||
case when instr(REPLACE(convert(UTL_RAW.CAST_TO_VARCHAR2(DBMS_LOB.SUBSTR( d.base_message_raw_data ,2000,139)),'JA16SJIS','UTF8'), '><', '>'||CHR(13)||'<'),'JFAAM530.xml') > 0 then 'JFAAM530受託NG→○'
     else 'JFAAM530受託NG→×'
     end ||','||
case when instr(REPLACE(convert(UTL_RAW.CAST_TO_VARCHAR2(DBMS_LOB.SUBSTR( d.base_message_raw_data ,2000,139)),'JA16SJIS','UTF8'), '><', '>'||CHR(13)||'<'),'ccAddress') > 0 then 'ccAddress含む→○'
     else 'ccAddress含む→×'
     end ||','|| 
B.inquiry_num ||','|| 
to_char(B.SALES_TO_CANCEL_DATETIME,'YYYYMMDD') ||','||
d.BASE_UNIQUE_ID
--(SELECT EMP_EMAIL FROM  TJFXX049_EMP_BASIC_M  WHERE EMP_CD=A.LAST_UPDATED_BY_ID) ||','||
--case when SVC_ARR_MODIFY_CTGR ='11' then '依頼元キャンセル'
--     when SVC_ARR_MODIFY_CTGR ='12' then '依頼取消'
--     when SVC_ARR_MODIFY_CTGR ='13' then '不受理'
--     when SVC_ARR_MODIFY_CTGR ='14' then '受託後不受理'
--     when SVC_ARR_MODIFY_CTGR ='15' then '受託NG'
--     when SVC_ARR_MODIFY_CTGR ='16' then '受託NG取消'
--     when SVC_ARR_MODIFY_CTGR ='17' then '受託OK取消'
--     when SVC_ARR_MODIFY_CTGR ='18' then '作業完了取消'
--     when SVC_ARR_MODIFY_CTGR ='21' then '依頼先指定'
--     when SVC_ARR_MODIFY_CTGR ='22' then '手配依頼'
--     when SVC_ARR_MODIFY_CTGR ='23' then '受託OK'
--     when SVC_ARR_MODIFY_CTGR ='24' then '作業完了'
--     when SVC_ARR_MODIFY_CTGR ='25' then '振替金額確定済'
--     when SVC_ARR_MODIFY_CTGR ='26' then '振替金額計上不要'
--     when SVC_ARR_MODIFY_CTGR ='31' then '依頼先変更'
--     when SVC_ARR_MODIFY_CTGR ='32' then '料金変更'
--     when SVC_ARR_MODIFY_CTGR ='33' then '納期更新'
--     when SVC_ARR_MODIFY_CTGR ='34' then '作業内容変更'
--     when SVC_ARR_MODIFY_CTGR ='35' then '機番情報更新（RLC）'
--     when SVC_ARR_MODIFY_CTGR ='36' then '納期時刻情報更新（RLC）'
--     when SVC_ARR_MODIFY_CTGR ='19' then 'キャンセル保留'
--     when SVC_ARR_MODIFY_CTGR ='37' then '作業完了保留'
--     else 'そのほか'
--     end
--     B.CR_NUM ||','||
--A.SVC_ARR_MODIFY_CTGR ||','||
--   "問合せ番号,受注番号,役務依頼ステータス,画面更新者のメールアドレス,売上先取消日時"
--, CHR(10) || REPLACE(convert(UTL_RAW.CAST_TO_VARCHAR2(DBMS_LOB.SUBSTR( d.base_message_raw_data ,2000,139)),'JA16SJIS','UTF8'), '><', '>'||CHR(13)||'<')
from TJFAX373_SVC_ARR_SERVICE_HIST a,TJFAX151_CUSTOMER_REQUEST b,TJFAX371_SVC_ARR c,TJFTX001_MESSAGE_HISTORY d
where 1=1
-- and a.SVC_ARR_MODIFY_CTGR ='15'
 and c.cr_num=b.cr_num
 and c.SVC_ARR_NUM=a.SVC_ARR_NUM
 and B.inquiry_num like 'JS%'
 AND B.DVLRY_MGMT_NUM =substrb( UTL_I18N.RAW_TO_CHAR(DBMS_LOB.SUBSTR(d.BASE_MESSAGE_RAW_DATA,2000,1),'AL32UTF8'), INSTRB(UTL_I18N.RAW_TO_CHAR(DBMS_LOB.SUBSTR(d.BASE_MESSAGE_RAW_DATA,2000,1),'AL32UTF8'),'>DELIVERY_MGMT_NUM')+57,8 )
 and d.BASE_UNIQUE_ID in (
 select 
   T_QUEUE_STATUS.JOB_SUBMIT_NAME           
from T_QUEUE_STATUS INNER JOIN M_JOB ON T_QUEUE_STATUS.JOB_ID = M_JOB.JOB_ID
LEFT JOIN T_JOB_RESULT ON T_QUEUE_STATUS.JOB_SUBMIT_ID = T_JOB_RESULT.JOB_SUBMIT_ID
where 1=1 
and  JOB_INIT_SUBMIT_TIME between TRUNC(SYSDATE) and SYSDATE
AND JOB_EXECUTION_STATUS = 'Execution Failed'
AND T_QUEUE_STATUS.JOB_ID  in ('AJJFAXM590')
)
;
 exit;




exit;
