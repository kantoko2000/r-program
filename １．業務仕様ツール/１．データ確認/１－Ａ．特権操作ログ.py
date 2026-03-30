import os
import datetime
import paramiko
import subprocess
from dateutil.relativedelta import relativedelta

# --- 設定情報 ---
HOSTNAME = '165.96.255.70'
USERNAME = 'jfxptokkenlog'
PASSWORD = 'jfxptokken01'

REMOTE_DIR = '/oradata/jfxp1/export/sox_log'
#BASE_PATH = r'X:\pm3share\保守運用\特権者操作ログ保管'
BASE_PATH = r'X:\pm3share\work\ipc\saito\特権テスト'
BAT_PATH = os.path.join(BASE_PATH, r'0.FFM\FFMD.bat')

def main():
    # 1. 日付計算
    # 今日が4/1であれば、target_month = "202603"
    today = datetime.date.today()
    last_month_date = today - relativedelta(months=1)
    target_month = last_month_date.strftime("%Y%m")
    
    # 2. 保存先フォルダの作成
    # X:\...\FFMW\202603 および X:\...\FFMD\202603
    paths = {
        "FFMW": os.path.join(BASE_PATH, 'FFMW', target_month),
        "FFMD": os.path.join(BASE_PATH, 'FFMD', target_month)
    }
    
    for p in paths.values():
        if not os.path.exists(p):
            os.makedirs(p)
            print(f"フォルダ作成: {p}")

    # 3. サーバ接続とファイル取得
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(HOSTNAME, username=USERNAME, password=PASSWORD)
        
        sftp = ssh.open_sftp()
        print(f"サーバ接続成功: {HOSTNAME}")

        # リモートディレクトリ内のファイル一覧を取得
        files = sftp.listdir(REMOTE_DIR)
        
        download_count = 0
        for file_name in files:
            target_local_dir = None
            
            # 条件：ファイル名に「先月(target_month)」の文字列が含まれているか
            if target_month in file_name:
                # FFMWファイルの判定
                if "R01_FFMW" in file_name:
                    target_local_dir = paths["FFMW"]
                
                # FFMDファイルの判定
                elif "R01_FFMD" in file_name:
                    target_local_dir = paths["FFMD"]

            # 該当する場合のみダウンロード
            if target_local_dir:
                remote_path = f"{REMOTE_DIR}/{file_name}"
                local_path = os.path.join(target_local_dir, file_name)
                
                print(f"取得中: {file_name}")
                sftp.get(remote_path, local_path)
                download_count += 1

        print(f"計 {download_count} 件のファイルをダウンロードしました。")
        sftp.close()
        ssh.close()
        
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return

    # 4. バッチファイルの実行
    if os.path.exists(BAT_PATH):
        print(f"バッチ実行開始: {BAT_PATH}")
        # バッチへ引数として対象年月(202603等)を渡して実行
        # cwd設定により、バッチ内の相対パス解決を確実にします
        subprocess.run([BAT_PATH, target_month], shell=True, cwd=os.path.dirname(BAT_PATH))
    else:
        print(f"バッチファイルが見つかりません: {BAT_PATH}")

if __name__ == "__main__":
    main()