import subprocess
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.rizm.st.vo3is.ricoh.co.jp/portal/"

# ① Chromeを強制終了
subprocess.run(["taskkill", "/f", "/im", "chrome.exe"], 
               stdout=subprocess.DEVNULL, 
               stderr=subprocess.DEVNULL)

# 少し待機（終了を待つ）
time.sleep(1)

# ② Chromeを起動
chrome_paths = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    rf"C:\Users\{os.getlogin()}\AppData\Local\Google\Chrome\Application\chrome.exe",
]

for path in chrome_paths:
    if os.path.exists(path):
        subprocess.Popen([path, url])
        break
else:
    print("Chromeが見つかりませんでした")

# ② Seleniumでクロームを起動
driver = webdriver.Chrome()
driver.get(url)

# テキストで検索（最も確実）
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), '詳細設定')]"))
)
button.click()