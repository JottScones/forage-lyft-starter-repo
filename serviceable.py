from abc import ABC, abstractmethod

class Serviceable(ABC):
    """Interface for components that require servicing"""
    @abstractmethod
    def needs_service():
        pass
