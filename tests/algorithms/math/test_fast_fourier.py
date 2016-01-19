import unittest
from src.algorithms.math.discrete_fourier import fourier_transform
import numpy as np


class TestFastFourier(unittest.TestCase):

    def test_fast_fourier(self):
        for i in range(20):
            x = np.random.random(1024)
            assert np.allclose(fourier_transform(x), np.fft.fft(x))
