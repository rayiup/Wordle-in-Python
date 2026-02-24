import unittest

from wordle import score_guess


class TestScoreGuess(unittest.TestCase):
    def test_all_correct(self):
        self.assertEqual(
            score_guess("crane", "crane"),
            ["correct", "correct", "correct", "correct", "correct"],
        )

    def test_mixed_result(self):
        self.assertEqual(
            score_guess("crate", "trace"),
            ["present", "correct", "correct", "present", "correct"],
        )

    def test_duplicate_letters_handled(self):
        # Only one 'a' exists in answer.
        self.assertEqual(
            score_guess("array", "flame"),
            ["present", "absent", "absent", "absent", "absent"],
        )


if __name__ == "__main__":
    unittest.main()
