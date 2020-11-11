import random
import unittest
import sys

import createObjects

class TestStates(unittest.TestCase):
    
    def test_transition_validity(self):
        with self.assertRaises(createObjects.state.ImproperCall):
            createObjects.concreteState1.check_transition_validity(createObjects.concreteObserver1)

        createObjects.concreteObserver1.type = createObjects.function.Function.triggered
        self.assertTrue(createObjects.concreteState1.check_transition_validity(createObjects.concreteObserver1))

        createObjects.concreteState1.observers[1].type = createObjects.function.Function.blocking
        self.assertFalse(createObjects.concreteState1.check_transition_validity(createObjects.concreteObserver1))


if __name__ == '__main__':
    unittest.main()
