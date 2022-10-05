import sys
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

class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(sys.version_info[:2] < (3, 10),
                     "not supported in this python version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        self.assertTrue(1)

    @unittest.skipIf('totolib' not in sys.modules, '`totolib` not imported')
    def test_library(self):
        self.assertEqual(totolib.fct(10), 10)

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        pass

if __name__ == '__main__':
    unittest.main()