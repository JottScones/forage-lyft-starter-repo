from battery import Battery

class SpindlerBattery(Battery):
    """Implementation of the Splindler Battery class."""

    def __init__(self, current_date, last_service_date):
        self.current_date      = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        last_service_year      = self.last_service_date.year
        service_threshold_date = self.last_service_date.replace(year=last_service_year + 3)

        return self.current_date >= service_threshold_date
