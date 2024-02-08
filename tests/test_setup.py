import unittest
from parameterized import parameterized
import random 
import shamirs
from src.setup import SetupManager

class TestSetup(unittest.TestCase):

    @parameterized.expand([
       (256),
       (512),
   ])
    def test_elgamal_key_length(self, key_length):
        setupManager = SetupManager()
        (pk,sk,p,g) = setupManager.setup_elgamal(key_length)
        self.assertLessEqual(pk.__int__().bit_length(), key_length, "Public key length is not less than or equal to the specified key length")
        self.assertLessEqual(sk.__int__().bit_length(), key_length, "Private key length is not less than or equal to the specified key length")
        self.assertLessEqual(p.__int__().bit_length(), key_length, "Length of prime p is not less than or equal to the specified key length")

    def test_shamirs_shares(self):
        setupManager = SetupManager()
        threshold = random.randint(2, 5) 
        share_num = random.randint(threshold, 10) 
        (pk, sk, p, g) = setupManager.setup_elgamal(256)
        shares = setupManager.get_shamirs_shares(threshold, share_num, sk, p)
         
        """
        Tests that all shares are correctly generated
        """
        # self.assertEqual(shares.len(), share_num)

        """
        Tests that each share is a tuple of an int and byte
        """
        # for share in shares:
        #   self.assertEqual(len(share), 2)
        #   self.assertEqual(share[0], int) 
        #   self.assertEqual(share[1], byte)

        """
        Tests that the reconstructed secret matches the original secret
        """
        subset_shares = shares[:threshold]
        reconstructed_sk = shamirs.interpolate(subset_shares, threshold=threshold)

        self.assertEqual(reconstructed_sk, sk)

if __name__ == '__main__':
    unittest.main()