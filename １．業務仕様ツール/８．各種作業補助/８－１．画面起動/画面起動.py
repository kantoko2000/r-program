import re
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    # メニューを表示
    print("--- 起動メニュー ---")
    print("1：講習 (Oracle Cloud)")
    print("2：図書館 (幸作ログイン・横浜市立図書館)")
    print("3：図書館 (颯ログイン・横浜市立図書館)")
    choice = input("どの画面を起動しますか？: ")

    # ブラウザ起動 (headless=False で画面を見せる)
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    if choice == "1":
        print("講習画面を起動します...")
        page.goto("https://mylearn.oracle.com/ou/course/oracle-cloud-infrastructure-architect-associate-2025-jp/152615/")
        page.get_by_role("button", name=" Account ").click()
        page.get_by_role("button", name="Sign in to my account").click()
        page.get_by_role("textbox", name="ユーザー名または電子メール").click()
        page.get_by_role("textbox", name="ユーザー名または電子メール").fill("kantoko2000@gmail.com")
        page.get_by_role("button", name="次").click()
        page.get_by_role("textbox", name="パスワード").click()
        page.get_by_role("textbox", name="パスワード").fill("Sai-444555")
        page.get_by_role("button", name="サイン・イン").click()
        page.get_by_role("textbox", name="パスコードの入力").click()
        # page.goto(url)
        # ここにOracle用のログイン処理などがあれば追加
        
    elif choice == "2":
        print("図書館画面を起動します...")
        url = "https://opac.lib.city.yokohama.lg.jp/winj/opac/top.do?lang=ja"
        page.goto(url)
        
        # 図書館用のログイン処理
        page.get_by_role("link", name="ログイン").click()
        page.get_by_role("textbox", name="図書館カード番号").fill("9031182660")
        page.get_by_role("textbox", name="パスワード").fill("sai-444555")
        page.get_by_role("button", name="ログイン").click()
        
        # ログイン後にMyライブラリへ移動
        if page.get_by_role("link", name="Myライブラリ").is_visible():
            page.get_by_role("link", name="Myライブラリ").click()
            
    elif choice == "3":
        print("図書館画面を起動します...")
        url = "https://opac.lib.city.yokohama.lg.jp/winj/opac/top.do?lang=ja"
        page.goto(url)
        
        # 図書館用のログイン処理
        page.get_by_role("link", name="ログイン").click()
        page.get_by_role("textbox", name="図書館カード番号").fill("9027524041")
        page.get_by_role("textbox", name="パスワード").fill("sai-444555")
        page.get_by_role("button", name="ログイン").click()
        
        # ログイン後にMyライブラリへ移動
        if page.get_by_role("link", name="Myライブラリ").is_visible():
            page.get_by_role("link", name="Myライブラリ").click()
            
    else:
        print("無効な選択です。終了します。")
        browser.close()
        return

    # 画面を閉じないように待機
    print("\n操作が完了しました。ブラウザを閉じるにはEnterキーを押してください...")
    input()

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)