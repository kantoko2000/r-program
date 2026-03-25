--役務手配作業履歴の外部連携データ送信済フラグを変更

set echo on
--■受注商品明細　確認
select inquiry_num,CR_LINE_ALL_CANCEL_FLG 受注明細全取消フラグ from TJFAX151_CUSTOMER_REQUEST
 where inquiry_num='【置換文字列1】';

--■役務手配作業履歴　更新
select SVC_ARR_NUM,SVC_ARR_HIST_NUM,INQUIRY_NUM from TJFAX371_SVC_ARR
 where inquiry_num='【置換文字列1】';

select SVC_ARR_HIST_NUM,SVC_ARR_SERV_HIST_NUM,EXTERNAL_COOP_DATA_SEND_FLG,l_flg
  from TJFAX373_SVC_ARR_SERVICE_HIST
 where
   SVC_ARR_NUM = '【置換文字列2】'
   and
   SVC_ARR_HIST_NUM = 【置換文字列3】
;

update TJFAX373_SVC_ARR_SERVICE_HIST
  set
   EXTERNAL_COOP_DATA_SEND_FLG = '1',
   LAST_UPDATE_DATETIME = sysdate,
   LAST_UPDATED_BY_ID = 'p000h12834'
  where
   SVC_ARR_NUM = '【置換文字列2】'
    and
   SVC_ARR_HIST_NUM = 【置換文字列3】
    and
   SVC_ARR_SERV_HIST_NUM = 【置換文字列4】
;

--確認
select SVC_ARR_HIST_NUM,SVC_ARR_SERV_HIST_NUM,EXTERNAL_COOP_DATA_SEND_FLG,l_flg
  from TJFAX373_SVC_ARR_SERVICE_HIST
 where
   SVC_ARR_NUM = '【置換文字列2】'
    and
   SVC_ARR_HIST_NUM = 【置換文字列3】
;
