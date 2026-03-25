@C:\ローカルツール\python\データ更新___注意\sql\共通設定.sql
set echo on

SELECT inquiry_num||','||CR_NUM||','||OPPORTUNITY_NUM "問合せ番号,受注番号,案件番号" FROM TJFAX151_CUSTOMER_REQUEST WHERE CR_NUM='&1';

SELECT inquiry_num||','||CR_NUM||','||OPPORTUNITY_NUM "問合せ番号,受注番号,案件番号" FROM TJFAX151_CUSTOMER_REQUEST WHERE CR_NUM='&1';

prompt '>>'
--exit;
