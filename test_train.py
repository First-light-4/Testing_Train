import unittest
from Python_Train import Train

class TestTrain(unittest.TestCase):

    def test_train(self):
        self.assertEqual(Train(586851, 21).station(9), 21+9)
        self.assertEqual(Train(142536, 11).station(8), 11+8)
        self.assertEqual(Train(745269, 20).station(9), 20+9)
        self.assertEqual(Train(453691, 15).station(5), 15+5)

    def test_types(self):
        self.assertRaises(TypeError, Train, (586851, 21))
        self.assertRaises(TypeError, Train, ([9823, 658, 8], 85))
        self.assertRaises(TypeError, Train, ('ghhhdvbv', 6))
        # self.assertRaises(TypeError, Train, {56:89, 36:1, 2: 89}, 5)

    # def test_values(self):
    #     self.assertRaises(ValueError, Train(586851, 21).station(9), 9)
    #     self.assertRaises(ValueError, Train(586851, 21).station(4), 4)
    #     self.assertRaises(ValueError, Train(586851, 21).station(7), 7)
