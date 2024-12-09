import subprocess
import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

DOMAIN = "0588582715"
PW = "Linhan102"


if __name__ == '__main__':
    # Chạy Chrome chuyên dụng:
    # Chạy lệnh CMD
    # command = [
    #     r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    #     "--remote-debugging-port=9222",
    #     r"--user-data-dir=C:\Users\AnMV\AppData\Local\Google\Chrome\User Data"
    # ]
    # subprocess.run(command)
    bat_file = r'C:\Users\AnMV\Desktop\run_chrome.bat'
    subprocess.run([bat_file], shell=True)

    time.sleep(2)

    # Thiết lập ChromeOptions để kết nối với trình duyệt đang mở
    chrome_options = Options()
    chrome_options.debugger_address = "127.0.0.1:9222"

    # Kết nối với trình duyệt hiện tại
    driver = webdriver.Chrome(service=Service("chromedriver.exe"), options=chrome_options)

    # Mở một trang web
    driver.get(f"https://{DOMAIN}.kiotviet.vn/man/#/Invoices")

    # Click Filter
    try:
        time_filter = WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located((By.ID, "reportsortDateTimeLbl"))
        )
        time_filter.click()
    except TimeoutException:
        raise Exception("Time too long")

    time.sleep(1)
    # Click Hôm nay
    try:
        to_day_lbl = WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, "//a[text()='Hôm nay' and @class='ng-binding']"))
        )
        to_day_lbl.click()
    except TimeoutException:
        raise Exception("Time too long")

    time.sleep(1)
    # Click export file dropdown list
    try:
        btn_file = WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, "//a[contains(@class, 'kv2BtnExport') and @title='Xuất  file']"))
        )
        btn_file.click()
    except TimeoutException:
        raise Exception("Time too long")

    time.sleep(1)
    # Click export file
    try:
        export_file = WebDriverWait(driver, 10).until(
            ec.visibility_of_element_located((By.XPATH, "//a[@ng-click='export()' and @class='ng-binding']"))
        )
        export_file.click()
    except TimeoutException:
        raise Exception("Time too long")

    # In tiêu đề trang
    print(driver.title)
    input("Testing system")

    # Đóng trình duyệt
    driver.quit()
