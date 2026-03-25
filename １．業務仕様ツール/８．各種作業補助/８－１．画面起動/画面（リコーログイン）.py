import re
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    
    # ブラウザ起動 (headless=False で画面を見せる)
    #browser = playwright.chromium.launch(headless=False, slow_mo=500)
    browser = playwright.chromium.launch(headless=False, channel="chrome")
    context = browser.new_context()
    page = context.new_page()

    print("講習画面を起動します...")
    page.goto("https://www.vo3is.ricoh.co.jp/portal/index.jsp")
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
        
    # 画面を閉じないように待機
    print("\n操作が完了しました。ブラウザを閉じるにはEnterキーを押してください...")
    input()

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)