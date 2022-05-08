import unittest
from tyres.carrigan_tyre import CarriganTyre

class TestCarriganTyre(unittest.TestCase):
    def test_tyre_should_be_serviced(self):
        tyre_sensor_array = [0.6,0.4,0.5,0.9]
        carrigan_tyre     = CarriganTyre(tyre_sensor_array)
        self.assertTrue(carrigan_tyre.needs_service(),
        "Tyre with at least one wheel with over 0.9 wear should need service.")

    def test_tyre_should_not_be_serviced(self):
        tyre_sensor_array = [0.6,0.4,0.5,0.89]
        carrigan_tyre     = CarriganTyre(tyre_sensor_array)
        self.assertFalse(carrigan_tyre.needs_service(),
        "Tyre with at no wheels with over 0.9 wear should not need service.")
