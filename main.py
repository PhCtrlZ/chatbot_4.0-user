import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QThread, pyqtSignal
from QtGui import Ui_MainWindow
import os
from tkinter import messagebox


# Tạo một luồng xử lý riêng cho các tác vụ nặng
class WorkerThread(QThread):
    progress_signal = pyqtSignal(str)  # Tín hiệu để cập nhật giao diện (dòng trạng thái)

    def __init__(self, copy2, copy3, copy4):
        super().__init__()
        self.copy2 = copy2
        self.copy3 = copy3
        self.copy4 = copy4

    def run(self):
        path_w2 = 'data.ini'
        # Gửi tín hiệu cập nhật trạng thái
        self.progress_signal.emit('Hệ thống sẽ tự động lấy cookie cho bạn')

        # Xóa file nếu đã tồn tại
        if os.path.isfile(path_w2):
            os.remove(path_w2)

        u = self.copy4
        c = self.copy2
        n = self.copy3

        with open(path_w2, mode='a+', encoding='utf-8') as f:
            f.write('\n')
            f.writelines(u)
            f.write('\n')
            f.writelines(c)
            f.write('\n')
            f.writelines(n)

        # Cập nhật trạng thái hoàn tất
        self.progress_signal.emit('Hoàn thành việc ghi file')


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)

        self.uic.english.clicked.connect(self.english)
        self.uic.vietnam.clicked.connect(self.vietnam)
        self.uic.start.clicked.connect(self.start)
        self.uic.stop.clicked.connect(self.stop)
        self.uic.cookie.clicked.connect(self.cookie)

    def cookie(self):
        messagebox.showinfo('Thông báo', 'Sau đây bạn phải đăng nhập bằng tay nhé')
        os.startfile('getcookie.exe')

    def english(self):
        self.uic.label_3.setText('Set timer')
        self.uic.label_4.setText('Text')
        self.uic.label_5.setText('ID facebook')
        self.uic.label_6.setText('Table profile')
        self.uic.profile.setText('Convert language English successfully!!!')

    def vietnam(self):
        self.uic.label_3.setText('Cài đặt giờ')
        self.uic.label_4.setText('Lời nhắn')
        self.uic.label_5.setText('ID facebook')
        self.uic.label_6.setText('Table profile')
        self.uic.profile.setText('Đã chuyển qua ngôn ngữ tiếng Việt')

    def start(self):
        # Lấy dữ liệu từ giao diện người dùng
        copy2 = self.uic.time.toPlainText()
        copy3 = self.uic.id.toPlainText()
        copy4 = self.uic.text.toPlainText()

        # Kiểm tra các trường thông tin có bị trống hay không
        if not copy4.strip():
            messagebox.showerror("Thông báo", "Không được để trống ô tin nhắn")
            return
        if not copy2.strip():
            messagebox.showerror("Thông báo", "Không được để trống ô thời gian")
            return
        if not copy3.strip():
            messagebox.showerror("Thông báo", "Không được để trống ô ID fb")
            return

        # Tạo và chạy luồng xử lý
        self.worker_thread = WorkerThread(copy2, copy3, copy4)
        self.worker_thread.progress_signal.connect(self.update_profile)  # Kết nối tín hiệu để cập nhật trạng thái
        self.worker_thread.start()  # Bắt đầu luồng
        try:
            os.startfile('luanch.exe')
        except:
            messagebox.showerror("thông báo","ko thể tìm thấy đường dẫn đến file!")

    def update_profile(self, message):
        # Hàm này cập nhật giao diện (profile) với thông báo từ luồng phụ
        self.uic.profile.setText(message)

    def show(self):
        self.main_win.show()

    def stop(self):
        messagebox.showerror("Thông báo", "The tool has been stopped!")
        sys.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
