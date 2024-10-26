n = int(input("Nhap so thanh vien HIT 15:"))

for i in range(n):
    print("Nhap thong cua thanh vien thu", i + 1)
    ten = input("Nhap ho ten:")
    tuoi = int (input("Nhap tuoi:"))
    gt = input("Gioi tinh:")
    tthn = input("Tinh trang hon nhan:")
    print("Ho va ten:",ten)
    print(f"Tuoi: = {tuoi}")
    print(f"Gioi tinh: = {gt}")
    print("Tinh trang hon nhan",tthn)
