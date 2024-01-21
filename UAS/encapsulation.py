class Mobil:
    def __init__(self, merk, warna):
        self.__merk = merk
        self.__warna = warna 

    def set_merk(self, merk_baru):
        self.__merk = merk_baru

    def get_merk(self):
        return self.__merk

    def set_warna(self, warna_baru):
        self.__warna = warna_baru

    def get_warna(self):
        return self.__warna


mobil1 = Mobil("Toyota", "Hitam")

print(mobil1.get_merk()) 
print(mobil1.get_warna())

mobil1.set_merk("Honda") 
mobil1.set_warna("Merah")

print(mobil1.get_merk()) 
print(mobil1.get_warna())  

