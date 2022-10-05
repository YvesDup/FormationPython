import unittest

import class_cercle

class TestCercleInit(unittest.TestCase):
    def test_noparam(self):
        """ test la creatiion d'un cercle sans parametre"""
        with self.assertRaises(TypeError):
            class_cercle.Cercle()

    def test_too_many_params(self):
        """ test la creatiion d'un cercle avec trop de parametres"""
        with self.assertRaises(TypeError):
            class_cercle.Cercle(10, 20)

    def test_bad_type_param(self):
        """ test la creatiion d'un cercle avec mauvais type de parametre"""
        with self.assertRaises(TypeError):
            class_cercle.Cercle([])

    def test_bad_value_param(self):
        """ test la creatiion d'un cercle avec valeur inappropriée"""
        with self.assertRaises(ValueError):
            class_cercle.Cercle(-23.9)

    def test_good_param(self):
        """ test la creatiion d'un cercle avec bonne valeur"""
        c = None
        try:
            c = class_cercle.Cercle(10.5)
        except Exception:
            self.fail()
        else:
            self.assertIsNotNone(c)


if __name__ == '__main__':
    unittest.main()