from unittest import TestCase
from rpi_7segment import Segments


def last(states):
    return states[-1]


def first(states):
    return states[0]


class SegmentTest(TestCase):

    def setUp(self):
        # Test without displays/GPIO-functionality disabled.
        # Segments are setup before each test. Tests are written for 7 segments.
        self.num_displays = 7
        self.debug = False
        self.segments = Segments(num_displays=self.num_displays, debug=self.debug, offline=True)

    def test_hello(self):
        states = self.segments.show("Hello!")

        self.assertEqual([' ', ' ', ' ', ' ', ' ', ' ', ' '], first(states))
        self.assertEqual([' ', 'H', 'e', 'l', 'l', 'o', '!'], last(states))

    def test_clear(self):
        states = self.segments.clear()

        self.assertEqual([' ', ' ', ' ', ' ', ' ', ' ', ' '], first(states))
        self.assertEqual([' ', ' ', ' ', ' ', ' ', ' ', ' '], last(states))

    def test_number_represented_as_string(self):
        states = self.segments.show("1234567")

        self.assertEqual([' ', ' ', ' ', ' ', ' ', ' ', ' '], first(states))
        self.assertEqual(['1', '2', '3', '4', '5', '6', '7'], last(states))

    def test_small_int(self):
        states = self.segments.show(1)

        self.assertEqual([' ', ' ', ' ', ' ', ' ', ' ', ' '], first(states))
        self.assertEqual([' ', ' ', ' ', ' ', ' ', ' ', '1'], last(states))

    def test_large_int(self):
        states = self.segments.show(1234567)

        self.assertEqual([' ', ' ', ' ', ' ', ' ', ' ', ' '], first(states))
        self.assertEqual(['1', '2', '3', '4', '5', '6', '7'], last(states))

    def test_int_larger_than_displays(self):
        states = self.segments.show(12345678, scroll_speed=0)
        self.show_states(states)

        self.assertEqual([' ', ' ', ' ', ' ', ' ', ' ', ' '], first(states))
        self.assertEqual([' ', ' ', ' ', ' ', ' ', ' ', ' '], states[(7 * 1) - 1])
        self.assertEqual([' ', ' ', ' ', ' ', ' ', ' ', ' '], states[(7 * 2) - 1])
        self.assertEqual([' ', ' ', ' ', ' ', ' ', ' ', '1'], states[(7 * 3) - 1])
        self.assertEqual([' ', ' ', ' ', ' ', ' ', '1', '2'], states[(7 * 4) - 1])
        self.assertEqual([' ', ' ', ' ', ' ', '1', '2', '3'], states[(7 * 5) - 1])
        self.assertEqual([' ', ' ', ' ', '1', '2', '3', '4'], states[(7 * 6) - 1])
        self.assertEqual([' ', ' ', '1', '2', '3', '4', '5'], states[(7 * 7) - 1])
        self.assertEqual([' ', '1', '2', '3', '4', '5', '6'], states[(7 * 8) - 1])
        self.assertEqual(['1', '2', '3', '4', '5', '6', '7'], states[(7 * 9) - 1])
        self.assertEqual(['2', '3', '4', '5', '6', '7', '8'], states[(7 * 10) - 1])
        self.assertEqual(['3', '4', '5', '6', '7', '8', ' '], states[(7 * 11) - 1])
        self.assertEqual(['4', '5', '6', '7', '8', ' ', ' '], states[(7 * 12) - 1])
        self.assertEqual(['5', '6', '7', '8', ' ', ' ', ' '], states[(7 * 13) - 1])
        self.assertEqual(['6', '7', '8', ' ', ' ', ' ', ' '], states[(7 * 14) - 1])
        self.assertEqual(['7', '8', ' ', ' ', ' ', ' ', ' '], states[(7 * 15) - 1])
        self.assertEqual(['8', ' ', ' ', ' ', ' ', ' ', ' '], states[(7 * 16) - 1])
        self.assertEqual([' ', ' ', ' ', ' ', ' ', ' ', ' '], states[(7 * 17) - 1])
        self.assertEqual([' ', ' ', ' ', ' ', ' ', ' ', ' '], last(states))

    def test_negative_int(self):
        states = self.segments.show(-123456)

        self.assertEqual([' ', ' ', ' ', ' ', ' ', ' ', ' '], first(states))
        self.assertEqual(['-', '1', '2', '3', '4', '5', '6'], last(states))

    def test_small_float(self):
        states = self.segments.show(1.0)

        self.assertEqual([' ', ' ', ' ', ' ', ' ', ' ', ' '], first(states))
        self.assertEqual([' ', ' ', ' ', ' ', ' ', '1.', '0'], last(states))

    def test_large_float(self):
        states = self.segments.show(123.4567)

        self.assertEqual([' ', ' ', ' ', ' ', ' ', ' ', ' '], first(states))
        self.assertEqual(['1', '2', '3.', '4', '5', '6', '7'], last(states))

    def test_float_larger_than_displays(self):
        states = self.segments.show(123.45678, scroll_speed=0)
        self.show_states(states)

        self.assertEqual([' ', ' ', ' ', ' ', ' ', ' ', ' '], first(states))
        self.assertEqual([' ', ' ', ' ', ' ', ' ', ' ', ' '], states[(7 * 1) - 1])
        self.assertEqual([' ', ' ', ' ', ' ', ' ', ' ', ' '], states[(7 * 2) - 1])
        self.assertEqual([' ', ' ', ' ', ' ', ' ', ' ', '1'], states[(7 * 3) - 1])
        self.assertEqual([' ', ' ', ' ', ' ', ' ', '1', '2'], states[(7 * 4) - 1])
        self.assertEqual([' ', ' ', ' ', ' ', '1', '2', '3'], states[(7 * 5) - 1])
        self.assertEqual([' ', ' ', ' ', '1', '2', '3.', '4'], states[(7 * 6) - 1])
        self.assertEqual([' ', ' ', '1', '2', '3.', '4', '5'], states[(7 * 7) - 1])
        self.assertEqual([' ', '1', '2', '3.', '4', '5', '6'], states[(7 * 8) - 1])
        self.assertEqual(['1', '2', '3.', '4', '5', '6', '7'], states[(7 * 9) - 1])
        self.assertEqual(['2', '3.', '4', '5', '6', '7', '8'], states[(7 * 10) - 1])
        self.assertEqual(['3.', '4', '5', '6', '7', '8', ' '], states[(7 * 11) - 1])
        self.assertEqual(['4', '5', '6', '7', '8', ' ', ' '], states[(7 * 12) - 1])
        self.assertEqual(['5', '6', '7', '8', ' ', ' ', ' '], states[(7 * 13) - 1])
        self.assertEqual(['6', '7', '8', ' ', ' ', ' ', ' '], states[(7 * 14) - 1])
        self.assertEqual(['7', '8', ' ', ' ', ' ', ' ', ' '], states[(7 * 15) - 1])
        self.assertEqual(['8', ' ', ' ', ' ', ' ', ' ', ' '], states[(7 * 16) - 1])
        self.assertEqual([' ', ' ', ' ', ' ', ' ', ' ', ' '], states[(7 * 17) - 1])
        self.assertEqual([' ', ' ', ' ', ' ', ' ', ' ', ' '], last(states))

    def test_negative_float(self):
        states = self.segments.show(-123.456)

        self.assertEqual([' ', ' ', ' ', ' ', ' ', ' ', ' '], first(states))
        self.assertEqual(['-', '1', '2', '3.', '4', '5', '6'], last(states))

    def test_scrolling_long_text(self):
        states = self.segments.show("Hello world!", scroll_speed=0)
        self.show_states(states)

        self.assertEqual([' ', ' ', ' ', ' ', ' ', ' ', ' '], first(states))
        self.assertEqual([' ', ' ', ' ', ' ', ' ', ' ', ' '], states[(7 * 1) - 1])
        self.assertEqual([' ', ' ', ' ', ' ', ' ', ' ', ' '], states[(7 * 2) - 1])
        self.assertEqual([' ', ' ', ' ', ' ', ' ', ' ', 'H'], states[(7 * 3) - 1])
        self.assertEqual([' ', ' ', ' ', ' ', ' ', 'H', 'e'], states[(7 * 4) - 1])
        self.assertEqual([' ', ' ', ' ', ' ', 'H', 'e', 'l'], states[(7 * 5) - 1])
        self.assertEqual([' ', ' ', ' ', 'H', 'e', 'l', 'l'], states[(7 * 6) - 1])
        self.assertEqual([' ', ' ', 'H', 'e', 'l', 'l', 'o'], states[(7 * 7) - 1])
        self.assertEqual([' ', 'H', 'e', 'l', 'l', 'o', ' '], states[(7 * 8) - 1])
        self.assertEqual(['H', 'e', 'l', 'l', 'o', ' ', 'w'], states[(7 * 9) - 1])
        self.assertEqual(['e', 'l', 'l', 'o', ' ', 'w', 'o'], states[(7 * 10) - 1])
        self.assertEqual(['l', 'l', 'o', ' ', 'w', 'o', 'r'], states[(7 * 11) - 1])
        self.assertEqual(['l', 'o', ' ', 'w', 'o', 'r', 'l'], states[(7 * 12) - 1])
        self.assertEqual(['o', ' ', 'w', 'o', 'r', 'l', 'd'], states[(7 * 13) - 1])
        self.assertEqual([' ', 'w', 'o', 'r', 'l', 'd', '!'], states[(7 * 14) - 1])
        self.assertEqual(['w', 'o', 'r', 'l', 'd', '!', ' '], states[(7 * 15) - 1])
        self.assertEqual(['o', 'r', 'l', 'd', '!', ' ', ' '], states[(7 * 16) - 1])
        self.assertEqual(['r', 'l', 'd', '!', ' ', ' ', ' '], states[(7 * 17) - 1])
        self.assertEqual(['l', 'd', '!', ' ', ' ', ' ', ' '], states[(7 * 18) - 1])
        self.assertEqual(['d', '!', ' ', ' ', ' ', ' ', ' '], states[(7 * 19) - 1])
        self.assertEqual(['!', ' ', ' ', ' ', ' ', ' ', ' '], states[(7 * 20) - 1])
        self.assertEqual([' ', ' ', ' ', ' ', ' ', ' ', ' '], states[(7 * 21) - 1])
        self.assertEqual([' ', ' ', ' ', ' ', ' ', ' ', ' '], last(states))

    def show_states(self, states):
        if self.debug:
            i = 0
            for s in states:
                print("{} {} {}".format(i, s, ('<---' if (i + 1) % self.num_displays == 0 else '')))
                i += 1
