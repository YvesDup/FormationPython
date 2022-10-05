# reprendre la classe Parallelo et mettre en place un TestCase sur la creation de l'objet méthode __init__
import unittest

import exo20 as parallelo

class TestParalleloInit(unittest.TestCase):
    """Test de la methode __init__ de la classe"""
    def test_not_enough_param(self):
        pass

    def test_too_many_param(self):
        pass

    def test_bad_type_param(self):
        with self.assertRaises(TypeError):
            parallelo.Parallelo("10", 20, 50)

        with self.assertRaises(TypeError):
            parallelo.Parallelo(10, [20], 50)

        with self.assertRaises(TypeError):
            parallelo.Parallelo(10, 20, "50")

    def test_bad_value_param(self):
        with self.assertRaises(ValueError):
            parallelo.Parallelo(-100, 20, 50)

        with self.assertRaises(ValueError):
            parallelo.Parallelo(-10, -5, 50)

        with self.assertRaises(ValueError):
            parallelo.Parallelo(100, 20, 50)

        # ici l'angle > 45 (je crois)
        with self.assertRaises(ValueError):
            parallelo.Parallelo(10, 20, 30)

if __name__ == '__main__':
    unittest.main()


# reprndre une methode de la classe et de la tester