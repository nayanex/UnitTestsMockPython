import unittest
from car import Car
from mock import Mock
from mock import patch
from mock import create_autospec

class CarTest(unittest.TestCase):
    car = Car("Ford")

    
    @patch("car.Car.drive", autospec=True)
    def test_drive(self, mock_drive):
        mock_drive.return_value = "BRRRRRUUUMMMM"
        noise = self.car.create_and_drive()
        assert(noise == "BRRRRRUUUMMMM")

    def test_create_autospec(self):
        mock_boom = create_autospec(self.car.boom, return_value='fishy')
        # mock_boom(1, 2, 3) => fishy
        mock_boom("tnt", 3, 45)
        #mock_boom.assert_called_once_with(1, 2, 3)
    
    @patch("car.Car", autospec=True)
    def test_drive_2(self, mock_car):
        mock_car.return_value.drive.return_value = "BBBBBBBRRRRRR"
        mock_car.return_value.make = "Porsche"
        noise = self.car.create_and_drive()
        assert(noise == "BBBBBBBRRRRRR")


