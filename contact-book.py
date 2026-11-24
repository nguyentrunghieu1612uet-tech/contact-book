import json

FILE="contact.json"

def save_contacts():
    with open(FILE,"w",encoding="utf8") as f:
        json.dump(contacts,f, ensure_ascii=False, indent=2)

def load_contacts():
    try:
        with open(FILE,encoding="utf8") as f:
            return json.load(f)
    except (FileNotFoundError,json.JSONDecodeError):
        return {}

contacts = load_contacts()

def add_contact(name, phone):
    name=name.strip()
    phone=phone.strip()
    if not name:
        print("Không thể để tên trống")
        return False
    if not phone.isdigit():
        print("Số không hợp lệ")
        return False
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
    name=name.strip()
    if name not in contacts:
        print("Tên không tồn tại.")
        return False
    phone=contacts.pop(name)
    print(f"Đã xoá {name}: {phone}")
    return True

def search_contact(keyword):
    keyword=keyword.strip()
    result=[x for x in contacts if keyword.lower() in x.lower()]
    if len(result)==0:
        print("Tên không tồn tại")
        return False
    for name in result:
        print(f"{name:<15}{contacts[name]}")
    return True

def show_all():
    if len(contacts)==0:
        print("Danh bạ trống")
    else:
        for name,phone in sorted(contacts.items()):
            print(f"{name:<15}{phone}")

def main():
    try:
        while True:
            print("1-Thêm 2-Xoá 3-Tìm 4-Xem 0-Thoát")
            choice=input("Chọn: ").strip()
            if choice=='1':
                name=input("Nhập tên cần thêm: ")
                phone=input("Nhập số: ")
                if add_contact(name,phone):
                    save_contacts()
            elif choice=='2':
                name=input("Nhập tên cần xoá: ")
                if delete_contact(name):
                    save_contacts()
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
    except (KeyboardInterrupt,EOFError):
        print("\nTạm biệt!")

main()