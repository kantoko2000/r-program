import win32com.client
import os
import sys
from datetime import datetime, timedelta

# 実行ファイルがあるディレクトリの絶対パスを取得→相対パスで共通フォルダを設定
# '../..' で 2 つ上のディレクトリへ移動
current_dir = os.path.dirname(os.path.abspath(__file__)) 
common_folder_path = os.path.join(current_dir, '..', '..', '..', '共通')

# sys.pathに共通フォルダを追加し、共通モジュールをインポートする
sys.path.append(common_folder_path)
from common_func import *
from typing import List

from datetime import datetime, timedelta

def get_file_name():
    #今日の日付と「前時〜現時」の範囲を組み合わせてファイル名を作成する。
    #例：16:55実行時 -> 20260312_1500-1600.html
    # 1. 現在時刻を取得
    now = datetime.now()
    
    # 2. 現在時刻の「分」以下を切り捨てて「現時00分」にする (例: 16:55 -> 16:00)
    current_hour_start = now.replace(minute=0, second=0, microsecond=0)
    
    # 3. 1時間前の「〇時00分」を計算 (例: 16:00 -> 15:00)
    one_hour_ago_start = current_hour_start - timedelta(hours=1)
    
    # 4. 文字列フォーマットを整える
    date_str = one_hour_ago_start.strftime("%Y%m%d")   # 20260312
    start_time_str = one_hour_ago_start.strftime("%H%M") # 1500
    end_time_str = current_hour_start.strftime("%H%M")   # 1600
    
    # 5. ファイル名を組み立て
    wk_title_name = f"{date_str}_{start_time_str}-{end_time_str}"
    
    return wk_title_name



# --- メイン処理 ---
# SQLファイルパスを取得
sql_file_path = common_get_file_path(current_dir,"sql",'AWR取得.sql')
print("sql_file_path:"+sql_file_path)

# 出力先ファイルのパス
output_html_path   = common_get_file_path(current_dir,'',get_file_name()  + '.html') 
print("output_html_path:"+output_html_path)

# csv出力
common_delete_file(output_html_path)
common_get_awr_report("ffm.dba",sql_file_path,output_html_path)

# 文字コード変換(utf8→sjis)
common_convert_encoding(1,output_html_path)

# ファイルをサーバに移動
ido_saki_file_path = r"X:\share\users\saito\■アーカイブ\▼AWR"
common_move_file(output_html_path,ido_saki_file_path)
