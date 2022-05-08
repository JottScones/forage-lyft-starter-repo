from tyre import Tyre

class OctoprimeTyre(Tyre):
    def __init__(self, tyre_sensor_array):
        self.tyre_sensor_array = tyre_sensor_array

    def needs_service(self):
        return sum(self.tyre_sensor_array) >= 3
