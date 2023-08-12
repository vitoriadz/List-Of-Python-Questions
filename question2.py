import unittest, math


def verbing(s: str) -> str:
    if s != 'do':
        s += 'ing' if s[-3:] != 'ing' else 'ly'
    
    return s


# Dado uma string, procurar a primeira ocorrência da substring 'not' e 'bad'
# Se 'bad' vier após o 'not', substituir todo o trecho "not ... bad" por 'good'
# Retorne a string resultante.
def not_bad(s):
  not_index = s.find('not')
  bad_index = s.find('bad')
  if not_index < bad_index:
    switch = s[not_index : (bad_index + 3)]
    return s.replace(switch, "good")
  return s


# Considere dividir uma string em duas metades.
# Se o comprimento for par, a parte da frente (front) e a parte de trás (back) são do mesmo tamanho.
# Se o comprimento for ímpar, o caracter extra irá para a parte da frente.
#
# Dado 2 strings, 'a' e 'b', retornar uma string na forma
# a front + b front + a back + b back
def front_back(a: str, b: str) -> str:
    def split_string(s: str) -> tuple:
        middle = (len(s) + 1) // 2
        return s[:middle], s[middle:]

    a_front, a_back = split_string(a)
    b_front, b_back = split_string(b)

    return f'{a_front}{b_front}{a_back}{b_back}'


class MyTest(unittest.TestCase):
    def test_verbing(self):
        self.assertEqual(verbing('hail'), 'hailing')
        self.assertEqual(verbing('swimming'), 'swimmingly')
        self.assertEqual(verbing('do'), 'do')

    def test_not_bad(self):
        self.assertEqual(not_bad('This movie is not so bad'), 'This movie is good')
        self.assertEqual(not_bad('This dinner is not that bad!'), 'This dinner is good!')
        self.assertEqual(not_bad('This tea is not hot'), 'This tea is not hot')
        self.assertEqual(not_bad("It's bad yet not"), "It's bad yet not")

    def test_front_back(self):
        self.assertEqual(front_back('abcd', 'xy'), 'abxcdy')
        self.assertEqual(front_back('abcde', 'xyz'), 'abcxydez')
        self.assertEqual(front_back('Kitten', 'Donut'), 'KitDontenut')


if __name__ == '__main__':
    unittest.main()