import unittest
import grammar.greek as greek

class GreekTests(unittest.TestCase):
    # ἀλήθεια, -ας, ἡ
    # βασιλεία, -ας, ἡ
    # Γαλιλαία, -ας, ἡ
    # γλῶσσα, -ης, ἡ
    # δικαιοσύνη, -ης, ἡ
    # δόξα, -ης, ἡ
    # ἐκκλησία, -ας, ἡ
    # ἐπαγγελία, -ας, ἡ
    # ζωή, -ής, ἡ
    # θάλασσα, -ης, ἡ
    # καρδία, -ας, ἡ
    # κεφαλή, -ής, ἡ
    # παραβολή, -ής, ἡ
    # ψυχή, -ής, ἡ
    # ὥρα, -ας, ἡ

    def test_ac_init_form(self):
        #ἀλήθεια, -ας, ἡ
        word = greek.Noun("ἀληθει", "ας", greek.Declension.First, greek.Gender.Female)
        self.assertEqual(word.create_initial_form(), 'ἀληθεια')

    def test_ac_genitive_singular(self):
        #ἀλήθεια, -ας, ἡ
        word = greek.Noun("ἀληθει", "ας", greek.Declension.First, greek.Gender.Female)
        declined = word.decline(greek.Number.Single, greek.Case.Genitive)
        self.assertEqual(declined, 'ἀληθειᾱς')
