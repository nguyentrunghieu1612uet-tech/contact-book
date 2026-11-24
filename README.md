# 📒 Contact Book

Ứng dụng danh bạ chạy trên terminal, viết bằng Python.

## Tính năng
- Thêm liên hệ: chặn tên rỗng, trùng tên, trùng số; số điện thoại chỉ gồm chữ số
- Xoá liên hệ
- Tìm theo tên, không phân biệt hoa thường
- Hiển thị danh bạ sắp xếp theo tên
- Thoát an toàn bằng `0` hoặc `Ctrl + C`
- Tự động lưu danh bạ vào file `contact.json`, mở lại không mất dữ liệu

## Yêu cầu
Python 3.8 trở lên

## Cách chạy
```bash
python contact-book.py
```

Lần chạy đầu tiên, file `contact.json` sẽ được tạo trong thư mục dự án ở lần thêm liên hệ đầu tiên.
File này chứa dữ liệu cá nhân nên đã được đưa vào `.gitignore` và không được đẩy lên GitHub.

## Ví dụ
```
1-Thêm 2-Xoá 3-Tìm 4-Xem 0-Thoát
Chọn: 1
Nhập tên cần thêm: An
Nhập số: 0901
Đã thêm An
```

## Kiến thức đã dùng
- dict, list comprehension
- hàm với `return True/False`
- vòng lặp `while`, f-string
- xử lý lỗi `try/except` (`KeyboardInterrupt`, `FileNotFoundError`, `JSONDecodeError`)
- đọc/ghi file với `with open(...)`, module `json`
- `.gitignore` để không đưa dữ liệu cá nhân lên GitHub

## Kế hoạch
- [x] Kiểm tra dữ liệu nhập và thoát an toàn
- [x] Lưu danh bạ ra file JSON
- [ ] Tách code thành module