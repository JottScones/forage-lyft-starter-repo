from battery import Battery

class SpindlerBattery(Battery):
    """docstring for SpindlerBattery."""

    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date      = current_date

    def needs_service(self):
        last_service_year      = self.last_service_date.year
        service_threshold_date = self.last_service_date.replace(year=last_service_year + 2)

        return self.current_date >= service_threshold_date