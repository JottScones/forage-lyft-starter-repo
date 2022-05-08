import unittest
from tyres.carrigan_tyre import CarriganTyre
from tyres.octoprime_tyre import OctoprimeTyre

class TestCarriganTyre(unittest.TestCase):
    def test_tyre_should_be_serviced(self):
        tyre_sensor_array = [0.6,0.4,0.5,0.9]
        carrigan_tyre     = CarriganTyre(tyre_sensor_array)
        self.assertTrue(carrigan_tyre.needs_service(),
        "Tyres with at least one wheel with over 0.9 wear should need service.")

    def test_tyre_should_not_be_serviced(self):
        tyre_sensor_array = [0.6,0.4,0.5,0.89]
        carrigan_tyre     = CarriganTyre(tyre_sensor_array)
        self.assertFalse(carrigan_tyre.needs_service(),
        "Tyres with at no wheels with over 0.9 wear should not need service.")

class TestOctoprimeTyre(unittest.TestCase):
    def test_tyre_should_be_serviced(self):
        tyre_sensor_array  = [1,0.4,0.9,0.7]
        octoprime_tyre     = OctoprimeTyre(tyre_sensor_array)
        self.assertTrue(octoprime_tyre.needs_service(),
        "Tyres whose wear sums to 3 or more should need service.")

    def test_tyre_should_not_be_serviced(self):
        tyre_sensor_array  = [1,0.4,0.9,0.69]
        octoprime_tyre     = OctoprimeTyre(tyre_sensor_array)
        self.assertFalse(octoprime_tyre.needs_service(),
        "Tyre whose wear sums to less than 3 should not need service.")
