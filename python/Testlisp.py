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


class TestLisp(unittest.TestCase):
    "Test class of lisp"

    def test_lisp_expression(self):
        input = '(+ 10 20)'
        expected = 30
        actual = lisp.eval(lisp.parse(input))
        self.assertEqual(expected, actual)

        input = '(- 10 20)'
        expected = -10
        actual = lisp.eval(lisp.parse(input))
        self.assertEqual(expected, actual)

        input = '(* 5 12)'
        expected = 60
        actual = lisp.eval(lisp.parse(input))
        self.assertEqual(expected, actual)

        input = '(/ 30 5)'
        expected = 6
        actual = lisp.eval(lisp.parse(input))
        self.assertEqual(expected, actual)

        # input = '(+ 1 2 3 4 5)'
        # expected = 15
        # actual = lisp.eval(lisp.parse(input))
        # self.assertEqual(expected, actual)

        # input = '(- 100 10 1)'
        # expected = 89
        # actual = lisp.eval(lisp.parse(input))
        # self.assertEqual(expected, actual)

        # input = '(* 1 2 3 4 5)'
        # expected = 120
        # actual = lisp.eval(lisp.parse(input))
        # self.assertEqual(expected, actual)

        # input = '(/ 100 10 2)'
        # expected = 5
        # actual = lisp.eval(lisp.parse(input))
        # self.assertEqual(expected, actual)

        input = '(+ (* 5 3) 5)'
        expected = 20
        actual = lisp.eval(lisp.parse(input))
        self.assertEqual(expected, actual)

    # def test_lisp_number(self):
        # input = '#3r22'
        # expected = 8
        # actual = lisp.eval(lisp.parse(input))
        # self.assertEqual(expected, actual)

        # input = '(/ 1 2)'
        # expected = 1 / 2
        # actual = lisp.eval(lisp.parse(input))
        # self.assertEqual(expected, actual)

    def test_lisp_equal(self):
        input = '(equal? 1 1)'
        expected = True
        actual = lisp.eval(lisp.parse(input))
        self.assertEqual(expected, actual)

    def test_lisp_begin(self):
        input = '(begin (define r 10) (* pi (* r r)))'
        expected = 314.1592653589793
        actual = lisp.eval(lisp.parse(input))
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
