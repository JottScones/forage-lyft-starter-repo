import unittest
from datetime import datetime

from batteries.nubbin_battery import NubbinBattery
from batteries.spindler_battery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date      = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 4)

        spindler_battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(spindler_battery.needs_service(),
        "Battery with more than 3 years since last service should need a service.")

    def test_battery_should_not_be_serviced(self):
        current_date      = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 2)

        spindler_battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(spindler_battery.needs_service(),
        "Battery with fewer than 3 years since last service should not need a service.")

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
