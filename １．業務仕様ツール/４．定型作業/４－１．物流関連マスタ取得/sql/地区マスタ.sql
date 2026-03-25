select 
      WK_TBL.住所コード
     ,WK_TBL.削除
     ,WK_TBL.郵便番号
     ,WK_TBL.都道府県名
     ,WK_TBL.市区郡町村名
     ,WK_TBL.大字通称名
     ,WK_TBL.字名丁目
     ,WK_TBL.エリア
     ,WK_TBL.エリア名
     ,WK_TBL.最寄サプライ在庫区
     ,WK_TBL.最寄サプライ在庫区名
     ,WK_TBL.配送手段
     ,WK_TBL.配送方法
--     ,WK_TBL.配送サービス区分
--
     ,MAX(WK_TBL.作業店コード_マシン配送) 作業店コード_マシン配送
     ,MAX(WK_TBL.作業店名_マシン配送)    作業店名_マシン配送
     ,MAX(WK_TBL.作業店コード_ルート配送) 作業店コード_ルート配送
     ,MAX(WK_TBL.作業店名_ルート配送)    作業店名_ルート配送
--
     ,WK_TBL.テリトリー
     ,WK_TBL.テリトリー名
     ,WK_TBL.限定出荷半日配送
     ,WK_TBL.日本紙通商在庫区
     ,WK_TBL.日本紙通商在庫名
     ,WK_TBL.配送暦flg
from 
 (SELECT distinct
   a.ADDRESS_CD               住所コード
  ,CASE a.ADDRESS_INVALID_FLG
    WHEN '0' THEN ''
    WHEN '1' THEN '削除'
    ELSE ''
   END                        削除
  ,a.ZIP_CD                   郵便番号
  ,a.PREFECTURES_NAME         都道府県名
  ,a.MUNI_NAME                市区郡町村名
  ,a.OAZA_ALIAS_NAME          大字通称名
  ,a.AZANA_NAME_CHO           字名丁目
  ,b.AREA_CD                  エリア
  ,c.AREA_NAME                エリア名
  ,c.NEARBY_SUPPLY_INV_GRP_CD 最寄サプライ在庫区
  ,d.INV_GRP_NAME             最寄サプライ在庫区名
  ,CASE b.MIXED_DELI_AREA_TARGET_FLG
    WHEN '0' THEN '貸切'
    WHEN '1' THEN '混載'
    ELSE ''
   END AS                     配送手段
  ,CASE b.DELI_METHOD_CTGR
    WHEN '1' THEN '半日配送'
    WHEN '2' THEN '一日配送'
    WHEN '3' THEN '半日一日選択可能'
    ELSE ''
   END AS                     配送方法
  ,e.DELI_SERV_CTGR           配送サービス区分
  ,case when e.DELI_SERV_CTGR='13' then e.DIST_BASE_CD
        else null
   end                        作業店コード_マシン配送
  ,case when e.DELI_SERV_CTGR='13' then f.DIST_BASE_NAME
        else null
   end                        作業店名_マシン配送
  ,case when e.DELI_SERV_CTGR='12' then e.DIST_BASE_CD
        else null
   end                        作業店コード_ルート配送
  ,case when e.DELI_SERV_CTGR='12' then f.DIST_BASE_NAME
        else null
   end                        作業店名_ルート配送
   ,b.TERRITORY_CD             テリトリー
  ,g.ALLOC_BASE_ITEM_GRP_CD
  ,CASE b.TERRITORY_CD
    WHEN '1' THEN '千葉、神奈川、東京都町田市'
    WHEN '2' THEN '滋賀、京都、兵庫'
    WHEN '3' THEN '愛知、山口光市大字三輪'
    WHEN '5' THEN '広島'
    WHEN '6' THEN '茨城、栃木、埼玉'
    WHEN '7' THEN '宮城'
    WHEN 'B' THEN '奈良、和歌山'
    WHEN 'C' THEN '富山、石川、福井、岐阜、静岡、三重'
    WHEN 'D' THEN '熊本、大分、宮崎、鹿児島、沖縄'
    WHEN 'E' THEN '鳥取、島根、岡山、山口'
    WHEN 'F' THEN '北海道'
    WHEN 'G' THEN '青森、岩手、秋田、山形、福島'
    WHEN 'J' THEN '群馬、新潟、山梨、長野'
    WHEN 'K' THEN '東京都'
    WHEN 'P' THEN '徳島、香川、愛媛、高知'
    WHEN 'R' THEN '大阪'
    WHEN 'T' THEN '福岡、佐賀、長崎'
    ELSE ''
   END AS                     テリトリー名
  ,CASE b.LMT_SHIP_H_DAY_DELI_ENB_FLG
    WHEN '2' THEN '可能'
    WHEN '1' THEN ''
    ELSE '？'
   END AS                     限定出荷半日配送
  ,g.INV_GRP_CD               日本紙通商在庫区
  ,h.INV_GRP_NAME             日本紙通商在庫名
  ,case 
    when a.ADDRESS_CD like '34202%' then 'on'
    when a.ADDRESS_CD like '11201%' then 'on'
    when a.ADDRESS_CD like '11202%' then 'on'
    when a.ADDRESS_CD like '11210%' then 'on'
    else ''
  end                         配送暦flg
FROM
   TJFXX02D_ADDR_M a
  ,TJFXX02K_ADDRESS_AREA_M b
  ,TJFAX661_AREA_M c
  ,TJFCX511_INV_GRP_M d
  ,TJFAX643_DIST_BASE_JUDG_M e
  ,TJFAX641_DIST_BASE_M f
  ,TJFAX651_INV_GRP_JUDG_M g
  ,TJFCX511_INV_GRP_M h
WHERE a.ADDRESS_CD   = b.ADDRESS_CD
  AND b.AREA_CD      = c.AREA_CD
  AND e.AREA_CD      = b.AREA_CD
  AND f.DIST_BASE_CD = e.DIST_BASE_CD
  AND g.AREA_CD      = b.AREA_CD
  AND g.INV_GRP_CD   = h.INV_GRP_CD 
  AND c.NEARBY_SUPPLY_INV_GRP_CD = d.INV_GRP_CD
  AND g.ALLOC_BASE_ITEM_GRP_CD = 'Q00001'
  AND e.DELI_SERV_CTGR <> '16'
) WK_TBL
-- WHERE WK_TBL.住所コード='33205000000'
GROUP BY 
      WK_TBL.住所コード
     ,WK_TBL.削除
     ,WK_TBL.郵便番号
     ,WK_TBL.都道府県名
     ,WK_TBL.市区郡町村名
     ,WK_TBL.大字通称名
     ,WK_TBL.字名丁目
     ,WK_TBL.エリア
     ,WK_TBL.エリア名
     ,WK_TBL.最寄サプライ在庫区
     ,WK_TBL.最寄サプライ在庫区名
     ,WK_TBL.配送手段
     ,WK_TBL.配送方法
--     ,WK_TBL.配送サービス区分
     ,WK_TBL.テリトリー
     ,WK_TBL.テリトリー名
     ,WK_TBL.限定出荷半日配送
     ,WK_TBL.日本紙通商在庫区
     ,WK_TBL.日本紙通商在庫名
     ,WK_TBL.配送暦flg
ORDER BY WK_TBL.住所コード
