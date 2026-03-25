--■提出用のＳＱＬ
SELECT DISTINCT
  a.AREA_CD エリアコード,
  b.AREA_NAME エリア名,
  a.ALLOC_BASE_ITEM_GRP_CD 引当拠点決定品群コード,
  c.ALLOC_BASE_ITEM_GRP_NAME 引当拠点決定品群名,
--  a.DELI_SERV_CTGR ,
  decode(a.DELI_SERV_CTGR,'11','サプライ','12','ルート','13','マシン','14','混載','15','ベンダー','16','納期短縮','17','振替配送','91','配送不要','不明') 配送サービス,
  a.INV_GRP_CD 在庫区コード,
  d.INV_GRP_NAME 在庫区名
--  a.COMPANY_CD 会社コード
--  a.M_INVALID_FLG 無効フラグ（＝１は無効）
--  a.CREATED_BY_ID ,
--  a.CREATE_DATETIME ,
--  a.LAST_UPDATED_BY_ID ,
--  a.LAST_UPDATE_DATETIME
FROM
  TJFAX651_INV_GRP_JUDG_M a,
  TJFAX661_AREA_M b,
  TJFAX533_ALLOC_BASE_ITEM_GRP_M c,
  TJFCX511_INV_GRP_M d
WHERE 1=1
--AND A.ALLOC_BASE_ITEM_GRP_CD='D00001'
AND  a.AREA_CD = b.AREA_CD AND 
  a.ALLOC_BASE_ITEM_GRP_CD = c.ALLOC_BASE_ITEM_GRP_CD AND 
  a.INV_GRP_CD = d.INV_GRP_CD
  and a.M_INVALID_FLG='0'
  AND a.DELI_SERV_CTGR<>'16'
  ORDER BY 1,3,5,6 ASC
