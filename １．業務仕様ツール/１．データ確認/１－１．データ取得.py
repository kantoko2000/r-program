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

####関数####
tmp_dir = "c:/tmp/"


####メイン処理####
# メニューを表示  パターン１：SQL実行→コンソール出力、パターン２：エクセル出力
selected_Process = [
                 [ 0,"終了",                                      "1","","","",""]
                ,[ 1,"社員情報取得",                               "1","MOM社員コードを入力: ","","",""]
                ,[ 2,"受注番号→問合せ番号",                         "1","受注番号を入力: ","","",""]
                ,[ 3,"キッティングパトロールメール対応",             "1","","","",""]
                ,[ 4,"作業依頼受付番号→問合せ番号",                 "1","作業依頼受付番号を入力: ","","",""]
                ,[ 5,"エラー返却確認",                             "1","UNIQ IDを入力: ","","",""]
                ,[ 6,"AJJFAXM590必須項目チェック",                 "1","","","",""]
                ,[ 7,"入庫予定リカバリチェック",                    "1","問合せ番号を入力: ","問合せ明細番号を入力: ","",""]
                ,[ 8,"単独下取で住所マスタに存在しない郵便番号を使用","1","住所一部を入力: ","","",""]
                ,[ 9,"当日発生エラーリスト",                        "2","","","",""]
                ,[ 10,"リランステータス確認",                       "1","UNIQ IDを入力: ","","",""]
                ,[ 11,"注文番号→問合せ番号",                        "1","注文番号を入力: ","","",""]
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
    # パターン１：SQL実行→コンソール出力
    common_exe_sqlplus("ffm",sql_file_path,input_content)
elif message2=='2' :
    # パターン２：エクセル出力
    # エクセルファイル出力
    output_file_name=common_output_excel("ffm",sql_file_path,input_content)
    # エクセルファイル移動
    ido_saki_file_path=tmp_dir + common_get_filename_from_path(output_file_name)
    common_move_file(output_file_name,ido_saki_file_path)
    # エクセルファイル起動
    common_column_width_adjustment(ido_saki_file_path)
