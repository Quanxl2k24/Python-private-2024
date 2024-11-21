a = ("Nguyen Van F", "Nguyen Van B", "Nguyen Van C", "Nguyen Van D", "Nguyen Van E")
b = ("Nguyen Van A", "Nguyen Van C", "Nguyen Van D")

def check_in(a,b):
    for x in a:
        tmp = 0;
        for y in b:
            if x == y:
                tmp = 1;
        if tmp == 0:
            print(x)
print("Danh sach cac ban dang ki nhuung ko check in:")
check_in(a,b)

print(f"Tong so cac ban da dang ki:{len(a)}")
print(f"Tong so cac ban da check-in:{len(b)}")

def sapxep_kitu(a):
    sapxep_a = tuple(sorted(a))
    return sapxep_a

print(sapxep_kitu(a))