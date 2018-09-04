import unittest
from mock import MagicMock
from mock import Mock

# Useful for raising exceptions or dynamically changing return values
class SideEffectMock:
    def __init__(self):
        self.values = {'a': 1, 'b': 2, 'c':3}

    mock = Mock()
        
    def side_effect(self, arg):
        return self.values[arg]

    mock.side_effect = side_effect
    #print mock('a') => 1
    #print mock('b') => 2
    #print mock('c') => 3

    # If side_effect is an iterable then each call to the mock will return the next value from the iterable.
    mock.side_effect = [5, 4, 3, 2, 1]

    print mock() #5
    print mock() #4
    print mock() #3
    print mock() #2
    print mock() #1

    
   
    