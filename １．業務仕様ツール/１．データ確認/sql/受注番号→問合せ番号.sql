@%OneDrive%\ツール\コマンド実行\Ｚ．共通\共通設定.sql


SELECT inquiry_num||','||CR_NUM||','||OPPORTUNITY_NUM "問合せ番号,受注番号,案件番号" FROM TJFAX151_CUSTOMER_REQUEST
WHERE CR_NUM='&1';

exit;
