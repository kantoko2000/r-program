select 
a.COMPANY_CD                 会社コード,
a.INV_GRP_CD                 在庫区コード,
b.INV_GRP_NAME 在庫区名,
a.TERRITORY_CD               テリトリーコード,
decode(a.TERRITORY_CD,'1','千葉、神奈川、東京都町田市','2','滋賀、京都、兵庫','3','愛知、山口(光)','5','広島','6','茨城、栃木、埼玉','7','宮城','B','大阪地区(奈良、和歌山)','C','名古屋地区(富山、石川、福井、岐阜、静岡、三重)','D','福岡地区(熊本、大分、宮崎、鹿児島、沖縄)','E','広島地区(鳥取、島根、岡山、山口)','F','札幌地区(北海道)','G','仙台地区(青森、岩手、秋田、山形、福島)','J','関東地区(群馬、新潟、山梨、長野)','K','東京都','P','四国地区(徳島、香川、愛媛、高知)','R','大阪','T','福岡、佐賀、長崎','') テリトリ名,
DECODE (a.DELI_SERV_CTGR ,'11' ,'サプライ' ,'12' ,'ルート' ,'13' ,'マシン' ,'14' ,'混載' ,'15' ,'ベンダー' ,'16' ,'納期短縮' ,'17' ,'振替配送' ,'91' ,'配送不要' ,'不明') 配送サービス区分,
DECODE (a.INV_GRP_SPC_OPERATION_CTGR ,'11' ,'通常' ,'12' ,'大塚商会共同在庫' ,'13' ,'ＰＭＭＣ特別チャーター便','不明') 在庫区特別対応区分,
a.CLOSE_TIME                 締時刻,
a.REF_CLOSE_TIME             参照締時刻,
a.AM_CLOSE_TIME              午前締時刻,
a.AM_REF_CLOSE_TIME          午前参照締時刻,
a.PM_CLOSE_TIME              午後締時刻,
a.PM_REF_CLOSE_TIME          午後参照締時刻,
a.M_INVALID_FLG              マスタ無効フラグ
from
TJFAX664_ARRANGE_CLOSE_TIME_M a,TJFCX511_INV_GRP_M b
where 
a.INV_GRP_CD=b.INV_GRP_CD
and a.COMPANY_CD <>'000010'
order by a.INV_GRP_CD,a.TERRITORY_CD,a.DELI_SERV_CTGR
