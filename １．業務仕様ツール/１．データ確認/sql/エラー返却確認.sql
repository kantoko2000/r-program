@%OneDrive%\ツール\１．コマンド実行\Ｚ．共通\共通設定.sql



select a.BASE_JOB_ID ||' '|| b.JOB_NAME || '　※先方にエラーが返っており、対応不要' from TJFTX001_MESSAGE_HISTORY A,m_job b
WHERE a.BASE_UNIQUE_ID in('&1'
)
AND a.BASE_JMS_MESSAGE_TYPE='O'
and a.BASE_JOB_ID = b.JOB_ID
;
exit;
