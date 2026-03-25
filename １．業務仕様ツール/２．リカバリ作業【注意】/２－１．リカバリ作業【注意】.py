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
# メニューを表示  パターン１：SQL実行→コンソール出力、パターン２：SQLファイル作成のみ、パターン３：SQL実行→コンソール出力 ffmdba
selected_Process = [
                 [ 0,"終了",                                                "1","","","",""]
                ,[ 1,"【JPI本番-3934】CE手配からのS01購買手配計画日時リカバリ","1","","","",""]
                ,[ 2,"売上予定一覧照会からの非表示対応",                      "1","問合せ番号を入力","","",""]
                ,[ 3,"検収確認登録画面からの非表示対応",                      "1","問合せ番号を入力","","",""]
                ,[ 4,"【PRB2022012600003】購買依頼取消承認処理で納期コメント履歴の連絡区分がNULL","1","受注番号を入力","","",""]
                ,[ 5,"受注搬入出明細タブ文字混入チェック","2","受注番号を入力","問合せ番号を入力","",""]
                ,[ 6,"TJFEX018_OTHCOM_PURC_L_この列に許容される指定精度より大きな値です","2","uniq_idを入力","","",""]
                ,[ 7,"【PRB2022112900001】セット化解除後にも関わらず、セット化マシン配送でＲＬＣに連携された（正しくは混載配送）","2","受注番号を入力","受注明細番号を入力","受注明細履歴番号を入力",""]
                ,[ 8,"セッションキル",                                      "3","sqlidを入力","","",""]
                ,[ 9,"役務手配作業履歴の外部連携データ送信済フラグを変更",     "2","inquiry_numを入力","SVC_ARR_NUMを入力","SVC_ARR_HIST_NUMを入力","SVC_ARR_SERV_HIST_NUMを入力"]
                ,[ 10,"【PRB2021031700005】【配送予約】注残品と下取のみ～",   "2","inquiry_numを入力","cr_l_numを入力","cr_numを入力",""]
                ,[ 11,"配送依頼キャンセル作成",                              "4","配送依頼管理番号を入力","","",""]
                ,[ 12,"入荷検収依頼キャンセル作成",                          "4","入荷検収依頼番号を入力","","",""]
                ,[ 13,"受注の依頼元課所コードを最新に更新",                   "2","受注番号を入力","","",""]
                ,[ 14,"【JPI本番-6495】Config在庫区と545在庫区のセット化配送で不正な配送指示","2","受注番号を入力","訂正出荷指示日を入力","配送依頼管理番号を入力",""]
                ,[ 15,"書面審査確定前にキャンセルされた受注の配送予約が残ってしまう","2","納品管理番号を入力","早期納品予約番号を入力","",""]
                ,[ 16,"1受注複数契約の売上予定が残ってしまう","2","売上予定番号を入力","","",""]
                ,[ 17,"作業またはキッティングの対象商品の一部だけを変更・取消できません","2","inquiry_numを入力","取消対象の商品コードを入力","",""]
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

if 0==choice_int:
   exit()

message1=""
message2=""
message3=""
message4=""
message5=""
message6=""

# メニューを表示
for row in selected_Process:
    if row[0]==choice_int:
        message1=row[1] # 作業内容
        message2=row[2] # 処理パターン
        message3=row[3] # 入力文字列指定１
        message4=row[4] # 入力文字列指定２
        message5=row[5] # 入力文字列指定３
        message6=row[6] # 入力文字列指定４

# メッセージ取得
input_header="★★"
input_footer="ー＞"

input_content[0] = message1 # 作業内容

if message3 != "": # 入力文字列指定１
    input_content[1] = common_get_input(input_header+message3+input_footer)

if message4 != "": # 入力文字列指定２
    input_content[2] = common_get_input(input_header+message4+input_footer)

if message5 != "": # 入力文字列指定３
    input_content[3] = common_get_input(input_header+message5+input_footer)

if message6 != "": # 入力文字列指定４
    input_content[4] = common_get_input(input_header+message6+input_footer)

# SQLファイルパス設定
sql_file_path = common_get_file_path(os.path.dirname(os.path.abspath(__file__)),'sql',message1+'.sql')

# パターン判定
if message2=='1' :
    # パターン１：SQL実行→コンソール出力
    common_kosin_sql_exe("ffm.kosin",current_dir,sql_file_path,input_content)
elif message2=='2' :
    # パターン２：SQLファイル作成のみ
    common_kosin_sql_make("ffm.st",current_dir,sql_file_path,input_content)
elif message2=='3' :
    # パターン３：SQL実行→コンソール出力 ffmdba
    common_kosin_sql_exe("ffm.dba",current_dir,sql_file_path,input_content)
elif message2=='4' :
    # パターン４：配送依頼、入荷依頼キャンセルファイル作成 
    # 置換文字列2：日時
    input_content[2] = common_get_YYYYMMDDHHMMSS()
    # 置換元ファイル：IFJFAPS57_JFAXSA014、IFJFAPS59_JFAXSA016
    if choice_int==11 :
        sql_file_path = common_get_folder_path(sql_file_path) + "/" + "IFJFAPS57_JFAXSA014"
    elif choice_int==12 :
        sql_file_path = common_get_folder_path(sql_file_path) + "/" + "IFJFAPS59_JFAXSA016"

    #print(common_get_folder_path(sql_file_path))
    #print("path"+sql_file_path)
    common_kosin_sql_make("ffm.st",current_dir,sql_file_path,input_content)
