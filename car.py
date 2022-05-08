from serviceable import Serviceable

class Car(Serviceable, ABC):
    """Abstract Car class"""
    def __init__(self, engine, battery):
        self.engine  = engine
        self.battery = battery

    def needs_service(self):
        return self.engine.needs_service() and self.battery.needs_service()
