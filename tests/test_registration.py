import unittest
from src.registration import VoterRegistration

class TestRegistration(unittest.TestCase):

    def test_register_voter(self):
        reg = VoterRegistration()
        (c_id, cr_id, t_id) = reg.register_voter('frederik')
        (c_id1, cr_id1, t_id1) = reg.register_voter('frederik')

        self.assertNotEqual(c_id, c_id1)
        self.assertNotEqual(cr_id, cr_id1)
        self.assertNotEqual(t_id, t_id1)
    
    def test_get_pseudonym(self):
        reg = VoterRegistration()
        pseudonym = reg.get_pseudonym('frederik')
        pseudonym1 = reg.get_pseudonym('frederik')
        self.assertNotEqual(pseudonym, pseudonym1)
    
    def test_register(self):
        reg = VoterRegistration()
        id = 'test_id'
        c_id = 'test_c_id'
        L = []
        self.reg.register(id, c_id, L)
        self.assertIn((id, c_id), L)


if __name__ == '__main__':
    unittest.main()