from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        # すでに起動しているChrome（ポート9222）に接続
        # これにより、専用ブラウザのダウンロードチェックを回避します
        browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        
        # 既存のページを取得、または新規ページ作成
        context = browser.contexts[0]
        page = context.new_page()
        
        # ★ここがポイント：コード生成パネル（Inspector）を強制起動
        page.pause()
        
        # ターゲットサイトへ移動
        page.goto("https://www.vo3is.ricoh.co.jp/portal/index.jsp")

if __name__ == "__main__":
    run()