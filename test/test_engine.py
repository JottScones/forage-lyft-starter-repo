import unittest

from engines.capulet_engine import CapuletEngine
from engines.sternman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine

class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage      = 30001
        last_service_mileage = 0

        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(capulet_engine.needs_service(),
        "Engines that have done more than 30k miles should need a service.")

    def test_engine_should_not_be_serviced(self):
        current_mileage      = 30000
        last_service_mileage = 0

        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(capulet_engine.needs_service(),
        "Engines that have done less than 30k miles should not need a service.")

class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_is_on = True

        sternman_engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(sternman_engine.needs_service(),
        "Engines with warning light should need a service.")

    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False

        sternman_engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(sternman_engine.needs_service(),
        "Engines with no warning light should not need a service.")

class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage      = 60001
        last_service_mileage = 0

        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(willoughby_engine.needs_service(),
        "Engines that have done more than 30k miles should need a service.")

    def test_engine_should_not_be_serviced(self):
        current_mileage      = 60000
        last_service_mileage = 0

        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(willoughby_engine.needs_service(),
        "Engines that have done less than 30k miles should not need a service.")
