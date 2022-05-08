import unittest
from datetime import datetime

from engines.capulet_engine import CapuletEngine
from engines.sternman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine

from batteries.nubbin_battery import NubbinBattery
from batteries.spindler_battery import SpindlerBattery


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

class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date      = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)

        spindler_battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(spindler_battery.needs_service(),
        "Battery with more than 2 years since last service should need a service.")

    def test_battery_should_not_be_serviced(self):
        current_date      = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)

        spindler_battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(spindler_battery.needs_service(),
        "Battery with fewer than 2 years since last service should not need a service.")

class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date      = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)

        nubbin_battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(nubbin_battery.needs_service(),
        "Battery with more than 4 years since last service should need a service.")

    def test_battery_should_not_be_serviced(self):
        current_date      = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)

        nubbin_battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(nubbin_battery.needs_service(),
        "Battery with fewer than 4 years since last service should not need a service.")


if __name__ == '__main__':
    unittest.main()
