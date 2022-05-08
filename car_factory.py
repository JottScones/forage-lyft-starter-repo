from car import Car
from engines.capulet_engine import CapuletEngine
from engines.sternman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine

from batteries.nubbin_battery import NubbinBattery
from batteries.spindler_battery import SpindlerBattery

class CarFactory(object):
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        capulet_engine   = CapuletEngine(current_mileage, last_service_mileage)
        spindler_battery = SpindlerBattery(current_date, last_service_date)
        return Car(capulet_engine, spindler_battery)

    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        spindler_battery  = SpindlerBattery(current_date, last_service_date)
        return Car(willoughby_engine, spindler_battery)

    def create_palindrome(current_date, last_service_date, warning_light_is_on):
        sternman_engine  = SternmanEngine(warning_light_is_on)
        spindler_battery = SpindlerBattery(current_date, last_service_date)
        return Car(sternman_engine, spindler_battery)

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        nubbin_battery    = NubbinBattery(current_date, last_service_date)
        return Car(willoughby_engine, nubbin_battery)

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        nubbin_battery = NubbinBattery(current_date, last_service_date)
        return Car(capulet_engine, nubbin_battery)
