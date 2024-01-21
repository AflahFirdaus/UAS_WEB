class Bentuk:
    def luas(self):
        pass


class Persegi(Bentuk):
    def luas(self, sisi, panjang=None):
        if panjang is not None:
            return sisi * panjang
        else:
            return sisi * sisi


persegi = Persegi()
print(persegi.luas(5))
print(persegi.luas(4, 6))
