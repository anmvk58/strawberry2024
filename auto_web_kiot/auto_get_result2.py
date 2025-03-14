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
download_dir = "C:\\Users\\Zefus\\Desktop\\Dâu"

if __name__ == '__main__':
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    user_data_dir = r"C:\Users\Zefus\AppData\Local\Google\Chrome\User Data"

    chrome_options = Options()
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_argument(f"--remote-debugging-port=9222")
    chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
    chrome_options.add_argument(f"--profile-directory=Default")

    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,  # Chỉ định thư mục tải file
        "download.prompt_for_download": False,  # Tắt hộp thoại tải file
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True  # Đảm bảo rằng trình duyệt không yêu cầu xác nhận khi tải file
    })

    # Kết nối với trình duyệt hiện tại
    driver = webdriver.Chrome(service=Service("chromedriver.exe"), options=chrome_options)

    # Mở một trang web
    driver.get(f"https://{DOMAIN}.kiotviet.vn/man/#/Invoices")

    # Click Filter
    try:
        time_filter = WebDriverWait(driver, 30).until(
            ec.visibility_of_element_located((By.ID, "reportsortDateTimeLbl"))
        )
        time_filter.click()
    except TimeoutException:
        raise Exception("Time too long")

    # Click Hôm nay
    time.sleep(1)
    try:
        to_day_lbl = WebDriverWait(driver, 30).until(
            ec.visibility_of_element_located((By.XPATH, "//a[text()='Hôm nay' and @class='ng-binding']"))
        )
        to_day_lbl.click()
    except TimeoutException:
        raise Exception("Time too long")

    # Click export file dropdown list
    time.sleep(1)
    try:
        btn_file = WebDriverWait(driver, 30).until(
            ec.visibility_of_element_located(
                (By.XPATH, "//a[contains(@class, 'kv2BtnExport') and @title='Xuất  file']"))
        )
        btn_file.click()
    except TimeoutException:
        raise Exception("Time too long")

    # Click export file
    time.sleep(1)
    try:
        export_file = WebDriverWait(driver, 30).until(
            ec.visibility_of_element_located((By.XPATH, "//a[@ng-click='export()' and @class='ng-binding']"))
        )
        export_file.click()
    except TimeoutException:
        raise Exception("Time too long")

    # Rename file download to right format:


    # In tiêu đề trang
    input("Testing system")

    # Đóng trình duyệt
    driver.quit()
