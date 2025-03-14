import time

import pandas as pd
import pyautogui
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from check_version import DICT_KIOT, convert_order

DOMAIN = "0588582715"
PW = "Linhan102"
download_dir = "C:\\Users\\Zefus\\Desktop\\Dâu"
user_data_dir = r"C:\Users\Zefus\AppData\Local\Google\Chrome\User Data"

if __name__ == '__main__':
    # Khởi tạo Options
    chrome_options = Options()
    # chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_argument(f"--remote-debugging-port=9222")
    chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
    chrome_options.add_argument(f"--profile-directory=Default")
    chrome_options.add_argument('--kiosk-printing')

    # chrome_options.add_experimental_option("prefs", {
    #     "download.default_directory": download_dir,  # Chỉ định thư mục tải file
    #     "download.prompt_for_download": False,  # Tắt hộp thoại tải file
    #     "download.directory_upgrade": True,
    #     "safebrowsing.enabled": True  # Đảm bảo rằng trình duyệt không yêu cầu xác nhận khi tải file
    # })

    # Khởi tạo Chrome
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    # Mở trang web
    driver.get(f"https://{DOMAIN}.kiotviet.vn/sale/#/")
    time.sleep(3)

    # read from excel and
    df = pd.read_excel("input_auto.xlsx", sheet_name="Sheet1", dtype=str)
    for item in df.itertuples():
        # Focus vào ô nhập KH:
        try:
            customerSearchInput = driver.find_element(By.ID, 'customerSearchInput')
            customerSearchInput.click()
            customerSearchInput.send_keys(item.phone)
            time.sleep(2)

        except NoSuchElementException:
            # Đã pick được KH rồi:
            deleteCustomer = driver.find_element(By.ID, 'deleteCustomer')
            deleteCustomer.click()
            # Tìm lại KH và bấm như bình thường
            customerSearchInput = driver.find_element(By.ID, 'customerSearchInput')
            customerSearchInput.click()
            customerSearchInput.send_keys(item.phone)
            time.sleep(2)
        # pick customer
        customerSearchInput.send_keys(Keys.RETURN)

        # check xem kh đã lên được chưa:
        try:
            icon_element = driver.find_element(By.XPATH, "//i[@class='fas fa-user']")
            infoCustomer = driver.find_element(By.ID, 'infoCustomer')
            infoCustomer.click()
            time.sleep(1)
        except NoSuchElementException:
            # chưa có trong hệ thống
            add_btn = driver.find_element(By.XPATH, "//i[@class='far fa-plus']")
            add_btn.click()
            time.sleep(1)

        customerName = driver.find_element(By.ID, 'customerName')
        customerName.clear()
        customerName.send_keys(item.customer)

        # Nếu là khách cũ và item.address is nan thì không fill vào address nữa
        if pd.isna(item.address):
            pass
        else:
            address = driver.find_element(By.ID, 'address')
            address.clear()
            address.send_keys(item.address)
        saveCusBtn = driver.find_element(By.ID, 'saveCusBtn')
        saveCusBtn.click()
        time.sleep(5)


        # Nhập số lượng hàng hóa cần mua
        list_product = convert_order(item.order)
        temp_kg = 0
        is_combo = False
        for product in list_product:
            kiotviet_product_code = DICT_KIOT[product['product']]
            kiotviet_product_quantity = product['quantity']
            # check freeship (combo or > 2kg)
            temp_kg += kiotviet_product_quantity
            if 'cb' in product['product']:
                is_combo = True

            productSearchInput = driver.find_element(By.ID, 'productSearchInput')
            productSearchInput.clear()
            productSearchInput.send_keys(kiotviet_product_code)
            time.sleep(1)
            productSearchInput.send_keys(Keys.RETURN)
            time.sleep(1)
            productQtyInput = driver.find_element(By.ID, 'productQtyInput')
            productQtyInput.send_keys(kiotviet_product_quantity)
            productQtyInput.send_keys(Keys.RETURN)

            # Điều chỉnh giá nếu có

        # Nhập ghi chú
        note_area = driver.find_element(By.XPATH, "//textarea[contains(@placeholder, 'Ghi chú đơn hàng')]")
        note_area.clear()
        note_area.send_keys(item.note if not pd.isna(item.note) else '')

        saveTransactionNormal = driver.find_element(By.ID, 'saveTransactionNormal')
        saveTransactionNormal.click()
        time.sleep(2)

        # Check FreeShip or not
        if not (temp_kg >= 2 or is_combo):
            # Có ship, không phải làm gì
            pass
        else:
            # Freeship cần sửa
            btnSurcharge = driver.find_element(By.ID, 'btnSurcharge')
            btnSurcharge.click()
            time.sleep(1)
            buttonSurchargeModal = driver.find_element(By.XPATH, "//button[text()='25,000']")
            buttonSurchargeModal.click()
            priceInput = WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.ID, "priceInput"))
            )
            priceInput.clear()
            priceInput.send_keys("0")

            # close modal
            # close_modal = driver.find_element(By.XPATH, "//a[@class='k-window-action k-link']")
            close_modal = driver.find_element(By.XPATH, "//div[@class='k-overlay']")
            close_modal.click()

        saveTransactionRegPmt = WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable((By.ID, 'saveTransactionRegPmt'))
        )
        # saveTransactionRegPmt = driver.find_element(By.ID, 'saveTransactionRegPmt')
        saveTransactionRegPmt.click()
        time.sleep(3)

        # pyautogui.press('enter')
        time.sleep(3)

    # In tiêu đề trang
    print("Tiêu đề trang:", driver.title)

    # Đóng trình duyệt (luôn dùng quit() thay vì close())
    input("hello")
    driver.quit()
