# class sinhvien:
#     def __init__(self, ten, tuoi, masv):
#         self.ten = ten
#         self.tuoi = tuoi
#         self.masv = masv
#
#     def display(self,stt):
#         print("Ten sinh vien: ",self.ten)
#         print("Tuoi: ", self.tuoi)
#         print("Ma sinh vien: ", self.masv)
#         print("STT: ", stt)
#
# SV = sinhvien("Nguyen va A", 18, 202360000)
# SV.display(1)

# class ClassA:
#     def inTT(self):
#         print("Xin chao")
# class ClassB:
#     def inTT(self):
#         print("Hello")
# class ClassC(ClassA, ClassB):
#     def inTT(self):
#         ClassB.inTT(self)
#
# C=ClassC()
# C.inTT()

class person:
    def __init__(self, ten, tuoi):
        self.__ten = ten
        self.__tuoi=tuoi
    def infor(self):
        print("Ten", self.__ten)
        print("Tuoi", self.__tuoi)
class sinhvien(person):
    def __init__(self, ten, tuoi, masv, diem):
        super().__init__(ten,tuoi)
        self.masv = masv
        self.diem = diem
    def infor(self):
        # print("Ten", self.__ten)
        # print("Tuoi", self.__tuoi)
        super().infor()
        print("masv: ", self.masv)
        print("diem: ", self.diem)

class Lophoc:
    def __init__(self, tenlop):
        self.tenlop = tenlop
        self.dssv = []

    def ThemSV(self, sinhvien):
        self.dssv.append(sinhvien)

    def XoaSV(self, sinhvien):
        self.dssv.remove(sinhvien)

    def inTT(self):
        print("Danh Sach lop: ", self.tenlop)
        for sinhvien in self.dssv:
            sinhvien.inTT()



lopa = Lophoc("Lop a")
Lopb = Lophoc("Lop b")

A = sinhvien("nam", 18, 2023600, 8.9)
B = sinhvien("a", 18, 2023, 7.0)

lopa.inTT()
