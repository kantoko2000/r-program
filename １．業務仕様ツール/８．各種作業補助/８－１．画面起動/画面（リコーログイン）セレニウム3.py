from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
import time

driver = webdriver.Chrome()
driver.get("https://www.vo3is.ricoh.co.jp/portal/index.jsp")

# ログイン
driver.find_element(By.ID, "userNameInput").click()
driver.find_element(By.NAME, "UserName").send_keys("kosaku.saito@jp.ricoh.com")
driver.find_element(By.ID, "passwordInput").click()
driver.find_element(By.NAME, "Password").send_keys("zaq12wsxcde3")
driver.find_element(By.ID, "submitButton").click()

# 会社選択
time.sleep(1)
driver.find_element(By.XPATH, '//input[@value="選択"]').click()

# 同意する
time.sleep(1)
driver.find_element(By.XPATH, '//input[@value="同意する"]').click()

wait = WebDriverWait(driver, 10)

# FFMをクリックしてサブメニューを表示
parent_menu = wait.until(
    EC.presence_of_element_located((By.ID, "_menu1menu1_10_1"))
)
driver.execute_script("arguments[0].click();", parent_menu)
time.sleep(1)

# 地区マスタメンテナンスをJavaScriptのCtrl+クリックで新しいタブで開く
submenu = wait.until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[24]/table/tbody/tr[1]/td[1]/div'))
)
driver.execute_script("""
    var event = new MouseEvent('click', {
        bubbles: true,
        cancelable: true,
        ctrlKey: true
    });
    arguments[0].dispatchEvent(event);
""", submenu)
time.sleep(1)

# 新しいタブに切り替え
driver.switch_to.window(driver.window_handles[-1])

print("ブラウザを閉じるとプログラムが終了します...")
while True:
    try:
        driver.title
        time.sleep(1)
    except WebDriverException:
        print("ブラウザが閉じられました。終了します。")
        break