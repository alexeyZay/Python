import unittest
import greet

class Test_User_Greet(unittest.TestCase):
    def test_get_user_greet(self):
        '''
        some comment for this test
        '''
        self.assertEqual(greet.greet_user('Jack',False),'Hello Jack! How are you?')
    
    def test_get_anemy_greet(self):
        '''
        some comment for this test
        '''
        self.assertEqual(greet.greet_user('Nick',True),'Hey Nick! Where are you? I will find you')
    
    def test_cooking_enough(self):
        '''
        some comment for this test
        '''
        self.assertEqual(greet.cooking_burgers(5,False),'You eat more then 5 burgers! Why you still hungry?')
    
    def test_cooking_not_enough(self):
        '''
        some comment for this test
        '''
        self.assertEqual(greet.cooking_burgers(2,True),'Need more? I will bring them to you')    
        
if __name__=="__main__":
    unittest.main()
    
        