contacts = {}   # dict: tên -> số điện thoại

def add_contact(name, phone):
    # TODO: thêm vào dict; nếu tên đã có thì báo trùng
    name=name.strip()
    phone=phone.strip()
    if name in contacts: 
        print("Tên trùng lặp")
        return False
    if phone in contacts.values(): 
        print("Số trùng lặp")
        return False
    contacts[name]=phone
    print(f"Đã thêm {name}")
    return True

def delete_contact(name):
    # TODO: xóa nếu tồn tại, ngược lại báo "không tìm thấy"
    name=name.strip()
    if name not in contacts:
        print("Tên không tồn tại.")
        return False
    phone=contacts.pop(name)
    print(f"Đã xoá {name}: {phone}")
    return True

def search_contact(keyword):
    # TODO: trả về list các tên có chứa keyword (không phân biệt hoa thường)
    keyword=keyword.strip()
    result=[x for x in contacts if keyword.lower() in x.lower()]
    if len(result)==0:
        print("Tên không tồn tại")
        return False
    for name in result:
        print(f"{name:<15}{contacts[name]}")
    return True

def show_all():
    # TODO: in danh bạ, sắp xếp theo tên
    if len(contacts)==0:
        print("Danh bạ trống")
    else:
        for name,phone in sorted(contacts.items()):
            print(f"{name:<15}{phone}")

def main():
    # TODO: vòng lặp while hiển thị menu 1-Thêm 2-Xóa 3-Tìm 4-Xem 0-Thoát
    while True:
        print("1-Thêm 2-Xoá 3-Tìm 4-Xem 0-Thoát")
        choice=input("Chọn: ")
        if choice=='1':
            name=input("Nhập tên cần thêm: ")
            phone=input("Nhập số: ")
            add_contact(name,phone)
        elif choice=='2':
            name=input("Nhập tên cần xoá: ")
            delete_contact(name)
        elif choice=='3':
            keyword=input("Nhập: ")
            search_contact(keyword)
        elif choice=='4':
            show_all()
        elif choice=='0':
            print("Tạm biệt!")
            break
        else:
            print("Không hợp lệ")

main()