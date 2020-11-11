import sys
import random
sys.path.insert(0, '..')
from Robot.State import function, observeur, state, transition

class TestObserver(observeur.Observeur):
    def watch(self):
        while True:
            yield random.randint(0, 10)
    
    def on_danger(self):
        pass

    def on_safe(self):
        pass

    def is_dangerous(self):
        return False

class TestState(state.State):
    rSpeed = 0
    lSpeed = 0

concreteObserver1 = TestObserver(10)
concreteObserver2 = TestObserver(20)

concreteState1 = TestState(observers=[concreteObserver1, concreteObserver2])


