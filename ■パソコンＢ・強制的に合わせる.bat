# 1. リモートの最新情報を取得（まだ中身は変わりません）
git fetch origin

# 2. ローカルの「master」ブランチを、リモートの「origin/master」と完全に一致させる
# ※ これにより、パソコンBにある未コミットの変更や衝突はすべて消去されます
git reset --hard origin/master
