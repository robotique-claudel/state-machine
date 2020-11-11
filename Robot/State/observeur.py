import enum
from typing import Any
import random

from .transition import Transition

class ImproperlyConfigured(Exception):
    pass

class Function(enum.Enum):
    passive = 0
    blocking = 0
    triggered = 0


class Observeur:
    def __init__(self, priority: int):
        self.priority = priority
        self.type = Function.passive
        self.transitions: Transition = []

    def start(self):
        """
        Start the iteration proccess
        """
        for val in self.watch():
            if self.is_dangerous(val):
                try:
                    self.on_danger(val)
                except NotImplementedError as e:
                    raise ImproperlyConfigured("Your class definition should include a `on_danger` function") from e 
            else:
                try:
                    self.on_safe(val)
                except NotImplementedError as e:
                    raise ImproperlyConfigured("Your class definition should include a `on_safe` function") from e 

    
    def watch(self) -> Any:
        """
        Function that returns an iterator that gets the value of a sensor
        """
        raise NotImplementedError

    def on_danger(self, val: Any = None) -> None:
        """
        This function is called when a "dangerous" value is returned by `watch`
        """
        raise NotImplementedError

    def on_safe(self, val: Any = None) -> None:
        """
        This function is called when a "safe"" value is returned by `watch`
        """
        raise NotImplementedError

    def is_dangerous(self, val: Any = None) -> bool:
        """
        This function checks whether a value is "dangerous"

        Returns:  
        Boolean: True if the value is "unsafe", False if its "safe"
        """
        return False
