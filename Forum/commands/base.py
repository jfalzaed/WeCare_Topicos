from abc import ABC, abstractmethod

class Command(ABC):
    """Interfaz base para todos los comandos"""
    @abstractmethod
    def execute(self, *args, **kwargs):
        pass
