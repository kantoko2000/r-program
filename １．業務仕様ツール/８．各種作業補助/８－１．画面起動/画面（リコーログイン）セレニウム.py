from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException  # ← これが必要！
import time

# 普通のChromeをそのまま使う（会社の証明書も引き継がれる）
driver = webdriver.Chrome()

# サイトを開く
driver.get("https://www.vo3is.ricoh.co.jp/portal/index.jsp")

# 例：ボタンをクリック
driver.find_element(By.ID, "userNameInput").click()
driver.find_element(By.NAME, "UserName").send_keys("kosaku.saito@jp.ricoh.com")

driver.find_element(By.ID, "passwordInput").click()
driver.find_element(By.NAME, "Password").send_keys("zaq12wsxcde3")

# サインインボタンをクリック ← ここを追加
driver.find_element(By.ID, "submitButton").click()

# パターン1：ボタンのテキストで探す（一番試しやすい）
driver.find_element(By.XPATH, '//input[@value="選択"]').click()

# 「同意する」ボタンをクリック
time.sleep(1)  # 画面読み込み待ち
driver.find_element(By.XPATH, '//input[@value="同意する"]').click()


time.sleep(1)

# FFMをJavaScriptでクリック（通常クリックできない要素に有効）
parent_menu = wait.until(
    EC.presence_of_element_located((By.ID, "_menu1menu1_10_1"))
)
driver.execute_script("arguments[0].click();", parent_menu)
time.sleep(1)

# 地区マスタメンテナンスも同様にJavaScriptでクリック
submenu = wait.until(
    EC.presence_of_element_located((By.XPATH, '//*[contains(text(),"地区マスタメンテナンス")]'))
)
driver.execute_script("arguments[0].click();", submenu)
# こちらも同様に右クリック→検証でXPathを確認してください
# driver.find_element(By.XPATH, '//*[contains(text(),"FFM")]').click()

# サブメニューが表示されるまで少し待つ
time.sleep(1)
# サブメニューも同様にdivで探す
driver.find_element(By.XPATH, '//div[contains(text(),"FFM")]').click()
# サブメニュー「地区マスタメンテナンス」をクリック
#driver.find_element(By.XPATH, '//a[contains(text(),"FFM")]').click()



# ブラウザが閉じられるまで待機
print("ブラウザを閉じるとプログラムが終了します...")
while True:
    try:
        driver.title  # ブラウザが生きているか確認
        time.sleep(1)
    except WebDriverException:
        print("ブラウザが閉じられました。終了します。")
        break
#driver.quit()