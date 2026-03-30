# 実行ファイルのパスを取得
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
import re
####関数####
tmp_dir = "c:/tmp/"


# 【共通関数：0012】接続先、SQLファイル名を指定し、SQLplusを実行する
#    呼出方法：common_exe_sqlplus("ffm","select.sql")
#    説明    ：入力「接続先、SQLファイル名」、出力「なし」
def exe_sqlplus(connection_target,sql_file_path,input_content):

    # 接続情報の取得
    connection_info = common_get_connection_info(connection_target)
    command = f"sqlplus  {connection_info['user']}/{connection_info['password']}@{connection_info['service_name']} @{sql_file_path}  {input_content[0]}  {input_content[1]}  {input_content[2]}  {input_content[3]}  {input_content[4]}  {input_content[5]}  {input_content[6]}  {input_content[7]}  {input_content[8]}  {input_content[9]} "
    print(command)

    try:
        # subprocessを使ってコマンドを実行
        result = subprocess.run(command, capture_output=True, text=True, check=True, shell=True)
        print(result.stdout)
        return(result.stdout)
    except subprocess.CalledProcessError as e:
        return f"Error executing SQLPlus: {e.stderr}"




####メイン処理####
# 入力引数のリスト（カラでよし、定義のみ）
input_content: List[str] = ["", "", "", "", "", "", "", "", "", ""]

# メッセージ取得
print("BLOB内容取得")
input_content[0] = common_get_input("★★UNIQ IDを入力：")

# SQLファイルパス設定
sql_file_path = common_get_file_path(os.path.dirname(os.path.abspath(__file__)),'sql',"BLOB内容取得"+'.sql')

text=exe_sqlplus("ffm",sql_file_path,input_content)

# 改行で分割してリストにする
lines = text.splitlines()
# 最初の14行を削除し、残りの行を再度結合する
remaining_text = '\n'.join(lines[14:])
remaining_text = remaining_text.splitlines()
# 最後の7行を削除し、残りの行を再度結合する
remaining_text = '\n'.join(remaining_text[:-7])

remaining_text= '■■■'+input_content[0]+'■■■' +'\n'+remaining_text
common_put_clip_board(remaining_text)

print(remaining_text)

# 結果を確認するために一時停止する
command = f"pause"
result = subprocess.run(command, capture_output=True, text=True, check=True, shell=True)
