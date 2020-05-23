from django.test import TestCase
from .models import Location,Image,Category
import datetime as dt
# Create your tests here.
class LocationTestClass(TestCase):
    def setup(self):
        '''
        Method that allows us to create an instance of the Location class before every test.
        '''
        self.paris= Location(loc_name = 'France')
        self.paris.save_location()

    def test_instance(self):
        '''
        test to confirm that the object is being instantiated correctly
        '''
        self.assertTrue(isinstance(self.paris,Location))
    
    def test_updating_location(self):
        location = Location.get_location_id(self.nairobi.id)
        location.update_location('Spain')
        location = Location.get_location_id(self.nairobi.id)
        self.assertTrue(location.loc_name == 'Spain')
    
    def tearDown(self):
        '''
        Method to delete  instance of our location model from the database after each test
        '''
        self.paris.delete_location()