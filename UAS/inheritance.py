class Kendaraan:
    def __init__(self, merk, tahun, warna):
        self.merk = merk
        self.tahun = tahun
        self.warna = warna

    def info(self):
        return f"Kendaraan: {self.merk}, Tahun: {self.tahun}, Warna: {self.warna}"


class Mobil(Kendaraan):
    def __init__(self, merk, tahun, warna, jenis):
        super().__init__(merk, tahun, warna)
        self.jenis = jenis

    def info(self):
        return f"Mobil: {self.merk}, Tahun: {self.tahun}, Warna: {self.warna}, Jenis: {self.jenis}"


class Motor(Kendaraan):
    def __init__(self, merk, tahun, warna, kapasitas):
        super().__init__(merk, tahun, warna)
        self.kapasitas = kapasitas

    def info(self):
        return f"Motor: {self.merk}, Tahun: {self.tahun}, Warna: {self.warna}, Kapasitas Mesin: {self.kapasitas}"


mobil = Mobil("Toyota", 2020, "Hitam", "Sedan")
print(mobil.info())

motor = Motor("Honda", 2019, "Merah", "150 cc")
print(motor.info())
