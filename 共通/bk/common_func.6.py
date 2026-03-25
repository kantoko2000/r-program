import cx_Oracle
import pandas as pd
import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows
import os
# 日付編集
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
# CSV出力
import csv
# zip圧縮
import zipfile
# コマンド実行
import subprocess
# ファイルコピー
import shutil
# エクセル操作
import pyautogui
# 時間に関する
import time
import threading
# クリップボードにコピー
import pyperclip
#####共通関数記述は以降#####




# 【共通関数：0024】接続先、SQLファイル名を指定し、SQLplusを実行する
#    呼出方法：common_kosin_sql_exe("ffm","select.sql")
#    説明    ：入力「接続先、SQLファイル名」、出力「なし」
def common_kosin_sql_exe3(connection_target, current_dir, sql_file_path, input_content):

    # 接続情報の取得
    connection_info = common_get_connection_info(connection_target)

    #sqlplus_command = f'sqlplus -s  {connection_info['user']}/{connection_info['password']}@{connection_info['service_name']} @{sql_file_path}  {input_content[0]}  {input_content[1]}  {input_content[2]}  {input_content[3]}  {input_content[4]}  {input_content[5]}  {input_content[6]}  {input_content[7]}  {input_content[8]}  {input_content[9]}'
    bat_arg1=connection_info['user']
    bat_arg2=connection_info['password']
    bat_arg3=connection_info['service_name']
    bat_arg4=sql_file_path
    bat_arg5=current_dir

    bat_input1=input_content[0]
    bat_input2=input_content[1]
    bat_input3=input_content[2]
    bat_input4=input_content[3]
    bat_input5=input_content[4]
    bat_input6=input_content[5]
    bat_input7=input_content[6]
    bat_input8=input_content[7]
    bat_input9=input_content[8]
    bat_input10=input_content[9]

    print(bat_input1)

    # 実行するバッチファイルと引数
    bat_file = r"C:\ローカルツール\python\データ更新___注意\データ更新___注意.bat"
    arguments = [bat_arg1, bat_arg2, bat_arg3,bat_arg4,bat_arg5,bat_input1,bat_input2,bat_input3,bat_input4,bat_input5,bat_input6,bat_input7,bat_input8,bat_input9,bat_input10]  # 引数のリスト

    command = f'start "" "{bat_file}" ' + ' '.join(arguments)

    # バッチファイルを切り離して非同期に実行（出力やエラーは無視）
    subprocess.Popen(command, shell=True,stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


 



# 【共通関数：0024】接続先、SQLファイル名を指定し、SQLplusを実行する
#    呼出方法：common_kosin_sql_exe("ffm","select.sql")
#    説明    ：入力「接続先、SQLファイル名」、出力「なし」
def common_kosin_sql_exe2(connection_target,sql_file_path,input_content):

    # 接続情報の取得
    connection_info = common_get_connection_info(connection_target)

    # SQLクエリ
    sql_query = "SELECT * FROM dual;"  # 実行したいSQL文をここに

    # ログファイル名
    log_file = "sqlplus_log.txt"

    sqlplus_command = f'sqlplus -s  {connection_info['user']}/{connection_info['password']}@{connection_info['service_name']} @{sql_file_path}  {input_content[0]}  {input_content[1]}  {input_content[2]}  {input_content[3]}  {input_content[4]}  {input_content[5]}  {input_content[6]}  {input_content[7]}  {input_content[8]}  {input_content[9]}'

    # SQL*Plusコマンドを実行
    process = subprocess.Popen(
        sqlplus_command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # SQLクエリを送信して実行
    #sql_input = f"{sql_query}\nEXIT;\n"
    sql_input = f"{sql_query}\n"
    stdout, stderr = process.communicate(input=sql_input)

    # 結果をコンソールに出力
    print("SQL Execution Result:")
    print(stdout)

    # エラーメッセージを表示（あれば）
    if stderr:
        print("Error:")
        print(stderr)

    # 実行結果をログファイルに保存
    with open(log_file, 'w') as f:
        f.write(stdout)
        if stderr:
            f.write("\nErrors:\n")
            f.write(stderr)

 





# 【共通関数：0024】接続先、SQLファイル名を指定し、SQLplusを実行する
#    呼出方法：common_kosin_sql_exe("ffm","select.sql")
#    説明    ：入力「接続先、SQLファイル名」、出力「なし」
def common_kosin_sql_exe(connection_target,sql_file_path,input_content):

    # 接続情報の取得
    connection_info = common_get_connection_info(connection_target)

    # コマンドプロンプトのコマンドを組み立て
    command = f'start cmd.exe /K sqlplus -s  {connection_info['user']}/{connection_info['password']}@{connection_info['service_name']} @{sql_file_path}  {input_content[0]}  {input_content[1]}  {input_content[2]}  {input_content[3]}  {input_content[4]}  {input_content[5]}  {input_content[6]}  {input_content[7]}  {input_content[8]}  {input_content[9]}'

    print(command)
    try:
        # 新しいcmd.exeウィンドウでsqlplusを実行
        subprocess.Popen(command, shell=True,stdout=subprocess.PIPE)
        print(f"SQLPlus has been executed in a new window with the command: {command}")

    except subprocess.CalledProcessError as e:
        print(f"Error executing SQL*Plus: {e}")







# 【共通関数：0023】クリップボードにコピーする
#    呼出方法：common_get_YYYYMMDD_hhmm()
#    説明    ：入力「なし」、出力「なし」
def common_put_clip_board(text):
    pyperclip.copy(text)
    return text


# 【共通関数：0022】ファイル起動し、列調整する
#    呼出方法：common_get_YYYYMMDD_hhmm()
#    説明    ：入力「なし」、出力「なし」
def common_column_width_adjustment(file_path):
    os.startfile(file_path)
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'a')
    # Alt -> H -> O -> I で幅を自動調整
    pyautogui.hotkey('alt', 'h', 'o', 'i')  
    # 先頭を選択する
    pyautogui.hotkey('ctrl', 'home')


# 【共通関数：0021】フルパスから、ファイル名だけ取得する
#    呼出方法：common_get_YYYYMMDD_hhmm()
#    説明    ：入力「なし」、出力「なし」
def common_get_filename_from_path(file_path):
    return os.path.basename(file_path)

# 【共通関数：0020】現在日時取得「20250107_1251」形式
#    呼出方法：common_get_YYYYMMDD_hhmm()
#    説明    ：入力「なし」、出力「なし」
def common_get_YYYYMMDD_hhmm():
    return datetime.now().strftime('%Y%m%d_%H%M')




# 【共通関数：0019】接続先、SQLファイル名を指定し、SQLを実行→エクセルに出力する
#    呼出方法：common_exe_sqlplus("ffm","select.sql")
#    説明    ：入力「接続先、SQLファイル名」、出力「なし」
def common_output_excel(connection_target,sql_file_path,input_content):

    # 接続情報の取得
    connection_info = common_get_connection_info(connection_target)

    # Oracle接続情報の設定
    dsn_tns = cx_Oracle.makedsn(connection_info['ip'], connection_info['port'], service_name=connection_info['service_name'])
    conn = cx_Oracle.connect(user=connection_info['user'], password=connection_info['password'], dsn=dsn_tns)

    # SQLファイルを読み込む
    query = common_read_file(sql_file_path)
    # データの取得
    df = pd.read_sql(query, conn)
    # DataFrame全体を文字列として処理
    df = df.applymap(str)

    # 取得したデータをエクセルに保存
    output_file_name=sql_file_path+'.'+common_get_YYYYMMDD_hhmm()+'.xlsx'
    df.to_excel(output_file_name, index=False, engine='openpyxl')

    # openpyxlを使ってExcelファイルに保存
    wb = openpyxl.Workbook()
    ws = wb.active
    # DataFrame を openpyxl ワークシートに変換して書き込む
    for row in dataframe_to_rows(df, index=False, header=True):
        ws.append(row)
    
    # セルの書式設定を行い、すべてを文字列として保存
    for row in ws.iter_rows():
        for cell in row:
            cell.number_format = '@'  # 文字列形式に設定
    
    # 取得したデータをエクセルに保存
    wb.save(output_file_name)

    return output_file_name

        




# 【共通関数：0018】ファイル移動
#    呼出方法：date_range = get_previous_month_date_range()
#    説明    ：入力「変換モード（1:utf8→sjisに変換、2:sjis→utf8）、変換対象ファイル名、出力ファイル名」、出力「なし」
def common_move_file(source, destination):
    # ファイルを移動
    shutil.move(source, destination)
    print(f"ファイル {source} を {destination} に移動しました。")



# 【共通関数：0018】ディレクトリ作成
#    呼出方法：date_range = get_previous_month_date_range()
#    説明    ：入力「変換モード（1:utf8→sjisに変換、2:sjis→utf8）、変換対象ファイル名、出力ファイル名」、出力「なし」
def common_create_directory(directory_path):
    # ディレクトリがすでに存在するかチェック
    if not os.path.exists(directory_path):
        # ディレクトリを作成
        os.makedirs(directory_path)
        print(f"ディレクトリ '{directory_path}' を作成しました。")
    else:
        print(f"ディレクトリ '{directory_path}' はすでに存在します。")


# 【共通関数：0017】ファイルコピー
#    呼出方法：date_range = get_previous_month_date_range()
#    説明    ：入力「変換モード（1:utf8→sjisに変換、2:sjis→utf8）、変換対象ファイル名、出力ファイル名」、出力「なし」
def common_copy_file(source, destination):

    # ファイルをコピー
    shutil.copy(source, destination)
    print(f"ファイル {source} を {destination} にコピーしました。")





# 【共通関数：0016】全角文字を半角に変換
#    呼出方法：date_range = get_previous_month_date_range()
#    説明    ：入力「変換モード（1:utf8→sjisに変換、2:sjis→utf8）、変換対象ファイル名、出力ファイル名」、出力「なし」
def fullwidth_to_halfwidth(text: str) -> str:
    # 全角から半角への変換テーブル
    fullwidth = "０１２３４５６７８９ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"
    halfwidth = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    
    # 変換テーブルを作成
    translation_table = str.maketrans(fullwidth, halfwidth)
    
    # 変換を実行して返す
    return text.translate(translation_table)


# 【共通関数：0015】ファイルをリネーム
#    呼出方法：date_range = get_previous_month_date_range()
#    説明    ：入力「変換モード（1:utf8→sjisに変換、2:sjis→utf8）、変換対象ファイル名、出力ファイル名」、出力「なし」
def common_rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"ファイル名が '{old_name}' から '{new_name}' に変更されました。")
    except FileNotFoundError:
        print(f"ファイル '{old_name}' が見つかりませんでした。")
    except PermissionError:
        print(f"ファイル '{old_name}' をリネームする権限がありません。")
    except Exception as e:
        print(f"ファイルのリネーム中にエラーが発生しました: {e}")

# 【共通関数：0014】ファイル削除
#    呼出方法：date_range = get_previous_month_date_range()
#    説明    ：入力「変換モード（1:utf8→sjisに変換、2:sjis→utf8）、変換対象ファイル名、出力ファイル名」、出力「なし」
def common_delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"ファイル '{file_path}' は削除されました。")
    except FileNotFoundError:
        print(f"ファイル '{file_path}' が見つかりませんでした。")
    except PermissionError:
        print(f"ファイル '{file_path}' を削除する権限がありません。")
    except Exception as e:
        print(f"ファイル '{file_path}' の削除中にエラーが発生しました: {e}")

# 【共通関数：0013】文字コード変換
#    呼出方法：date_range = get_previous_month_date_range()
#    説明    ：入力「変換モード（1:utf8→sjisに変換、2:sjis→utf8）、変換対象ファイル名、出力ファイル名」、出力「なし」
def common_convert_encoding(convert_mode,input_file_path):
    # 指定された内容で文字コード変換する
    if convert_mode == 1:
        read_encoding='utf-8'
        write_encoding='shift_jis'
    else:
        read_encoding='shift_jis'
        write_encoding='utf-8'

    # UTF-8で読み込み
    with open(input_file_path, mode='r', encoding=read_encoding) as infile:
        content = infile.read()

    output_file_path=input_file_path + '.convert'

    # SJISで書き込み
    with open(output_file_path, mode='w', encoding=write_encoding, errors='ignore') as outfile:
        outfile.write(content)
    
    # 元のファイルを削除する
    common_delete_file(input_file_path)

    # 変換後ファイル名をリネームする
    common_rename_file(output_file_path,input_file_path)
    


# 【共通関数：0012】接続先、SQLファイル名を指定し、SQLplusを実行する
#    呼出方法：common_exe_sqlplus("ffm","select.sql")
#    説明    ：入力「接続先、SQLファイル名」、出力「なし」
def common_exe_sqlplus(connection_target,sql_file_path,input_content):

    # 接続情報の取得
    connection_info = common_get_connection_info(connection_target)
    command = f"sqlplus  {connection_info['user']}/{connection_info['password']}@{connection_info['service_name']} @{sql_file_path}  {input_content[0]}  {input_content[1]}  {input_content[2]}  {input_content[3]}  {input_content[4]}  {input_content[5]}  {input_content[6]}  {input_content[7]}  {input_content[8]}  {input_content[9]} "
    print(command)

    try:
        # subprocessを使ってコマンドを実行
        result = subprocess.run(command, capture_output=True, text=True, check=True, shell=True)
        print(result.stdout)
        command = f"pause"
        # 結果を確認するために一時停止する
        result = subprocess.run(command, capture_output=True, text=True, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        return f"Error executing SQLPlus: {e.stderr}"

        



# 【共通関数：0011】入力を取得する
#    呼出方法：date_range = get_previous_month_date_range()
#    説明    ：入力「問合せ文言」、出力「入力内容」
def common_get_input(prompt):
    
    #入力を要求し、ユーザーからの入力を返す関数。
    #入力が空であった場合、再度入力を要求する。
    # 末尾の空白を削除
    prompt = prompt.rstrip() 
    while True:
        user_input = input(prompt)
        if user_input.strip():  # 入力が空でないかチェック
            return user_input
        else:
            print("入力は空であってはいけません。もう一度入力してください。")


# 【共通関数：0010】１週間期間を取得
#    呼出方法：date_range = get_previous_month_date_range()
#    説明    ：入力「なし」、出力「前月の日付範囲」
def common_get_previous_week_date_range():
    # 今日の日付
    today = datetime.today()

    # 開始日: 今日から7日前
    start_date = today - timedelta(days=7)

    # 終了日: 今日から1日前
    end_date = today - timedelta(days=1)

    # "YYYYMMDD"形式にフォーマット
    start_date_str = start_date.strftime("%Y%m%d")
    end_date_str = end_date.strftime("%Y%m%d")

    # 結果として前月の日付範囲を作成
    return f"{start_date_str}-{end_date_str}"



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
#    呼出方法：common_get_dataToCsv("ffm",sql_file_path,output_csv_path)
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
    header = '"' + '","'.join(columns) + '"'

    # データ取得
    data = cursor.fetchall()

    # 接続を閉じる
    cursor.close()
    conn.close()

    # CSV出力
    common_write_to_csv(data, output_csv_path,header)  





# 【共通関数：0007】現在日時取得「20250107」形式
#    呼出方法：common_get_YYYYMMDD()
#    説明    ：入力「なし」、出力「なし」
def common_get_YYYYMMDD():
    return datetime.now().strftime('%Y%m%d')



# 【共通関数：0006】CSV出力
#    呼出方法：common_write_to_csv(data, output_csv_path,header)  
#    説明    ：入力「CSV出力する内容、出力ファイルのパス」、出力「なし」 encoding='utf-8'  sjis
def common_write_to_csv(data, output_file_path,header):
    # CSVファイルにデータを出力する
    with open(output_file_path, mode='w', newline='', encoding='utf-8', errors='replace') as file:
        writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_ALL)

        # ヘッダーをそのまま書き込む
        file.write(header + "\n")  
        
        # データ行の書き込み
        for row in data:
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
    elif connection_target=="ffm.st":
            connection_info = {
            'ip': '165.96.255.141',     
            'port': '1522',            
            'service_name': 'JFXR1',   
            'user': 'JFXA001_J',            
            'password': 'XAhZQwihe29D' 
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

