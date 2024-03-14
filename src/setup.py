from Crypto.PublicKey import ElGamal, ECC
from Crypto.Random import get_random_bytes
from Crypto.Signature import eddsa
from zkpy.ptau import PTau
from zkpy.circuit import Circuit, GROTH
from src.bulletinboard import BullitinBoard
import os
import shamirs

class SetupManager:
    def __init__(self):
        pass 
    
    def setup(self):
        (pk,sk,p,g) = self.setup_elgamal(256)
        shares = self.get_shamirs_shares(10,20,sk,p)
        self.setup_digital_signature()
        #self.setup_zk_SNARK()

    def setup_elgamal(self,keysize):
        ElGamalKey = ElGamal.generate(keysize, get_random_bytes)

        BullitinBoard.set_elgamal(ElGamalKey.y.__int__(), ElGamalKey.p.__int__(), ElGamalKey.g.__int__())
        BullitinBoard.set_private_param("elgamal_priv_key", ElGamalKey.x.__int__())
        return (ElGamalKey.y, ElGamalKey.x, ElGamalKey.p, ElGamalKey.g)

    def get_shamirs_shares(self,threshold,share_num,sk,p):
        shares = shamirs.shares(sk.__int__(), quantity=share_num, modulus=p.__int__(), threshold=threshold)
        return shares

    def setup_digital_signature(self):
        signing_key = ECC.generate(curve='ed25519')
        verification_key = eddsa.import_public_key(signing_key.public_key().export_key(format='raw'))

        BullitinBoard.set_digital_signature(verification_key.export_key(format='OpenSSH'))
        BullitinBoard.set_private_param("signing_key", signing_key.export_key(format='PEM'))
        return (signing_key,verification_key)        

    def setup_zk_SNARK(self):
        working_dir = os.path.dirname(os.path.realpath(__file__)) + "/../circuits/FullCircuit/"

        ptau = PTau(ptau_file=working_dir+"../ptau_15.ptau")

        circuit = Circuit("circuit.circom", working_dir=working_dir,output_dir=working_dir)
        circuit.compile()
        circuit.get_info()
        circuit.print_constraints()
        circuit.setup(GROTH, ptau)
        circuit.contribute_phase2(entropy="p1", output_file=working_dir+"final.zkey")
        BullitinBoard.set_zkey_file_name(circuit.zkey_file)
