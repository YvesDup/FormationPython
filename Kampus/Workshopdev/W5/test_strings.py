import unittest

class TestStringMethods(unittest.TestCase):
    """"""

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


class TestStringImmutable(unittest.TestCase):
    def test_immutable(self):
        self.assertTrue(1 > 0)


class TestSetupFail(unittest.TestCase):
    def setUp(self):
        super().setUp()
        try:
            1/0
        except:
            print("setUp failed")
            raise

    def test_run(self):
        print("test_run done !!")

    def tearDown(self):
        print("tearDown done !!")


class TestComplete(unittest.TestCase):
    def setUp(self):
        super().setUp()
        print("setUp ok")

    def test_run_ok(self):
        print("test_run ok")

    def test_run_ko(self):
        print("test_run ko")
        self.assertTrue(0 == 1)

    def tearDown(self):
        print("tearDown ok")

if __name__ == '__main__':
    unittest.main()