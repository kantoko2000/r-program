import os
# 実行ファイルがあるディレクトリの絶対パスを取得→相対パスで共通フォルダを設定
current_dir = os.path.dirname(os.path.abspath(__file__)) 
# 対象フォルダ
BASE_DIR = r"C:\ローカルツール\python\２．単発ツール\３．大塚投入データ出力\入力ファイル"
# 実行中スクリプトのあるフォルダ
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
# '../..' で 2 つ上のディレクトリへ移動
common_folder_path = os.path.join(current_dir, '..', '..', '共通')

KEY_FILE = "キーファイル.txt"
OUTPUT_FILE = "大塚データ読込.出力ファイルテキスト.txt"


def main():
    key_file_path = os.path.join(BASE_DIR, KEY_FILE)

    # --- 1. キーファイル読み込み（SJIS） ---
    with open(key_file_path, "r", encoding="shift_jis") as f:
        keys = [line.strip() for line in f if line.strip()]

    # --- 2. データファイル一覧 ---
    data_files = [
        os.path.join(BASE_DIR, fname)
        for fname in os.listdir(BASE_DIR)
        if fname != KEY_FILE and os.path.isfile(os.path.join(BASE_DIR, fname))
    ]

    # --- 出力ファイル初期化（UTF-8 で出力、SJISが良ければ変更可能）---
    with open(os.path.join(OUTPUT_DIR, OUTPUT_FILE), "w", encoding="shift_jis") as out:
        pass

    # 3. 各キーコードで処理
    for key in keys:
        for file_path in data_files:
            process_file(file_path, key)

def normalize_dash(s: str) -> str:
    """ダッシュ類を全角ハイフン '－' に統一する"""
    if not s:
        return s
    # よくあるダッシュ類を全角ハイフンに置換
    return (s.replace('−', '－')   # U+2212 MINUS SIGN
             .replace('-', '－')  # ASCII HYPHEN-MINUS
             .replace('–', '－')  # en dash
             .replace('—', '－')  # em dash
             .replace('﹣', '－')  # small variants
           )

def process_file(file_path, key):
    """データファイルを読み、該当キー行と後続行を出力する"""
    output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)

    # --- データファイル読み込み（SJIS） ---
    with open(file_path, "r", encoding="shift_jis", errors="ignore") as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        line = lines[i]
        prefix = line[:3]

        # 3. 先頭3バイトがD01 かつ キーが含まれる？
        if prefix == "D01" and key in line:
            with open(output_path, "a", encoding="shift_jis") as out:  # SJIS 出力が良ければ変更可
                # 最初の一致行を出力
                out.write(normalize_dash(line))

                i += 1
                # 次の行以降
                while i < len(lines):
                    next_line = lines[i]
                    next_prefix = next_line[:3]

                    # D01 または D00 が来たら終了
                    if next_prefix in ("D01", "D00"):
                        break

                    out.write(next_line)
                    i += 1
        else:
            i += 1


if __name__ == "__main__":
    main()
