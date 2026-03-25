SELECT /* parallel(4) */ distinct
  a.ADDRESS_CD 住所コード,
  decode(a.ADDRESS_INVALID_FLG,'0','','1','削除','') 削除,
  a.ZIP_CD 郵便番号,
  a.PREFECTURES_NAME 都道府県名,
  a.MUNI_NAME 市区郡町村名,
  a.OAZA_ALIAS_NAME 大字通称名,
  a.AZANA_NAME_CHO 字名丁目,
  b.AREA_CD エリア,
  c.AREA_NAME エリア名,
  c.NEARBY_SUPPLY_INV_GRP_CD 最寄サプライ在庫区,
  d.INV_GRP_NAME 最寄サプライ在庫区名,
  decode(b.MIXED_DELI_AREA_TARGET_FLG,'0','貸切','1','混載','') 配送手段,
  decode(b.DELI_METHOD_CTGR,'1','半日配送','2','一日配送','3','半日一日選択可能','') 配送方法,
  e.DIST_BASE_CD 作業店,
  f.DIST_BASE_NAME 作業店名,
  b.TERRITORY_CD テリトリー,
  decode(b.TERRITORY_CD,'1','千葉、神奈川、東京都町田市','2','滋賀、京都、兵庫','3','愛知、山口光市大字三輪','5','広島','6','茨城、栃木、埼玉','7','宮城','B','奈良、和歌山','C','富山、石川、福井、岐阜、静岡、三重','D','熊本、大分、宮崎、鹿児島、沖縄','E','鳥取、島根、岡山、山口','F','北海道','G','青森、岩手、秋田、山形、福島','J','群馬、新潟、山梨、長野','K','東京都','P','徳島、香川、愛媛、高知','R','大阪','T','福岡、佐賀、長崎','') "   ",
  decode(b.LMT_SHIP_H_DAY_DELI_ENB_FLG,'2','可能','1','','？') 限定出荷半日配送,
  g.INV_GRP_CD 日本紙通商在庫区,
  h.INV_GRP_NAME 日本紙通商在庫名,
  case 
    when a.ADDRESS_CD like '34202%' then 'on'
    when a.ADDRESS_CD like '11201%' then 'on'
    when a.ADDRESS_CD like '11202%' then 'on'
    when a.ADDRESS_CD like '11210%' then 'on'
    else ''
  end 配送暦flg
FROM
  TJFXX02D_ADDR_M a,
  TJFXX02K_ADDRESS_AREA_M b,
  TJFAX661_AREA_M c,
  TJFCX511_INV_GRP_M d,
  TJFAX643_DIST_BASE_JUDG_M e,
  TJFAX641_DIST_BASE_M f,
  TJFAX651_INV_GRP_JUDG_M g,
  TJFCX511_INV_GRP_M h
WHERE
  a.ADDRESS_CD = b.ADDRESS_CD AND 
  b.AREA_CD = c.AREA_CD AND 
  c.NEARBY_SUPPLY_INV_GRP_CD = d.INV_GRP_CD AND 
  e.AREA_CD = b.AREA_CD AND 
--  e.DELI_SERV_CTGR = '13' AND
  f.DIST_BASE_CD = e.DIST_BASE_CD AND
  g.AREA_CD = b.AREA_CD AND
  g.ALLOC_BASE_ITEM_GRP_CD = 'Q00001' AND
--  g.DELI_SERV_CTGR = '15' AND
  g.INV_GRP_CD = h.INV_GRP_CD 
--AND  a.ADDRESS_CD like '%'
--ORDER BY a.ADDRESS_CD
