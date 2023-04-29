import unittest

from mrz.checker.td3 import TD3CodeChecker
from mrz.generator.td3 import TD3CodeGenerator, dictionary


class TestCase06(unittest.TestCase):
    mrz_str = "P<IND<<SHABEER<PUTHIYAVEETIL<ALIAMUNNY<<<<<<\nZ3560238<8IND7812101M2809012<<<<<<<<<<<<<<02"
    mrz_str_1 = "P<UKRTKACHENKO<<MARIANA<<<<<<<<<<<<<<<<<<<<<\nXX000000<0UKR9108242F23092571234567890<<<<70"

    def test_td3_checker(self):
        fields = TD3CodeChecker(self.mrz_str).fields()

        self.assertEqual("IND", fields.nationality)
        self.assertEqual("", fields.surname)
        self.assertEqual("SHABEER PUTHIYAVEETIL ALIAMUNNY", fields.name)

    def test_td3_checker_ukraine(self):
        fields = TD3CodeChecker(self.mrz_str_1).fields()

        self.assertEqual("UKR", fields.nationality)
        self.assertEqual("TKACHENKO", fields.surname)
        self.assertEqual("MARIANA", fields.name)

    def test_td3_generator(self):
        td3_generator = TD3CodeGenerator("P", "INDIA", "", "SHABEER PUTHIYAVEETIL ALIAMUNNY", "Z3560238", "INDIA",
                                              "781210", "M", "280901")

        result = self.mrz_str

        self.assertEqual(str(td3_generator), result)


if __name__ == '__main__':
    unittest.main()
