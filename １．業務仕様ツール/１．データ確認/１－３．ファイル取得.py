# 実行ファイルのパスを取得
import os
import sys
# 実行ファイルがあるディレクトリの絶対パスを取得→相対パスで共通フォルダを設定
current_dir = os.path.dirname(os.path.abspath(__file__)) 
# '../..' で 2 つ上のディレクトリへ移動
common_folder_path = os.path.join(current_dir, '..', '..', '共通')
# sys.pathに共通フォルダを追加し、共通モジュールをインポートする
sys.path.append(common_folder_path)
from common_func import *
from typing import List

####関数####
tmp_dir = "c:/tmp/"


####メイン処理####
# メニューを表示  パターン１：SQL実行→コンソール出力、パターン２：エクセル出力
selected_Process = [
                 [ 0,"本番asyncログ",                 "1","","","",""]
                ,[ 1,"本番syncログ" ,                 "1","MOM社員コードを入力: ","","",""]
                ,[ 2,"本番file_use_state_webログ",        "1","受注番号を入力: ","","",""]
                ,[ 3,"キッティングパトロールメール対応", "1","","","",""]
                ]

# 入力引数のリスト
input_content: List[str] = ["", "", "", "", "", "", "", "", "", ""]

# メニューを表示
for row in selected_Process:
    print(str(row[0]) + ":" + row[1])

# ユーザーの選択に基づいて処理を分岐
choice = input("★選択肢を入力してくださいー＞")

# 全角入力しても大丈夫なように・・・
choice = fullwidth_to_halfwidth(choice)
choice_int = int(choice)

message1=""
message2=""
message3=""
message4=""
message5=""
message6=""

# メニューを表示
for row in selected_Process:
    if row[0]==choice_int:
        message1=row[1]
        message2=row[2]
        message3=row[3]
        message4=row[4]
        message5=row[5]
        message5=row[6]

# メッセージ取得
input_modifier="★★"
if message3 != "":
    input_content[0] = common_get_input(input_modifier+message3)

if message4 != "":
    input_content[1] = common_get_input(input_modifier+message4)

if message5 != "":
    input_content[2] = common_get_input(input_modifier+message5)

if message6 != "":
    input_content[3] = common_get_input(input_modifier+message6)

# SQLファイルパス設定
sql_file_path = common_get_file_path(os.path.dirname(os.path.abspath(__file__)),'sql',message1+'.sql')

print(message2)
if message2=='1' :
    # パターン１：ファイル取得
    common_file_get("ffm",sql_file_path,input_content)
elif message2=='2' :
    # パターン２：エクセル出力
    # エクセルファイル出力
    output_file_name=common_output_excel("ffm",sql_file_path,input_content)
    # エクセルファイル移動
    ido_saki_file_path=tmp_dir + common_get_filename_from_path(output_file_name)
    common_move_file(output_file_name,ido_saki_file_path)
    # エクセルファイル起動
    common_column_width_adjustment(ido_saki_file_path)
