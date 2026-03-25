from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
import time

# --- 1. ブラウザの初期設定 ---
options = Options()
# 会社PCでの安定性を高める設定（自動操作の検知を回避）
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# Selenium 4.6以降の標準機能でブラウザを起動
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15)

try:
    # --- 2. ログイン処理 ---
    portal_url = "https://www.vo3is.ricoh.co.jp/portal/index.jsp"
    #portal_url = "https://www.rizm.st.vo3is.ricoh.co.jp/portal/"
    driver.get(portal_url)
    
    # ユーザー名とパスワードの入力
    wait.until(EC.presence_of_element_located((By.ID, "userNameInput"))).send_keys("kosaku.saito@jp.ricoh.com")
    driver.find_element(By.NAME, "Password").send_keys("zaq12wsxcde3")
    #wait.until(EC.presence_of_element_located((By.ID, "userNameInput"))).send_keys("mms88026236@jp-ngt.ricoh.com")
    #driver.find_element(By.NAME, "Password").send_keys("testpass2008")
    driver.find_element(By.ID, "submitButton").click()

    # --- 3. 会社選択・同意（クリック可能になるまで待機） ---
    wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="選択"]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="同意する"]'))).click()

    # --- 4. FFMメニューの展開 ---
    # FFM親メニューがクリック可能になるまで待機
    parent_menu = wait.until(EC.element_to_be_clickable((By.ID, "_menu1menu1_10_1")))
    # JavaScriptを使用して確実にメニューをクリック
    driver.execute_script("arguments[0].click();", parent_menu)
    
    # サブメニューが描画されるのを少し待つ
    time.sleep(1.5)

    # --- 5. ターゲット画面の起動とポータルの復元（1ウィンドウ2タブ化） ---
    # 地区マスタメンテナンス（子メニュー）を待機
    submenu = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[24]/table/tbody/tr[1]/td[1]/div')))

    print("マスタ画面へ移動します...")
    # 確実にクリックして、今のタブで画面を遷移させる
    submenu.click()
    
    # 画面が切り替わるのを少し待つ
    time.sleep(2)

    print("別タブで元のポータルを復元します...")
    # JavaScriptで新しいタブを作成し、そこにポータルを読み込む
    # これにより、1つのウィンドウに「マスタ」と「ポータル」が並びます
    driver.execute_script(f"window.open('{portal_url}', '_blank');")
    
    # 念のため、新しく開いたポータル側のタブに操作対象を移しておく
    driver.switch_to.window(driver.window_handles[-1])

    print("完了！ 1つのウィンドウにマスタ画面とポータルが揃いました。")

    # --- 6. 終了待機ロジック（ブラウザを閉じるとプログラム終了） ---
    print("ブラウザを閉じるとプログラムが終了します...")
    while True:
        try:
            _ = driver.title
            time.sleep(1)
        except WebDriverException:
            print("ブラウザが閉じられました。終了します。")
            break

except Exception as e:
    print(f"エラーが発生しました: {e}")

finally:
    # エラー時もブラウザを維持するため、ここでは quit() しません
    pass