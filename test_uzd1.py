import unittest

import uzd1
from uzd1 import *


class TestUzd1(unittest.TestCase):
    def test_skaiciu_suma(self):
        self.assertEqual(56, skaiciu_suma(45, 5, 6))
        self.assertNotEqual(55, skaiciu_suma(45, 5, 6))
        self.assertEqual(-34, skaiciu_suma(-45, 5, 6))

    def test_saraso_suma(self):
        self.assertEqual(95, saraso_suma([4, 5, 78, 8]))
        self.assertNotEqual(94, saraso_suma([4, 5, 78, 8]))
        self.assertEqual(69, saraso_suma([4, -5, 78, -8]))

    def test_didziausias_skaicius(self):
        self.assertEqual(78, didziausias_skaicius(4, 5, 78, 8))
        self.assertNotEqual(500, didziausias_skaicius(4, -500, 63, 8))
        self.assertEqual(8, didziausias_skaicius(4, 5, 8, -8))

    def test_didziausias_skaicius2(self):
        self.assertEqual(78, didziausias_skaicius(4, 5, 78, 8))
        self.assertNotEqual(500, didziausias_skaicius(4, -500, 63, 8))
        self.assertEqual(8, didziausias_skaicius(4, 5, 8, -8))

    def test_stringas_atbulai(self):
        self.assertEqual("8488 - satserevE", stringas_atbulai("Everestas - 8848"))
        self.assertNotEqual("8488 - saterevE", stringas_atbulai("Everestas - 8848"))
        self.assertEqual("ibilA", stringas_atbulai("Alibi"))

    def test_info_apie_sakini(self):
        self.assertEqual((6, 1, 20, 3), info_apie_sakini("Laba diena laba diena lab 522"))
        self.assertNotEqual((6, 1, 20, 4), info_apie_sakini("Laba diena laba diena lab 522"))
        self.assertEqual((7, 3, 47, 0),
                         info_apie_sakini("Pastaba: paleidžiant testą PyCharm programoje, to nereikia"))

    def test_unikalus_sarasas(self):
        self.assertEqual([4, 5, 'Labas', 6, True, 10],
                         unikalus_sarasas([4, 5, "Labas", 6, "Labas", True, 5, True, 10]))
        self.assertNotEqual([5, 5, 'Labas', 6, True, 10], unikalus_sarasas([4, 5, "Labas", 6, "Labas", True, 5, True, 10]))
        self.assertEqual([4, 5, 'Labas', 6, True, 10, False],
                         unikalus_sarasas([4, 5, "Labas", 6, "Labas", True, 5, True, 10, False, False]))

    def test_ar_pirminis(self):
        self.assertTrue(ar_pirminis(19))
        self.assertTrue(ar_pirminis(23))
        self.assertFalse(ar_pirminis(35))

    def test_isrikiuoti_nuo_galo(self):
        self.assertEqual("keturi trys du Vienas", isrikiuoti_nuo_galo("Vienas du trys keturi"))
        self.assertNotEqual("keturi du trys Vienas", isrikiuoti_nuo_galo("Vienas du trys keturi"))
        self.assertEqual("keturi trys1 du Vienas", isrikiuoti_nuo_galo("Vienas du trys1 keturi"))

    def test_ar_keliamieji(self):
        self.assertTrue(ar_keliamieji(2000))
        self.assertTrue(ar_keliamieji(1996))
        self.assertFalse(ar_keliamieji(2100))
        self.assertFalse(ar_keliamieji(1999))
        self.assertFalse(ar_keliamieji(2300))



    if __name__ == '__main__':
        unittest.main()
