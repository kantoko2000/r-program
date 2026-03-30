import win32com.client
import os
import sys
# 実行ファイルがあるディレクトリの絶対パスを取得→相対パスで共通フォルダを設定
# '../..' で 2 つ上のディレクトリへ移動
current_dir = os.path.dirname(os.path.abspath(__file__)) 
common_folder_path = os.path.join(current_dir, '..', '..', '共通')

# sys.pathに共通フォルダを追加し、共通モジュールをインポートする
sys.path.append(common_folder_path)
from common_func import *
from typing import List

# --- 件数チェック処理 ---
def get_csv_row_count(file_path):
    with open(file_path, 'r', encoding='shift_jis') as f:
        # csv.readerを使って行を数える
        reader = csv.reader(f)
        data = list(reader)
        return len(data)

def send_via_outlook_app(file_path,wk_title_name):
    # Outlookアプリを起動（または接続）
    outlook = win32com.client.Dispatch("Outlook.Application")
    
    # 新しいメールアイテムを作成
    mail = outlook.CreateItem(0) 
    
    # メールの設定
    mail.To = "kosaku.saito@jp.ricoh.com"
    mail.Subject = "■調査用通知■"+wk_title_name
    mail.Body = ""
    
    # 添付ファイルの追加（※フルパスで指定する必要があります）
    if os.path.exists(file_path):
        # abspathで絶対パスに変換するのが確実です
        mail.Attachments.Add(os.path.abspath(file_path))
    
    # 送信！
    try:
        mail.Send()
        print("Outlookアプリ経由で送信しました！")
    except Exception as e:
        print(f"送信失敗: {e}")

# --- メイン処理 ---
# 引数の取得
# 作業タイトルを設定
wk_title_name = sys.argv[1]
print(wk_title_name)

#wk_title_name="売上取消→売上先取消"

# SQLファイルパスを取得
sql_file_path = common_get_file_path(current_dir,"sql",wk_title_name +'.sql')
print("sql_file_path:"+sql_file_path)

# 出力先ファイルのパス
output_csv_path   = common_get_file_path(current_dir,'',wk_title_name  + '.csv') 
print("output_csv_path:"+output_csv_path)

# csv出力
common_delete_file(output_csv_path)
common_get_dataToCsv("ffm",sql_file_path,output_csv_path)

# 行数を取得
row_count = get_csv_row_count(output_csv_path)

# 判定：1件以下（ヘッダーのみ、または空）なら終了
if row_count <= 1:
    print("抽出データが0件（ヘッダーのみ）のため、処理を終了します。")
    # ここでプログラムを終了させる
    import sys
    sys.exit() 

# 文字コード変換(utf8→sjis)
common_convert_encoding(1,output_csv_path)

# 前段の処理で作ったファイル名を指定
send_via_outlook_app(output_csv_path,wk_title_name)

