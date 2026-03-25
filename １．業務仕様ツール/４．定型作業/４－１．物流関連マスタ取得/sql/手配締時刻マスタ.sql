--2025/9/10  52147件
select 
 a.COMPANY_CD                 会社コード
,a.INV_GRP_CD                 在庫区コード
,b.INV_GRP_NAME 在庫区名
,a.TERRITORY_CD               テリトリーコード
,CASE a.TERRITORY_CD
       WHEN '1' THEN '千葉、神奈川、東京都町田市'
       WHEN '2' THEN '滋賀、京都、兵庫'
       WHEN '3' THEN '愛知、山口(光)'
       WHEN '5' THEN '広島'
       WHEN '6' THEN '茨城、栃木、埼玉'
       WHEN '7' THEN '宮城'
       WHEN 'B' THEN '大阪地区(奈良、和歌山)'
       WHEN 'C' THEN '名古屋地区(富山、石川、福井、岐阜、静岡、三重)'
       WHEN 'D' THEN '福岡地区(熊本、大分、宮崎、鹿児島、沖縄)'
       WHEN 'E' THEN '広島地区(鳥取、島根、岡山、山口)'
       WHEN 'F' THEN '札幌地区(北海道)'
       WHEN 'G' THEN '仙台地区(青森、岩手、秋田、山形、福島)'
       WHEN 'J' THEN '関東地区(群馬、新潟、山梨、長野)'
       WHEN 'K' THEN '東京都'
       WHEN 'P' THEN '四国地区(徳島、香川、愛媛、高知)'
       WHEN 'R' THEN '大阪'
       WHEN 'T' THEN '福岡、佐賀、長崎'
       WHEN 'O' THEN '沖縄(販売店マスタ使用不可)'
    ELSE '該当なし'
  END テリトリ名
,CASE A.DELI_SERV_CTGR
    WHEN '11' THEN 'サプライ'
    WHEN '12' THEN 'ルート'
    WHEN '13' THEN 'マシン'
    WHEN '14' THEN '混載'
    WHEN '15' THEN 'ベンダー'
    WHEN '16' THEN '納期短縮'
    WHEN '17' THEN '振替配送'
    WHEN '91' THEN '配送不要'
    ELSE '該当なし'
  END 配送サービス区分
,CASE A.DELI_SERV_CTGR
    WHEN '11' THEN '通常'
    WHEN '12' THEN '大塚商会共同在庫'
    WHEN '13' THEN 'ＰＭＭＣ特別チャーター便'
    ELSE '不明'
  END 在庫区特別対応区分
  ,a.CLOSE_TIME                 締時刻
  ,a.REF_CLOSE_TIME             参照締時刻
  ,a.AM_CLOSE_TIME              午前締時刻
  ,a.AM_REF_CLOSE_TIME          午前参照締時刻
  ,a.PM_CLOSE_TIME              午後締時刻
  ,a.PM_REF_CLOSE_TIME          午後参照締時刻
  ,a.M_INVALID_FLG              マスタ無効フラグ
 from
   TJFAX664_ARRANGE_CLOSE_TIME_M a,TJFCX511_INV_GRP_M b
 where a.INV_GRP_CD=b.INV_GRP_CD
   and a.COMPANY_CD <>'000010'
order by a.INV_GRP_CD,a.TERRITORY_CD,a.DELI_SERV_CTGR
