@%OneDrive%\ツール\コマンド実行\Ｚ．共通\共通設定.sql


SELECT inquiry_num||','||CR_NUM||','||OPPORTUNITY_NUM "問合せ番号,受注番号,案件番号" FROM TJFAX151_CUSTOMER_REQUEST
WHERE CR_NUM='&1';


select DISTINCT
B.inquiry_num ||','||
     B.CR_NUM ||','||
A.SVC_ARR_MODIFY_CTGR ||','||
(SELECT EMP_EMAIL FROM  TJFXX049_EMP_BASIC_M  WHERE EMP_CD=A.LAST_UPDATED_BY_ID)  ||','||
B.SALES_TO_CANCEL_DATETIME   "問合せ番号,受注番号,役務依頼ステータス,画面更新者のメールアドレス,売上先取消日時"
from TJFAX373_SVC_ARR_SERVICE_HIST a,TJFAX151_CUSTOMER_REQUEST b,TJFAX371_SVC_ARR c
where a.SVC_ARR_MODIFY_CTGR ='15'
 and c.cr_num=b.cr_num
 and c.SVC_ARR_NUM=a.SVC_ARR_NUM
 and B.inquiry_num like 'JS%' AND B.DVLRY_MGMT_NUM='&1'  --サンプル　38513727
;


exit;
