"""
2.

1. Pasiimti anksčiau sukurtą programos kodą
2. Teste sukurti setUp() metodą, kuriame būtų inicijuotas klasės objektas
3. Funkcijas perdaryti taip, kad jos gražintų duomenis
4. Sukurti UNIT testą visoms funkcijoms
5. Kiekvienai funkcijai turi būti mažiausiai 3 patikrinimai
6. Maksimaliai patobulinti kodą, nuolatos leidžiant sukurtą UNIT testą

"""


import unittest
from uzd2 import Sakinys

class TestKlases2(unittest.TestCase):
    def setUp(self) -> None:
        self.mano_sakinys = Sakinys("Mano tekstas yra toks")

    def test_atbulai(self):
        self.assertEqual("skot ary satsket onaM", self.mano_sakinys.atbulai())

    def test_didziosiomis(self):
        self.assertEqual("MANO TEKSTAS YRA TOKS", self.mano_sakinys.didziosiomis())

    def test_mazosiomis(self):
        self.assertEqual("mano tekstas yra toks", self.mano_sakinys.mazosiomis())

    def test_ieskoti(self):
        self.assertEqual(3, self.mano_sakinys.ieskoti("a"))

    def test_pakeisti(self):
        self.assertEqual("Savo tekstas yra toks", self.mano_sakinys.pakeisti("Mano", "Savo"))

    def test_atspausdintiZodi(self):
        self.assertEqual("yra", self.mano_sakinys.atspausdintiZodi(2))

    def test_info(self):
        self.assertEqual("Žodžių kiekis: 4, Skaičiai: 0, Didžiosios: 1, Mažosios: 17", self.mano_sakinys.info())