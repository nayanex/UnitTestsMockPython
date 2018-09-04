import unittest
from mock import MagicMock
from mock import Mock
from mock import patch
from mock import create_autospec
from phonebook import Phonebook
from dummy import Dummy

class MockTest(unittest.TestCase):
    
    @unittest.skip("WIP")
    def test_mock_up_thing(self):
        thing = Phonebook()
        
        #<MagicMock id='140115817358032'>
        thing.method = MagicMock(return_value=3)
        
        # It is going to return 3
        thing.method(3, 4, 5, key='value')
        thing.method.assert_called_with(3, 4, 5, key='value')
    
    # not working :(
    @unittest.skip("WIP")
    @patch('phonebook.Phonebook')
    def test_if_MockPhonebook_is_called(self, MockPhonebook):
        Phonebook()
        assert MockPhonebook is Phonebook
        assert MockPhonebook.called

    @unittest.skip("WIP")
    def test_patch_as_context_manager(self):
        with patch.object(Phonebook, 'lookup', return_value=None) as mock_method:
            thing = Phonebook()
            thing.lookup("Nayana")
        mock_method.assert_called_with("Nayana")
    
    # patch.dict() for setting values in a dictionary just during a scope and restoring the dictionary to its original state when the test ends.
    @unittest.skip("WIP")
    def test_patch_dict(self):
        foo = {'key':'value'}
        original = foo.copy()
        with patch.dict(foo, {'newkey':'newvalue'}, clear = True):
            assert foo == {'newkey':'newvalue'}
        assert foo == original

    # For ensuring that the mock objects in your tests have the same api as the objects they are replacing
    @unittest.skip("WIP")
    def test_create_autospec(self):
        dummy = Mock()
        mock_function = create_autospec(dummy.function, return_value='fishy')
        # mock_function(1, 2, 3) => fishy
        mock_function.assert_called_once_with(1, 2, 3)

    @unittest.skip("WIP")
    def test_assert_called_once(self):
        mock = Mock()
        mock.method()
        mock.method.test_assert_called_once()

    @unittest.skip("WIP")
    def test_assert_called_once_with(self):
        mock = Mock(return_value=None)
        mock('foo', bar='baz')
        mock.assert_called_once_with('foo', bar='baz')

    # The assert passes if the mock has ever been called, unlike assert_called_with() and assert_called_once_with() 
    # that only pass if the call is the most recent one 
    @unittest.skip("WIP")
    def test_assert_any_call(self):
        mock = Mock(return_value=None)
        mock(1, 2, arg='thing')
        mock('some', 'thing', 'else')
        mock.assert_any_call(1, 2, arg='thing')

    



        