from .function import Function


class ImproperCall(Exception):
    pass



class State:
    rSpeed: int = 0
    lSpeed: int = 0

    def __init__(self, observers):
        self.observers = observers

    def check_transition_validity(self, observer_triggered):
        if observer_triggered.type != Function.triggered: # Sanity check
            raise ImproperCall("The observer supplied wasn't triggered")

        observer_p = observer_triggered.priority

        for observer in self.observers:
            if observer.type == Function.passive: # Observers doesn't care
                pass
            elif observer.type == Function.blocking: # Observer is blocking
                if observer.priority < observer_p:
                    pass # Allowed to override
                else:
                    return False # Not allowed to override
        return True

