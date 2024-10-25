from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json
import time

# Hàm để lưu cookie sau khi đã đăng nhập thủ công vào Facebook
def save_cookies(driver, cookies_file):
    cookies = driver.get_cookies()
    with open(cookies_file, 'w', encoding='utf-8') as file:
        json.dump(cookies, file, ensure_ascii=False)
    print(f"Cookies đã được lưu vào {cookies_file}")

if __name__ == "__main__":
    # Khởi tạo trình điều khiển Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Mở Facebook và chờ bạn đăng nhập thủ công
    driver.get("https://www.facebook.com")
    time.sleep(30)  # Thời gian để bạn hoàn tất việc đăng nhập (30 giây)

    # Sau khi đăng nhập, lưu cookie vào file JSON
    cookies_file = 'facebook_cookies.json'
    save_cookies(driver, cookies_file)

    # Đóng trình duyệt sau khi hoàn thành
    driver.quit()
