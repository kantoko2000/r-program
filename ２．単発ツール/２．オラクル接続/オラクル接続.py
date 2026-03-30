# 実行ファイルのパスを取得
import os
import sys
# 実行ファイルがあるディレクトリの絶対パスを取得→相対パスで共通フォルダを設定
# '..' で一つ上のディレクトリに移動して共通フォルダへ
current_dir = os.path.dirname(os.path.abspath(__file__)) 
common_folder_path = os.path.join(current_dir, '..', '..','共通')  

# sys.pathに共通フォルダを追加し、共通モジュールをインポートする
sys.path.append(common_folder_path)
from common_func import *
from typing import List

####関数####

import subprocess

def execute_sqlplus_query(query):
    # SQL*Plusの接続情報
    user = "username"
    password = "password"
    host = "hostname:port/sid"

    # SQL*Plusコマンドの構築
    command = f"echo \"{query}\" | sqlplus -s {user}/{password}@{host}"


    connection_info = common_get_connection_info(connection_target)
    command = f"sqlplus  {connection_info['user']}/{connection_info['password']}@{connection_info['service_name']} @{sql_file_path}  {input_content[0]}  {input_content[1]}  {input_content[2]}  {input_content[3]}  {input_content[4]}  {input_content[5]}  {input_content[6]}  {input_content[7]}  {input_content[8]}  {input_content[9]} "
    print(command)





    # SQL*Plusを実行して結果を取得
    result = subprocess.run(command, shell=True, text=True, capture_output=True)

    # 実行結果を返す（標準出力をキャプチャ）
    return result.stdout

# 例: sysdateを取得
query = "SELECT TO_CHAR(SYSDATE, 'YYYY/MM/DD HH24:MI:SS') FROM dual;"
result = execute_sqlplus_query(query)

# 結果を表示
print(result)