# 実行ファイルのパスを取得
import os
import sys

# 実行ファイルがあるディレクトリの絶対パスを取得→相対パスで共通フォルダを設定
# '../..' で 2 つ上のディレクトリへ移動
current_dir = os.path.dirname(os.path.abspath(__file__)) 
common_folder_path = os.path.join(current_dir, '..', '..', '..', '共通')

# sys.pathに共通フォルダを追加し、共通モジュールをインポートする
sys.path.append(common_folder_path)
from common_func import *

# 物流関連マスタ格納フォルダ
#logi_master_dir = r"\\expfs01.ty1.unics.ricoh.com\ricoh41\pm3share\保守運用\アプリ作業依頼\■データ抽出依頼\物流関連マスタ取得（ロジ依頼）\\"
logi_master_dir = r"\\z2stzsmbxx0199.file.core.windows.net\z2sh16000zsmb199\pm3share\保守運用\アプリ作業依頼\■データ抽出依頼\物流関連マスタ取得（ロジ依頼）\\"

####メイン処理####
# リストを作成
syori_taisyo = ["搬入出付帯作業実施可否マスタ","顧客納品リードタイム決定マスタ_マシン配送・サプライ在庫区","顧客納品リードタイム決定マスタ_マシン配送・マシン在庫区","物流拠点間リードタイム決定マスタ","地区マスタ","顧客納品リードタイム決定マスタ_マシン配送以外全て","手配締時刻マスタ","在庫区決定マスタ","配送パターン決定マスタ","顧客納品リードタイム決定マスタ_混載配送(物流拠点130006、270019)","顧客納品リードタイム決定マスタ_混載配送(物流拠点130006、270019、010001、040001、230001、340001、410001、460001、160001)"]
#syori_taisyo = ["地区マスタ"]

# リモートのzipファイルをすべて削除する
common_delete_files("zip",logi_master_dir)
# ローカルのcsvファイルをすべて削除する
common_delete_files("csv",current_dir)

for i in range(len(syori_taisyo)):

    # SQLファイルパスを取得
    sql_file_path = common_get_file_path(current_dir,'sql',syori_taisyo[i]+'.sql')

    # 出力先ファイルのパス
    output_csv_path   = common_get_file_path(current_dir,'',common_get_YYYYMMDD()+'_'+syori_taisyo[i]  + '.csv') 

    # zipファイルのパス
    output_zip_path   = common_get_file_path(current_dir,'',common_get_YYYYMMDD()+'_'+syori_taisyo[i]  + '.zip') 

    # csv出力
    common_get_dataToCsv("ffm",sql_file_path,output_csv_path)

    # 文字コード変換(utf8→sjis)
    common_convert_encoding(1,output_csv_path)

    # zipに圧縮
    common_csv_to_zip(output_csv_path,output_zip_path)

    # 作成したファイルを格納ディレクトリにコピー
    common_move_file(output_zip_path, logi_master_dir)


