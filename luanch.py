import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from tkinter import messagebox
from datetime import datetime
#ta quy định như sau dòng đầu tiên là dòng thời gian
#dòng thứ 2 là dòng tin nhắn 
#dòng thứ 3 là dòng id user
file_path='data.ini'
with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            c = file.readline().strip() #text
            e = file.readline().strip()  #time
            d = file.readline().strip()  # id

while True:
    now = datetime.now()  # Lấy thời gian hiện tại
    timeing = now.strftime("%Y-%m-%d %H:%M:%S")  # Định dạng thời gian theo chuẩn: Năm-Tháng-Ngày Giờ:Phút:Giây
    if e==timeing:
        def send_facebook_message(cookies_file, recipient_id, message):
            # Khởi tạo trình điều khiển Chrome
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            
            try:
                # Mở Facebook
                driver.get("https://www.facebook.com")

                # Tải cookie từ file
                with open(cookies_file, 'r', encoding='utf-8') as file:
                    cookies = json.load(file)

                # Thêm cookie vào trình duyệt
                for cookie in cookies:
                    driver.add_cookie(cookie)

                # Tải lại trang sau khi thêm cookie
                driver.get("https://www.facebook.com")

                # Chờ cho trang tải xong và tìm kiếm phần tử tin nhắn
                try:
                    # Truy cập vào trang nhắn tin của người nhận
                    driver.get(f"https://www.facebook.com/messages/t/{recipient_id}")

                    # Đợi ô nhập tin nhắn xuất hiện
                    message_box = WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "div[aria-label='Tin nhắn']"))
                    )

                    # Nhập tin nhắn
                    message_box.click()  # Click vào ô nhắn tin để đảm bảo nó được focus
                    message_box.send_keys(message)

                    # Sử dụng JavaScript để gửi phím Enter
                    driver.execute_script("arguments[0].dispatchEvent(new KeyboardEvent('keydown', {'key': 'Enter'}));", message_box)

                    # Đợi một thời gian ngắn để chắc chắn tin nhắn được gửi
                    time.sleep(2)

                    # Kiểm tra xem tin nhắn có xuất hiện trong cuộc hội thoại không
                    recent_messages = driver.find_elements(By.CSS_SELECTOR, "div[aria-label='Tin nhắn'] div[data-testid='message']")

                    if recent_messages:
                        messagebox.showinfo('Thông báo','Đã gửi tin nhắn ')
                    else:
                        messagebox.showinfo('Thông báo','Tin được gửi thành công')
                except Exception as e:
                    messagebox.showwarning('ERROR','ERROR CODE 505!')

            except Exception as e:
                    messagebox.showwarning('ERROR','ERROR CODE 505!')

            finally:
                # Đảm bảo rằng cửa sổ trình duyệt được đóng
                driver.quit()

        if __name__ == "__main__":
            # Thay đổi các thông tin ở đây
            cookies_file = 'facebook_cookies.json'  # File chứa cookie
            recipient_id = d  # ID người nhận
            message = c  # Tin nhắn bạn muốn gửi

            send_facebook_message(cookies_file, recipient_id, message)
