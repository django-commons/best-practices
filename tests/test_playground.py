from unittest import TestCase

from src.django_commons_best_practices import playground


class TestPlayground(TestCase):
    def test_seesaw(self):
        seesaw = playground.seesaw()
        self.assertEqual(next(seesaw), "see")
        self.assertEqual(next(seesaw), "saw")
        self.assertEqual(next(seesaw), "see")
        self.assertEqual(next(seesaw), "saw")
        self.assertEqual(next(seesaw), "see")
        self.assertEqual(next(seesaw), "saw")
