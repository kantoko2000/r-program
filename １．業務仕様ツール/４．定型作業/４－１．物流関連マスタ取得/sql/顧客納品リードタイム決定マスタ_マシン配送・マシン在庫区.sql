SELECT
  c.INV_GRP_CD 在庫区コード,
  c.INV_GRP_NAME 在庫区名,
  d.DIST_BASE_CD 物流拠点コード,
  d.DIST_BASE_NAME 物流拠点名,
  decode(a.DELI_SERV_CTGR,'11','サプライ','12','ルート','13','マシン','14','混載','15','ベンダー','16','納期短縮','17','振替配送','91','配送不要','不明') 配送サービス,
  a.SHIPPING_ADDRESS_CD 住所コード,
  a.CUST_DVLRY_LT リードタイム,
  b.ZIP_CD 郵便番号,
  b.PREFECTURES_NAME 都道府県名,
  b.MUNI_NAME 市区郡町村名,
  b.OAZA_ALIAS_NAME 大字通称名,
  b.AZANA_NAME_CHO 字名丁目
FROM
  TJFAX662_CUST_DELIV_LT_M a,
  TJFXX02D_ADDR_M b,
  TJFCX511_INV_GRP_M c,
  TJFAX641_DIST_BASE_M d
WHERE
  a.SHIPPING_ADDRESS_CD = b.ADDRESS_CD AND 
  c.DIST_BASE_CD = a.CARRY_OUT_DIST_BASE_CD AND 
  c.DIST_BASE_CD = d.DIST_BASE_CD AND 
  c.INV_GRP_CD in (
'534',
'583',
'509',
'RF0',
'539',
'507',
'561',
'589',
'E31',
'518',
'5P1',
'584',
'577',
'U10',
'525',
'128',
'511',
'521',
'585',
'512',
'586',
'129'
) AND
  a.DELI_SERV_CTGR = '13' AND 
  a.M_INVALID_FLG = '0'
ORDER BY 在庫区コード,住所コード
