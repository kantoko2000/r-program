import shutil
import glob
import os

src = r"X:\share\users\saito\■アーカイブ\▼AWR"
dst = r"C:\Users\g10012013\OneDrive - Ricoh\ツール\７．調査\①ＤＢ調査\AWR取得"

files = glob.glob(os.path.join(src, "*.html"))
print(f"{len(files)}件見つかりました")

for f in files:
    shutil.move(f, dst)
    print(f"移動: {os.path.basename(f)}")

print("完了")
