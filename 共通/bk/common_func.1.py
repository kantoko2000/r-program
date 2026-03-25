import cx_Oracle
import pandas as pd
import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows
import os
# 日付編集
from datetime import datetime
from dateutil.relativedelta import relativedelta
# CSV出力
import csv
# zip圧縮
import zipfile
#####共通関数記述は以降#####



# 【共通関数：0009】zip圧縮
#    呼出方法：
#    説明    ：入力「csvファイル名、zipファイル名」、出力「なし」
def common_csv_to_zip(csv_file_path, zip_file_path):
    # CSVファイルが存在するか確認
    if not os.path.exists(csv_file_path):
        print(f"CSVファイルが見つかりません: {csv_file_path}")
        return
    
    # ZIPファイルに圧縮
    with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # CSVファイルをZIPファイルに追加
        zipf.write(csv_file_path, os.path.basename(csv_file_path))
        print(f"{csv_file_path} を {zip_file_path} に圧縮しました。")


# 【共通関数：0008】CSV出力（データ抽出→ヘッダ付きで出力）
#    呼出方法：
#    説明    ：入力「connection_target→接続先、sql_file_path→実行するＳＱＬファイル」、出力「取得データ」
def common_get_dataToCsv(connection_target,sql_file_path,output_csv_path ):
    # 接続情報を取得
    connection_info = common_get_connection_info(connection_target)
    dsn_tns = cx_Oracle.makedsn(connection_info['ip'], connection_info['port'], service_name=connection_info['service_name'])
    conn    = cx_Oracle.connect(user=connection_info['user'], password=connection_info['password'], dsn=dsn_tns)
    cursor = conn.cursor()

    # SQLクエリを実行してデータを取得
    query = common_read_file(sql_file_path)
    cursor.execute(query)
    # カラム名（ヘッダー）を取得  col[0] はカラム名
    columns = [col[0] for col in cursor.description]
    formatted_columns = '"' + '","'.join(columns) + '"'
    #formatted_columns = ','.join(columns)
    print(columns)
    print(formatted_columns)
    data = cursor.fetchall()

    # 接続を閉じる
    cursor.close()
    conn.close()

    # ヘッダーを書き込む
    #common_write_to_csv(formatted_columns, output_csv_path)

    # CSV出力
    common_write_to_csv(data, output_csv_path,formatted_columns)  





# 【共通関数：0007】現在日時取得「20250107」形式
#    呼出方法：common_get_YYYYMMDD()
#    説明    ：入力「なし」、出力「なし」
def common_get_YYYYMMDD():
    return datetime.now().strftime('%Y%m%d')



# 【共通関数：0006】CSV出力
#    呼出方法：sql_file_path = common_get_file_path(os.path.dirname(os.path.abspath(__file__)),'sql',sql_file_name)
#    説明    ：入力「CSV出力する内容、出力ファイルのパス」、出力「なし」 encoding='utf-8'  sjis
def common_write_to_csv(data, output_file_path,header):
    # CSVファイルにデータを出力する
    with open(output_file_path, mode='w', newline='', encoding='utf-8', errors='replace') as file:
        writer = csv.writer(file)
        print("はいった")
        print(header)
        writer.writerow(header)

    with open(output_file_path, mode='a', newline='', encoding='utf-8', errors='replace') as file:
        writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_ALL)
        #writer.writerow(header)
        # ヘッダー行（キー名、またはカラム名）を書き込み
        #if len(data) > 0:
        #    header = data[0].keys() if isinstance(data[0], dict) else range(len(data[0]))
        #    writer.writerow(header)
        
        # データ行の書き込み
        for row in data[1:]:
            if isinstance(row, dict):
                writer.writerow(row.values())
            else:
                writer.writerow(row)


# 【共通関数：0005】ファイル名のパスを取得する
#    呼出方法：sql_file_path = common_get_file_path(os.path.dirname(os.path.abspath(__file__)),'sql',sql_file_name)
#    説明    ：入力「実行ファイルのディレクトリ、ターゲットファイルがあるディレクトリ、ターゲットファイル名」、出力「ターゲットファイルのフルパス」
def common_get_file_path(current_dir,target_dir,target_file_name ):
    target_file_path = os.path.join(current_dir, target_dir)
    target_file_path = os.path.join(target_file_path, target_file_name) 
    return target_file_path



# 【共通関数：0004】ＳＱＬ実行データ取得
#    呼出方法：data = common_get_data("syomen",sql_file_path)
#    説明    ：入力「connection_target→接続先、sql_file_path→実行するＳＱＬファイル」、出力「取得データ」
def common_get_data(connection_target,sql_file_path ):
    # 接続情報を取得
    connection_info = common_get_connection_info(connection_target)
    dsn_tns = cx_Oracle.makedsn(connection_info['ip'], connection_info['port'], service_name=connection_info['service_name'])
    conn    = cx_Oracle.connect(user=connection_info['user'], password=connection_info['password'], dsn=dsn_tns)
    cursor = conn.cursor()

    # SQLクエリを実行してデータを取得
    query = common_read_file(sql_file_path)
    cursor.execute(query)
    data = cursor.fetchall()

    # 接続を閉じる
    cursor.close()
    conn.close()
    return data


# 【共通関数：0003】接続情報取得
#    呼出方法：connection_info = common_get_connection_info("syomen" )
#    説明    ：入力「"syomen"→書面審査、"ffm"→FFM本体」、出力「接続情報」
def common_get_connection_info(connection_target ):
    # 接続情報を辞書形式で返す
    if connection_target=="syomen":
        connection_info = {
            'ip': '165.96.255.89',     
            'port': '1522',            
            'service_name': 'JFAG1',   
            'user': 'JFAX',            
            'password': '7qY2OehckN7Z' 
        }
    elif connection_target=="ffm":
            connection_info = {
            'ip': '165.96.255.70',     
            'port': '1521',            
            'service_name': 'JFXP1',   
            'user': 'JFXA002_J',            
            'password': 'rns7AXLJm94d' 
        }
    else:
        connection_info = None

    return connection_info


# 【共通関数：0002】前月の日付範囲を取得
#    呼出方法：date_range = get_previous_month_date_range()
#    説明    ：入力「なし」、出力「前月の日付範囲」
def common_get_previous_month_date_range():
    # 今日の日付を取得
    today = datetime.today()

    # 前月の1日を取得
    first_day_of_previous_month = (today.replace(day=1) - relativedelta(months=1)).replace(day=1)

    # 前月の最終日を取得
    last_day_of_previous_month = (today.replace(day=1) - relativedelta(days=1))

    # 前月の開始日と終了日を "YYYYMMDD" の形式にフォーマット
    start_date = first_day_of_previous_month.strftime('%Y%m%d')
    end_date = last_day_of_previous_month.strftime('%Y%m%d')

    # 結果として前月の日付範囲を作成
    return f"{start_date}-{end_date}"


# 【共通関数：0001】ファイルを読み込む関数
#    呼出方法：query = common_read_file(file_path)
#    説明    ：入力「ファイルのパス」、出力「読み込んだSQLファイルの内容」
def common_read_file(file_path):
    with open(file_path, 'r', encoding='shift_jis') as file:
        return file.read()

