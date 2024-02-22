from Crypto.PublicKey import ElGamal, ECC
from Crypto.Random import get_random_bytes
from Crypto.Signature import eddsa
from zkpy.ptau import PTau
from zkpy.circuit import Circuit, GROTH
from src.bulletinboard import BullitinBoard
from src.utility import Utility
import os
#import subprocess
import shamirs

class SetupManager:
    def __init__(self):
        pass 
    
    def setup(self):
        (pk,sk,p,g) = self.setup_elgamal(256)
        shares = self.get_shamirs_shares(10,20,sk,p)
        self.setup_digital_signature()
        m = b'Hello world!'
        (com,rand) = Utility.SHA_commit(m)
        # print(m)
        # print(com)
        # print(rand)
        # print(Utility.SHA_commit_verify(com,m,rand))
        #self.setup_zk_SNARK()

    def setup_elgamal(self,keysize):
        ElGamalKey = ElGamal.generate(keysize, get_random_bytes)
        # print("y/publickey:", ElGamalKey.y)
        # print("x/privateKey:", ElGamalKey.x)
        # print("p:", ElGamalKey.p)
        # print("g:", ElGamalKey.g)

        #print(ElGamalKey.x.to_bytes())
        # shares = shamirs.shares(ElGamalKey.x.__int__(), quantity=share_num, modulus=ElGamalKey.p.__int__(), threshold=threshold)
        #print("shares:", shares)
        
        # privateKey = shamirs.interpolate(shares[5:15], threshold=10)
        # print("pk:", privateKey)
        # print("pk:", ElGamalKey.x)

        BullitinBoard.set_elgamal(ElGamalKey.y.__int__(), ElGamalKey.p.__int__(), ElGamalKey.g.__int__())
        BullitinBoard.set_private_param("elgamal_priv_key", ElGamalKey.x.__int__())
        return (ElGamalKey.y, ElGamalKey.x, ElGamalKey.p, ElGamalKey.g)

    def get_shamirs_shares(self,threshold,share_num,sk,p):
        shares = shamirs.shares(sk.__int__(), quantity=share_num, modulus=p.__int__(), threshold=threshold)
        return shares

    def setup_digital_signature(self):
        signing_key = ECC.generate(curve='ed25519')
        verification_key = eddsa.import_public_key(signing_key.public_key().export_key(format='raw'))

        # message = b'Hello, World!'
        # message1 = b'Hello, World!2'
        # signer = eddsa.new(signing_key, 'rfc8032')
        # verifier = eddsa.new(verification_key,'rfc8032')
        # h = signer.sign(message)
        # print(verifier.verify(message1,h))
        # print("sign: ", signer)
        # print("verify: ", verifier)
        #print(DSS.DssSigScheme.can_sign(sign))

        BullitinBoard.set_digital_signature(verification_key.export_key(format='OpenSSH'))
        BullitinBoard.set_private_param("signing_key", signing_key.export_key(format='PEM'))
        return (signing_key,verification_key)        

    def setup_zk_SNARK(self):
        working_dir = os.path.dirname(os.path.realpath(__file__)) + "/../circuits/FullCircuit/"
        # ptau = PTau(working_dir=working_dir)
        # ptau.start(constraints='15')
        # ptau.contribute()
        # ptau.beacon()
        # ptau.prep_phase2()

        ptau = PTau(ptau_file=working_dir+"../ptau_15.ptau")

        # Args:
        #     circ_file (str): Path to a circom circuit file.
        #     output_dir (str, optional): Path to where generated files should be outputted. Defaults to the current directory.
        #     working_dir (str, optional): Path that all given file paths are relative to. Defaults to the current directory
        #     r1cs (str, optional): Optional path to a pre-generated r1cs file.
        #     sym_file (str, optional): Optional path to a pre-generated symbols file.
        #     js_dir (str, optional): Optional path to a pre-generated directory with JS files.
        #     wasm (str, optional): Optional path to a pre-generated wasm file.
        #     witness (str, optional): Optional path to a witness file.
        #     zkey (str, optional): Optional path to a pre-generated zkey file.
        #     vkey (str, optional): Optional path to a pre-generated verification key file.

        circuit = Circuit("NullVote.circom", working_dir=working_dir,output_dir=working_dir)

        circuit.compile()

        circuit.get_info()

        circuit.print_constraints()

        # circuit.gen_witness(working_dir+"input.json")
     
        circuit.setup(GROTH, ptau)

        circuit.contribute_phase2(entropy="p1", output_file=working_dir+"final.zkey")
        print(circuit.zkey_file)
        BullitinBoard.set_zkey_file_name(circuit.zkey_file)

        # circuit.prove(GROTH)

        # circuit.export_vkey(output_file=working_dir+"vkey.json")

        # circuit.verify(GROTH, vkey_file=working_dir+"vkey.json", public_file=working_dir+"public.json", proof_file=working_dir+"proof.json")
