from tyre import Tyre

class CarriganTyre(Tyre):
    def __init__(self, tyre_sensor_array):
        self.tyre_sensor_array = tyre_sensor_array

    def needs_service(self):
        return any(sensor >= 0.9 for sensor in self.tyre_sensor_array)
