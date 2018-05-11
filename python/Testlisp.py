import unittest
import lisp

class TestLispParsing(unittest.TestCase):
    "Test class of lisp parsing"

    def test_lisp_tokenize(self):
        "Test for lisp.tokenize"
        expected = ['(', '+', '1', '1', ')']
        actual = lisp.tokenize('(+ 1 1)')
        self.assertEqual(expected, actual)

        expected = ['(', '(', '+', '1', '1', ')', '(', '-', '1', '1', ')', ')']
        actual = lisp.tokenize('((+ 1 1)(- 1 1))')
        self.assertEqual(expected, actual)

    def test_lisp_atom(self):
        "Test for lisp.atom"
        expected = 1
        actual = lisp.atom('1')
        self.assertEqual(expected, actual)

        expected = 1.1
        actual = lisp.atom('1.1')
        self.assertEqual(expected, actual)

        expected = 1
        actual = lisp.atom(1.1)
        self.assertEqual(expected, actual)

        expected = 1.1
        actual = lisp.atom(1.1)
        self.assertNotEqual(expected, actual)

    def test_lisp_read_from_tokens(self):
        "Test for lisp.read_from_tokens"
        expected = [['+', 1, 1], ['-', 1, 1]]
        actual = lisp.read_from_tokens(['(', '(', '+', '1', '1', ')', '(', '-', '1', '1', ')', ')'])
        self.assertEqual(expected, actual)

    def test_lisp_parse(self):
        "Test for lisp.parse"
        expected = [['+', 1, 1], ['-', 1, 1]]
        actual = lisp.parse('((+ 1 1)(- 1 1))')
        self.assertEqual(expected, actual)


class TestLispaEnvironments(unittest.TestCase):
    "Test class of lisp environments"

    def test_lisp_Env(self):
        "Test for lisp.Env"
        env = lisp.Env()

if __name__ == "__main__":
    unittest.main()
